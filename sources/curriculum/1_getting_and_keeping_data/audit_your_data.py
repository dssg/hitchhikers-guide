#!/usr/bin/env python3
"""
pg_data_audit.py — programmatic data audit for a PostgreSQL database.

Sweeps EVERY table and EVERY column and reports, per column:
  - exact row count          - distinct-value count
  - non-null / null counts   - min / max (numbers & dates)
  - % null                   - max string length (text columns)
and flags candidate keys, constant columns, and all-null columns.

DESIGN: computation is pushed into Postgres. Python discovers the schema from
information_schema, then builds ONE aggregate query per table so every column is
profiled in a single server-side scan. Rows never get pulled into Python, so this
scales to large tables. count(DISTINCT ...) is the only expensive part — use
--no-distinct on very large tables, or sample first.

USAGE
    # Credentials come from the environment — never hardcode them.
    export DATABASE_URL="postgresql://user@host:5432/dbname"   # password via PGPASSWORD or ~/.pgpass
    python pg_data_audit.py --schema public --out ./audit_out

    # Multiple schemas, skip the expensive distinct counts, and sweep top values
    python pg_data_audit.py --schema public --schema staging --no-distinct --top-values

DEPENDENCIES
    pip install "psycopg2-binary>=2.9" pandas
"""

import os
import sys
import argparse

import pandas as pd
import psycopg2
from psycopg2 import sql

# --- type categories (from information_schema.columns.data_type) -------------
NUMERIC_TYPES = {
    "smallint", "integer", "bigint", "decimal", "numeric",
    "real", "double precision", "money",
}
TEMPORAL_TYPES = {
    "date", "time without time zone", "time with time zone",
    "timestamp without time zone", "timestamp with time zone", "interval",
}
TEXT_TYPES = {"character varying", "character", "text", "citext"}
# `json` has no equality operator, so count(DISTINCT json_col) errors out.
NO_DISTINCT_TYPES = {"json"}


# --- connection --------------------------------------------------------------
def get_connection():
    """Connect using DATABASE_URL if set, else standard PG* environment vars."""
    dsn = os.environ.get("DATABASE_URL")
    conn = psycopg2.connect(dsn) if dsn else psycopg2.connect()
    conn.autocommit = True  # read-only profiling; avoids aborted-transaction cascades
    return conn


# --- schema discovery --------------------------------------------------------
def list_tables(conn, schemas, include_views=False):
    """Return a DataFrame of tables (and optionally views) with approx size."""
    relkinds = ["r", "p"] + (["v", "m"] if include_views else [])
    q = """
        SELECT n.nspname                       AS schema_name,
               c.relname                       AS table_name,
               c.reltuples::bigint             AS approx_rows,
               pg_total_relation_size(c.oid)   AS total_bytes,
               pg_size_pretty(pg_total_relation_size(c.oid)) AS total_size
        FROM pg_class c
        JOIN pg_namespace n ON n.oid = c.relnamespace
        WHERE c.relkind = ANY(%s)
          AND n.nspname = ANY(%s)
        ORDER BY pg_total_relation_size(c.oid) DESC;
    """
    with conn.cursor() as cur:
        cur.execute(q, (relkinds, schemas))
        rows = cur.fetchall()
        cols = [d.name for d in cur.description]
    return pd.DataFrame(rows, columns=cols)


def get_columns(conn, schema, table):
    """Return [(column_name, data_type), ...] in ordinal order."""
    q = """
        SELECT column_name, data_type
        FROM information_schema.columns
        WHERE table_schema = %s AND table_name = %s
        ORDER BY ordinal_position;
    """
    with conn.cursor() as cur:
        cur.execute(q, (schema, table))
        return cur.fetchall()


