# Python

We will need to import the virtual environment in which we are working to jupyter, so that we work with the same packages -and versions of those- within jupyter. To do that, go to `/mnt/data/projects/food_inspections/` and type the following command:

```
$ python -m ipykernel install --user --name=food_inspections --display-name food_inspections
```

Also, since we are going to connect to the database through Python we will need to chage some environment variables.

```
$ nano ~/.bashrc
```

Add your credentials for the variables: `PGUSER`, `PGPASSWORD`, `PGHOST`, `PGPORT`, and `PGDATABASE`. For example:

```
export PGUSER='yourandrewid'
export PGPASSWORD='yourandrewid'
export PGHOST='db.dssg.io'
export PGPORT=5432
export PGDATABASE='food-inspections'
```

Then make these variables available to the session:

```
$ source ~/.bashrc
```


Start a Jupyter notebook, remember to use a port available from the list `ss -tulnp`:

```
$ jupyter notebook --port {XXXX}
```

Make a port forwarding between your local machine and the server so that we can use the browser in your machine as GUI.

```
$ ssh localhost:{YYYY}:localhost:{XXXX} andrewid@training.dssg.io
```

Open your browser and open the URL `localhost:{YYYY}` it will ask for a token.

[Let's code!](./python_sql_pandas_viz.ipynb)