# --- query building ----------------------------------------------------------
def build_table_profile_query(schema, table, columns, include_distinct=True):
    """
    Build a single SELECT that profiles all given columns in one scan.
    Returns (query, meta) where meta maps each result alias back to (column, stat).
    Identifiers are quoted via psycopg2.sql, so odd column names are safe.
    """
    select_parts = [sql.SQL("count(*) AS n_rows")]
    meta = []  # list of {"alias", "column", "stat"}

    def add(col, stat, expr):
        alias = f"c{len(meta)}__{stat}"  # alias is index-based, so it never collides
        select_parts.append(
            sql.SQL("{expr} AS {alias}").format(expr=expr, alias=sql.Identifier(alias))
        )
        meta.append({"alias": alias, "column": col, "stat": stat})

    for name, dtype in columns:
        ident = sql.Identifier(name)
        add(name, "non_null", sql.SQL("count({c})").format(c=ident))
        if include_distinct and dtype not in NO_DISTINCT_TYPES:
            add(name, "ndistinct", sql.SQL("count(DISTINCT {c})").format(c=ident))
        if dtype in NUMERIC_TYPES or dtype in TEMPORAL_TYPES:
            add(name, "min", sql.SQL("min({c})").format(c=ident))
            add(name, "max", sql.SQL("max({c})").format(c=ident))
            add(name, "mean", sql.SQL("average({c})").format(c=ident))
        if dtype in TEXT_TYPES:
            add(name, "max_len", sql.SQL("max(length({c}))").format(c=ident))

    query = sql.SQL("SELECT {fields} FROM {sch}.{tbl}").format(
        fields=sql.SQL(", ").join(select_parts),
        sch=sql.Identifier(schema),
        tbl=sql.Identifier(table),
    )
    return query, meta


def run_profile_query(conn, schema, table, columns, include_distinct=True):
    query, meta = build_table_profile_query(schema, table, columns, include_distinct)
    with conn.cursor() as cur:
        cur.execute(query)
        row = cur.fetchone()
        names = [d.name for d in cur.description]
    result = dict(zip(names, row))
    return result.get("n_rows"), result, meta


# --- assembling per-column rows ---------------------------------------------
def assemble_rows(schema, table, n_rows, result, meta, columns):
    """Turn the single wide result row into one tidy row per column."""
    stats = {
        name: {
            "schema": schema, "table": table, "column": name, "data_type": dtype,
            "n_rows": n_rows, "non_null": None, "n_null": None, "pct_null": None,
            "ndistinct": None, "min": None, "max": None, "max_len": None,
        }
        for name, dtype in columns
    }
    for m in meta:
        stats[m["column"]][m["stat"]] = result.get(m["alias"])

    out = []
    for name, dtype in columns:
        s = stats[name]
        nn = s["non_null"]
        if nn is not None and n_rows:
            s["n_null"] = n_rows - nn
            s["pct_null"] = round(100.0 * (n_rows - nn) / n_rows, 2)
        nd = s["ndistinct"]
        s["is_all_null"] = (nn == 0) if nn is not None else None
        s["is_constant"] = (nd == 1) if nd is not None else None
        s["is_unique_candidate"] = bool(
            nd is not None and nn is not None and n_rows
            and nd == n_rows and nn == n_rows
        )
        out.append(s)
    return out


def profile_table(conn, schema, table, columns, include_distinct=True):
    """Profile a whole table; fall back to per-column if the wide query fails."""
    try:
        n_rows, result, meta = run_profile_query(conn, schema, table, columns, include_distinct)
        return assemble_rows(schema, table, n_rows, result, meta, columns)
    except psycopg2.Error as e:
        print(f"    ! combined query failed ({e.pgcode}); profiling columns one by one")
        rows = []
        for col in columns:
            try:
                n_rows, result, meta = run_profile_query(conn, schema, table, [col], include_distinct)
                rows += assemble_rows(schema, table, n_rows, result, meta, [col])
            except psycopg2.Error as ce:
                print(f"      ! could not profile {table}.{col[0]}: {ce.pgcode}")
                rows.append({
                    "schema": schema, "table": table, "column": col[0],
                    "data_type": col[1], "note": "profiling failed",
                })
        return rows


# --- optional: top values (great for spotting sentinel / missing codes) ------
def top_values(conn, schema, table, column, n=20):
    q = sql.SQL(
        "SELECT {col} AS value, count(*) AS n FROM {s}.{t} "
        "GROUP BY {col} ORDER BY n DESC LIMIT %s"
    ).format(col=sql.Identifier(column), s=sql.Identifier(schema), t=sql.Identifier(table))
    with conn.cursor() as cur:
        cur.execute(q, (n,))
        rows = cur.fetchall()
    return [{"schema": schema, "table": table, "column": column,
             "value": str(v), "n": cnt} for v, cnt in rows]


# --- optional helper: test a candidate (composite) key ----------------------
def check_unique(conn, schema, table, key_columns):
    """Return (n_rows, n_distinct_key) — equal means the key uniquely identifies rows."""
    cols = sql.SQL(", ").join(sql.Identifier(c) for c in key_columns)
    if len(key_columns) == 1:
        distinct_expr = sql.SQL("count(DISTINCT {c})").format(c=sql.Identifier(key_columns[0]))
    else:
        distinct_expr = sql.SQL("count(DISTINCT ({c}))").format(c=cols)
    q = sql.SQL("SELECT count(*), {d} FROM {s}.{t}").format(
        d=distinct_expr, s=sql.Identifier(schema), t=sql.Identifier(table))
    with conn.cursor() as cur:
        cur.execute(q)
        return cur.fetchone()


# --- Level 5: relationships between tables -----------------------------------
def list_foreign_keys(conn, schemas):
    """Foreign keys that are formally DECLARED in the catalog."""
    q = """
        SELECT tc.table_schema  AS child_schema,  tc.table_name  AS child_table,
               kcu.column_name  AS child_column,
               ccu.table_schema AS parent_schema, ccu.table_name AS parent_table,
               ccu.column_name  AS parent_column
        FROM information_schema.table_constraints tc
        JOIN information_schema.key_column_usage kcu
          ON tc.constraint_name = kcu.constraint_name
         AND tc.table_schema    = kcu.table_schema
        JOIN information_schema.constraint_column_usage ccu
          ON ccu.constraint_name = tc.constraint_name
         AND ccu.table_schema    = tc.table_schema
        WHERE tc.constraint_type = 'FOREIGN KEY'
          AND tc.table_schema = ANY(%s);
    """
    with conn.cursor() as cur:
        cur.execute(q, (schemas,))
        rows = cur.fetchall()
        cols = [d.name for d in cur.description]
    return pd.DataFrame(rows, columns=cols)


def orphan_count(conn, cs, ct, cc, ps, pt, pc):
    """Child rows whose key has no match in the parent (a broken/partial link)."""
    q = sql.SQL(
        "SELECT count(*) FROM {cs}.{ct} c LEFT JOIN {ps}.{pt} p "
        "ON c.{cc} = p.{pc} WHERE p.{pc} IS NULL AND c.{cc} IS NOT NULL"
    ).format(cs=sql.Identifier(cs), ct=sql.Identifier(ct), cc=sql.Identifier(cc),
             ps=sql.Identifier(ps), pt=sql.Identifier(pt), pc=sql.Identifier(pc))
    with conn.cursor() as cur:
        cur.execute(q)
        return cur.fetchone()[0]


def max_children_per_key(conn, cs, ct, cc):
    """Largest number of child rows sharing one key value -> cardinality / fan-out."""
    q = sql.SQL(
        "SELECT coalesce(max(cnt), 0) FROM "
        "(SELECT {cc} AS k, count(*) AS cnt FROM {cs}.{ct} "
        "WHERE {cc} IS NOT NULL GROUP BY {cc}) s"
    ).format(cs=sql.Identifier(cs), ct=sql.Identifier(ct), cc=sql.Identifier(cc))
    with conn.cursor() as cur:
        cur.execute(q)
        return cur.fetchone()[0]


def discover_relationships(conn, schemas, col_df):
    """
    Map how tables link. Two sources:
      1. DECLARED foreign keys (from the catalog).
      2. INFERRED links: a column whose name matches a candidate-key column in
         another table (e.g. claims.person_id -> persons.person_id).
    Every candidate is validated by counting orphans and measuring cardinality.
    """
    edges, seen = [], set()

    declared = list_foreign_keys(conn, schemas)
    for _, r in declared.iterrows():
        key = (r.child_schema, r.child_table, r.child_column, r.parent_table)
        seen.add(key)
        edges.append(dict(
            child_schema=r.child_schema, child_table=r.child_table,
            child_column=r.child_column, parent_schema=r.parent_schema,
            parent_table=r.parent_table, parent_column=r.parent_column, declared=True))

    # Candidate parents = columns that look like primary keys (unique, no nulls).
    if "is_unique_candidate" in col_df:
        parents = col_df[col_df["is_unique_candidate"] == True]  # noqa: E712
        parent_index = {}
        for _, p in parents.iterrows():
            parent_index.setdefault(p["column"], []).append(
                (p["schema"], p["table"], p["column"]))

        for _, c in col_df.iterrows():
            for (ps, pt, pcol) in parent_index.get(c["column"], []):
                if (ps, pt) == (c["schema"], c["table"]):
                    continue  # don't link a table to itself on its own PK
                key = (c["schema"], c["table"], c["column"], pt)
                if key in seen:
                    continue
                seen.add(key)
                edges.append(dict(
                    child_schema=c["schema"], child_table=c["table"],
                    child_column=c["column"], parent_schema=ps,
                    parent_table=pt, parent_column=pcol, declared=False))

    out = []
    for e in edges:
        try:
            e["orphan_rows"] = orphan_count(
                conn, e["child_schema"], e["child_table"], e["child_column"],
                e["parent_schema"], e["parent_table"], e["parent_column"])
            mc = max_children_per_key(conn, e["child_schema"], e["child_table"], e["child_column"])
            e["max_children_per_parent"] = mc
            e["cardinality_guess"] = "1:1" if mc <= 1 else "1:many (fan-out risk)"
            out.append(e)
        except psycopg2.Error:
            pass  # skip links that can't be evaluated (type mismatch, etc.)
    return pd.DataFrame(out)


# --- main --------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description="Programmatic Postgres data audit.")
    ap.add_argument("--schema", action="append", default=None,
                    help="Schema to audit (repeatable). Default: public")
    ap.add_argument("--out", default="./audit_out", help="Output directory")
    ap.add_argument("--no-distinct", action="store_true",
                    help="Skip count(DISTINCT) — much faster on huge tables")
    ap.add_argument("--include-views", action="store_true",
                    help="Also profile views/materialized views (runs the view)")
    ap.add_argument("--top-values", action="store_true",
                    help="After profiling, dump top values for low-cardinality columns")
    ap.add_argument("--max-cardinality", type=int, default=50,
                    help="Columns with ndistinct <= this get a top-values dump")
    ap.add_argument("--top-n", type=int, default=20, help="How many top values to list")
    ap.add_argument("--relationships", action="store_true",
                    help="Discover declared + inferred table links and check orphans")
    args = ap.parse_args()

    schemas = args.schema or ["public"]
    include_distinct = not args.no_distinct
    os.makedirs(args.out, exist_ok=True)

    conn = get_connection()
    print(f"Connected. Auditing schemas: {', '.join(schemas)}\n")

    tables = list_tables(conn, schemas, include_views=args.include_views)
    if tables.empty:
        print("No tables found in the given schema(s).")
        return
    print(f"Found {len(tables)} tables.\n")

    all_rows, exact_counts = [], {}
    for i, t in enumerate(tables.itertuples(index=False), start=1):
        cols = get_columns(conn, t.schema_name, t.table_name)
        print(f"[{i}/{len(tables)}] {t.schema_name}.{t.table_name} "
              f"(~{t.approx_rows:,} rows, {len(cols)} cols, {t.total_size})")
        rows = profile_table(conn, t.schema_name, t.table_name, cols, include_distinct)
        all_rows.extend(rows)
        if rows and rows[0].get("n_rows") is not None:
            exact_counts[(t.schema_name, t.table_name)] = rows[0]["n_rows"]

    col_df = pd.DataFrame(all_rows)

    # attach exact row count + column count to the inventory
    tables["exact_rows"] = tables.apply(
        lambda r: exact_counts.get((r["schema_name"], r["table_name"])), axis=1)
    tables["n_columns"] = tables.apply(
        lambda r: int((col_df["schema"] == r["schema_name"]).__and__(
            col_df["table"] == r["table_name"]).sum()), axis=1)

    inv_path = os.path.join(args.out, "table_inventory.csv")
    col_path = os.path.join(args.out, "column_profile.csv")
    tables.to_csv(inv_path, index=False)
    col_df.to_csv(col_path, index=False)

    # --- console summary -----------------------------------------------------
    print("\n" + "=" * 64)
    print("SUMMARY")
    print("=" * 64)
    print(f"Tables profiled : {len(tables)}")
    print(f"Columns profiled: {len(col_df)}")
    if "is_all_null" in col_df:
        all_null = col_df[col_df["is_all_null"] == True]  # noqa: E712
        constant = col_df[col_df["is_constant"] == True]   # noqa: E712
        uniq = col_df[col_df["is_unique_candidate"] == True]  # noqa: E712
        print(f"\nAll-null columns (likely dead)     : {len(all_null)}")
        for _, r in all_null.iterrows():
            print(f"    {r['table']}.{r['column']}")
        print(f"Constant columns (no information)  : {len(constant)}")
        for _, r in constant.iterrows():
            print(f"    {r['table']}.{r['column']}")
        print(f"Candidate-key columns (unique, no nulls): {len(uniq)}")
        for _, r in uniq.iterrows():
            print(f"    {r['table']}.{r['column']}")

    print(f"\nWrote {inv_path}\nWrote {col_path}")

    # --- optional top-values sweep ------------------------------------------
    if args.top_values and "ndistinct" in col_df:
        targets = col_df[(col_df["ndistinct"] >= 2)
                         & (col_df["ndistinct"] <= args.max_cardinality)]
        tv_rows = []
        print(f"\nDumping top values for {len(targets)} low-cardinality columns "
              f"(ndistinct <= {args.max_cardinality})...")
        for _, r in targets.iterrows():
            try:
                tv_rows += top_values(conn, r["schema"], r["table"], r["column"], args.top_n)
            except psycopg2.Error:
                pass
        if tv_rows:
            tv_path = os.path.join(args.out, "top_values.csv")
            pd.DataFrame(tv_rows).to_csv(tv_path, index=False)
            print(f"Wrote {tv_path}  "
                  f"(scan for -9 / 999 / 'N/A' / blanks — disguised missing codes)")

    # --- optional relationship discovery ------------------------------------
    if args.relationships:
        print("\nDiscovering relationships (declared + inferred)...")
        rel_df = discover_relationships(conn, schemas, col_df)
        if rel_df.empty:
            print("  No links found. (Need distinct counts on — don't combine with --no-distinct.)")
        else:
            rel_path = os.path.join(args.out, "relationships.csv")
            rel_df.to_csv(rel_path, index=False)
            for _, r in rel_df.iterrows():
                tag = "declared" if r["declared"] else "inferred"
                warn = f"  <-- {r['orphan_rows']} ORPHANS" if r["orphan_rows"] else ""
                print(f"    [{tag:8}] {r['child_table']}.{r['child_column']} -> "
                      f"{r['parent_table']}.{r['parent_column']}  "
                      f"({r['cardinality_guess']}){warn}")
            print(f"Wrote {rel_path}")

    conn.close()


if __name__ == "__main__":
    sys.exit(main())
