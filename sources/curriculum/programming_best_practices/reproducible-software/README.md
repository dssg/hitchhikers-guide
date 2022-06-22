# Making Projects Reproducible

Scientific software is often developed and used by a single person. It is all too common in academia
to be handed a postdoc or graduate student's old code and be unable to replicate the original study, run
the software outside of the original development machine, or even get the software to work at all. The
goal of this tutorial is to provide some guidelines to make your summer projects reproducible -- this means your
project can be installed on another computer and give the same results you got over the summer. At the end of
the summer, your project should be understandable and transferable to your future-self and anyone else who
may want to pick up where you left off without having to constantly email you about how to get your project
running.

*(Note: Your future-self doesn't have the luxury of being able to email your past-self).*

---

# What is a reproducible project?

One that...

- works for someone other than the original team
- can be **easily** installed on another computer
- has documentation that describes any dependencies and how to install them
- comes with enough tests to indicate the software is running properly

---

# README.md(rst)

All projects should have a README that communicates the following:

1. What the project is about
   - A short description of the project (i.e. the problem you are trying to solve).

2. The required dependencies to run the software
   - Can be in the form of a *requirements.txt* file for Python that lists
   the dependencies and version numbers.
   - The system-level dependencies.

3. Installation instructions
   - How to install your software and associated binaries. This can be in the form of
     instructions on how to use *pip*, *apt*, *yum*, or some other binary package
     manager.

4. Example usage
   - The inputs and outputs of your software (i.e. how to use it) with code examples.

5. Attribution/Licensing
   - Who did what and how others can use your software.

Examples:
   - [Chicago Food Inspections](https://github.com/Chicago/food-inspections-evaluation)
   - [DSSG Police EIS](https://github.com/dssg/police-eis)
   - [Linux Kernel](https://github.com/torvalds/linux)

---


# What to Do

- Use [virtual environments](#virtual-environments).
- [Use automation tools like Make or Drake](https://github.com/dssg/hitchhikers-guide/tree/master/tech-tutorials/reproducible_ETL)
- Keep your directory structure [intuitive, interpretable and easy to understand](#good-directory-organization).
- Keep your database free of "junk tables." Keep only what you need and what's current.
  - Junk tables will only confuse your future-self or others that come fresh to the project.
- Merge all branches into master.
  - Branches are for adding features or patches. When you have added said feature or patch
    and you know you won't break the master branch, merge into master and delete the branch.
- Write commit messages in such a way that your log is helpful (see [Git and Github tutorial](https://github.com/dssg/hitchhikers-guide/tree/master/tech-tutorials/git-and-github).)
- [Periodically make database backups](#backup-your-database).
- Write unit tests and use continuous integration so you can catch bugs quickly, particularly when you are merging
  new features into master. (See [testing tutorial](https://github.com/dssg/hitchhikers-guide/tree/master/tech-tutorials/test-test-test).)
- Document all of your functions with docstrings. (See [legible, good code tutorial](https://github.com/dssg/hitchhikers-guide/tree/master/tech-tutorials/legible-good-code).)
- Write your python code following the PEP8 standard. (See [legible, good code tutorial](https://github.com/dssg/hitchhikers-guide/tree/master/tech-tutorials/legible-good-code).)
- Use (4) spaces instead of tabs in your Python code for indentation.

---

# What NOT to Do

- Use [hard-coded paths](#hard-coded-paths).

- Require Sudo/root privileges to install your project.
  - You can't anticipate whether or not someone will have root access to the machine
    they are installing your project on, so don't count on it. Additionally, you shouldn't
    require users to create separate user names for your project.
- Use non-standard formats for inputs (stick to *YAML*, *XML*, *JSON*, *CLA*, etc).
  - My one exception to this rule is log files - which you should provide an example of in a README.
    Otherwise it is easier to just stick with what is already in use.
- Have a [messy repo with random files everywhere](#bad-directory-organization).
  - This is confusing, irritating and cancerous to productive enterprise.
- Commit data or sensitive information like database passcodes to the GitHub repo.
  - Your repository is for your codebase, not the data. Furthermore, your data may be sensitive
    and need to be protected.
  - Always assume that your repo will be public someday if you are hosting on GitHub (for your DSSG project it will be).
    Sensitive information also includes architecture decisions about your database. After sensitive
    information is pushed to GitHub, you cannot remove it completely from the repository.
- Have code that needs to be operationalized in Jupyter Notebooks.
  - Jupyter notebooks are wonderful for containing your analysis, code and figures in a single document,
    particularly for doing exploratory analysis. They are not good for keeping the code you will need for
    your pipeline or code that you will eventually want to turn into a library.

---

# Virtual Environments

A virtual environment solves the problem that projectX uses version 1.x of a package
while projectY uses version 2.x of a package by keeping dependencies in different
environments.

### Install a virtualenv
```
pip install --user virtualenv
virtualenv dssg-venv --no-site-packages #does not use any global packages
```
>You can also install a virtual environment and specify the type of python interpreter you
>would like to use using the -p option. This is good for keeping Python2 and Python3
>dependencies separate.
>
>Python2
>
>`virtualenv dssg-py2-venv -p $(which python) --no-site-packages`
>
>Python3
>
>`virtualenv dssg-py3-venv -p $(which python3) --no-site-packages`


### Activate a virtualenv
```
source ./dssg-venv/bin/activate
```

### Install Dependencies
```
pip install -r requirements.txt
```

### Freeze Dependencies
```
pip freeze > requirements.txt #outputs a list of dependencies and version numbers

```
> **Warning**: `pip freeze` will output every package that was installed using pip or setup.py (setuptools).
> External dependencies that are from github or some other source not found on PyPi will appear but will
> not be found when trying to reinstall the dependencies. You can include github repositories from github
> in your requirements.txt file, you just have to do manual housekeeping. Other external dependencies and how
> to install them should be recorded in your README.md file.

> Note: There is also the conda environment created by Continuum Analytics. The
> conda environment handles creating a environment and package dependencies -- what the virtual
> environment + pip combination does. Conda, unlike pip, includes many non-python dependencies
> (e.g, MKL) as precompiled binaries that are necessary for scientific python packages.
> The author is currently of the opinion that if you are a beginner or using a dated OS then using a
> conda environment is not the worst of ideas. If you are a developer working on a development
> machine then compile things yourself -- an important and useful skill. Whatever path you choose
> be consistent about how you set up your environment and document it thoroughly.

---

# Systems Level Dependencies

Systems level dependencies are the libraries installed on your OS. For Ubuntu/Debian Linux
you can get a list of them and then install them using the following:
```
#grab systems level dependencies
dpkg --get-selections > dependencies.txt
#reinstall on a new machine
dpkg --clear-selections
sudo dpkg --set-selections < dependencies.txt
```

Also courtesy of Tristan Crockett: installing a list of dependencies using apt
```
xargs -a <(awk '/^\s*[^#]/' dependencies.txt) -r -- sudo apt-get install

```


This will give every package installed on your OS. An easier alternative is to just keep track when you
install a new library and manually keep the list in a `dependencies.txt` file.

> There are also lightweight vitalization containers like Docker containers, Hyper-V images (Windows),
> or Ansible playbooks that can be used to "freeze" the systems level configuration of an OS.

---

# Backup Your Database

In PostGreSQL when a table is dropped, it is gone forever. You don't want to drop your results
table on the last day of the fellowship, so it is a good idea to backup periodically.

To dump your database in PostGreSQL:

```
pg_dump -Fc --schema='raw|clean|models' -N '*public*' --no-acl -v -h <hostname> -U <dbuser> <dbname> > dssg-$(date +%F).dump
```
*Note: This can be automated with a crontab script.*

To restore your database from a dump:
```
< dump_file psql -U dbuser -h dbhost dbname
```
---

# Hard-coded Paths

## Example of Adding Shapefile with hard-coded paths

Hard-coded paths are absolute paths that are native to the machine you are using for
development. It is unlikely someone else will keep their data in the exact same directory
as you when trying to use your project in a separate environment. Users should be able to set
location of files as command line parameters. Below are examples.

### load_shapefile_hardpath_v1.sh
```
# Data downloaded from this website: http://mrdata.usgs.gov/geology/state/state.php?state=NY
shp2pgsql -d -s 4267:2261 -d /mnt/data/syracuse/NY_geol_dd soil.geology | psql

```
Although this script documents the command that runs, it has a hard path and the purpose of the arguments
are not clear. This script has the shelf-life of a banana.

### load_shapefile_hardpath_v2.sh
```
#!/bin/bash
# Data downloaded from this website: http://mrdata.usgs.gov/geology/state/state.php?state=NY
original_projection=4267
new_projection=2261 #projection of Upstate NY
schema='soil'
table='geology'
shapefile='/mnt/data/syracuse/NY_geol_dd/nygeol_poly_dd.shp'

#create table and schema
psql -c "drop table if exists ${schema}.${table}"
psql -c "create schema if not exists ${schema}"
#import the data
shp2pgsql -d -s ${original_projection}:${new_projection} -d ${shapefile} ${schema}.${table} | psql

```
With this version someone can better surmise what is being done. Every time you want to load
your data you have to change the filename in the script. It also checks if the table already exists
in the database so the command can be used to reload data.

### load_shapefile_hardpath_v3.sh
```
#!/bin/bash
#ETL script for importing shape files.

PROGRAM=$(basename $0)
usage="${PROGRAM} -s schema -t table -p original_projection [-n new_projection] [-v] shapefilename"

function die() {
local errmsg="$1" errcode="${2:-1}"
echo "ERROR: ${errmsg}"
exit ${errcode}
}

#if called with no command line arguments then output usage
if [ ${#} -eq 0 ]
then
    echo ${usage}
    exit 1;
fi

#--------------------------------------------------
# process input arguments
#--------------------------------------------------
verbose="false"
new_projection=""
while getopts hp:n:s:t:v OPT; do
case "${OPT}" in
h)  echo "${usage}";
exit 0
;;
p)  original_projection="${OPTARG}"
;;
n)  new_projection="${OPTARG}"
;;
s)  schema="${OPTARG}"
;;
t)  table="${OPTARG}"
;;
v)  verbose="true"
;;
?)  die "unknown option or missing argument; see -h for usage" 2
;;
esac
done
shift $((OPTIND - 1))
shapefile="$*"

if [ ${verbose} == "true" ]
then
    echo 'original_projection:' $original_projection
    echo 'new_projection:' $new_projection
    echo 'schema:' $schema
    echo 'table:'$table
    echo 'shapefile:'$shapefile
fi


#create table and schema
psql -c "drop table if exists ${schema}.${table}"
psql -c "create schema if not exists ${schema}"

#import the data
if [ -z "${new_projection}" ]
then
    shp2pgsql -s ${original_projection} -d ${shapefile} ${schema}.${table} | psql
else
    shp2pgsql -s ${original_projection}:${new_projection} -d ${shapefile} ${schema}.${table} | psql
fi

```
In this version, you can call the script from the command line and use it for any shapefile. When
called with no arguments it prints out a usage so the user does not have to look into the actual
script. It also has a verbose mode for debugging. Here, there are no hard paths.

# Bad Directory Organization
```
nfp2/
├── 10_month_to_12_month_ISOMAP_final_asq_psocial_2r_and_time4_DURATION_time_MATERNAL_sum_and_time4_DURATION_sum_and_final_asq_comm_2r_and_final_asq_psolve_2r.png
├── 10_month_to_12_month_ISOMAP_final_asq_psocial_2r_and_time4_DURATION_time_MATERNAL_sum_and_time4_DURATION_sum_and_final_asq_comm_2r_and_time4_cumulative_DURATION_time_MATERNAL_sum.png
├── 10_month_to_12_month_ISOMAP_final_asq_psocial_2r_and_time4_DURATION_time_MATERNAL_sum_and_time4_DURATION_sum_and_final_asq_comm_2r_and_whptile1.png
├── 10_month_to_12_month_LLE_final_asq_psocial_2r_and_time4_DURATION_time_MATERNAL_sum_and_time4_DURATION_sum_and_final_asq_comm_2r_and_final_asq_psolve_2r.png
├── 10_month_to_12_month_LLE_final_asq_psocial_2r_and_time4_DURATION_time_MATERNAL_sum_and_time4_DURATION_sum_and_final_asq_comm_2r_and_time4_cumulative_DURATION_time_MATERNAL_sum.png
├── 10_month_to_12_month_LLE_final_asq_psocial_2r_and_time4_DURATION_time_MATERNAL_sum_and_time4_DURATION_sum_and_final_asq_comm_2r_and_whptile1.png
├── 12_month_to_14_month_ISOMAP_momwtgain_and_birthgms2_and_time4_DURATION_sum_and_PREPGBMI_and_time4_DURATION_time_MATERNAL_sum.png
├── 12_month_to_14_month_ISOMAP_momwtgain_and_birthgms2_and_time4_DURATION_sum_and_PREPGBMI_and_whptile2.png
├── 12_month_to_14_month_ISOMAP_momwtgain_and_birthgms2_and_time4_DURATION_sum_and_time5_cumulative_DURATION_sum_and_whptile2.png
├── 12_month_to_14_month_ISOMAP_momwtgain_and_birthgms2_and_time4_DURATION_sum_and_time5_DURATION_sum_and_time4_DURATION_time_MATERNAL_sum.png
├── 12_month_to_14_month_LLE_momwtgain_and_birthgms2_and_time4_DURATION_sum_and_PREPGBMI_and_time4_DURATION_time_MATERNAL_sum.png
├── 12_month_to_14_month_LLE_momwtgain_and_birthgms2_and_time4_DURATION_sum_and_PREPGBMI_and_whptile2.png
├── 12_month_to_14_month_LLE_momwtgain_and_birthgms2_and_time4_DURATION_sum_and_time5_cumulative_DURATION_sum_and_whptile2.png
├── 12_month_to_14_month_LLE_momwtgain_and_birthgms2_and_time4_DURATION_sum_and_time5_DURATION_sum_and_time4_DURATION_time_MATERNAL_sum.png
├── 4_month_to_6_month_ISOMAP_final_asq_fmotor_1r_and_final_asq_psocial_1r_and_final_asq_gmotor_1r_and_final_asq_comm_1r_and_final_asq_psolve_1r.png
├── 4_month_to_6_month_ISOMAP_final_asq_fmotor_1r_and_final_asq_psocial_1r_and_final_asq_gmotor_1r_and_final_asq_comm_1r_and_time2_DURATION_sum.png
├── 4_month_to_6_month_LLE_final_asq_fmotor_1r_and_final_asq_psocial_1r_and_final_asq_gmotor_1r_and_final_asq_comm_1r_and_final_asq_psolve_1r.png
├── 4_month_to_6_month_LLE_final_asq_fmotor_1r_and_final_asq_psocial_1r_and_final_asq_gmotor_1r_and_final_asq_comm_1r_and_time2_DURATION_sum.png
├── 6_month_to_10_month_ISOMAP_whptile1_and_time3_DURATION_time_MATERNAL_sum_and_birthgms2_and_momwtgain_and_time3_cumulative_DURATION_sum.png
├── 6_month_to_10_month_ISOMAP_whptile1_and_time3_DURATION_time_MATERNAL_sum_and_time2_DURATION_sum_and_time3_cumulative_DURATION_sum_and_MomsAgeBirth_and_time3_cumulative_DURATION_time_MATERNAL_sum.png
├── 6_month_to_10_month_ISOMAP_whptile1_and_time3_DURATION_time_MATERNAL_sum_and_time2_DURATION_sum_and_time3_cumulative_DURATION_sum_and_momwtgain.png
├── 6_month_to_10_month_ISOMAP_whptile1_and_time3_DURATION_time_MATERNAL_sum_and_time2_DURATION_sum_and_time3_DURATION_sum_and_time3_cumulative_DURATION_time_MATERNAL_sum.png
├── 6_month_to_10_month_LLE_whptile1_and_time3_DURATION_time_MATERNAL_sum_and_birthgms2_and_momwtgain_and_time3_cumulative_DURATION_sum.png
├── 6_month_to_10_month_LLE_whptile1_and_time3_DURATION_time_MATERNAL_sum_and_time2_DURATION_sum_and_time3_cumulative_DURATION_sum_and_MomsAgeBirth_and_time3_cumulative_DURATION_time_MATERNAL_sum.png
├── 6_month_to_10_month_LLE_whptile1_and_time3_DURATION_time_MATERNAL_sum_and_time2_DURATION_sum_and_time3_cumulative_DURATION_sum_and_momwtgain.png
├── 6_month_to_10_month_LLE_whptile1_and_time3_DURATION_time_MATERNAL_sum_and_time2_DURATION_sum_and_time3_DURATION_sum_and_time3_cumulative_DURATION_time_MATERNAL_sum.png
├── ada_all.yaml
├── ada_simple_SAMMER.yaml
├── Add_null_data.ipynb
├── Add_null_data.py
├── all.yaml
├── assemble_long_data.ipynb
├── binary_classifer.py
├── birth_to_4_month_ISOMAP_MomsAgeBirth_and_time1_DURATION_time_PERSHLTH_std_and_time1_DURATION_sum_and_momwtgain_and_birthgms2.png
├── birth_to_4_month_ISOMAP_MomsAgeBirth_and_time1_DURATION_time_PERSHLTH_std_and_time1_DURATION_sum_and_time1_DURATION_time_MATERNAL_sum_and_time1_DURATION_time_PERSHLTH_sum.png
├── birth_to_4_month_LLE_MomsAgeBirth_and_time1_DURATION_time_PERSHLTH_std_and_time1_DURATION_sum_and_momwtgain_and_birthgms2.png
├── birth_to_4_month_LLE_MomsAgeBirth_and_time1_DURATION_time_PERSHLTH_std_and_time1_DURATION_sum_and_time1_DURATION_time_MATERNAL_sum_and_time1_DURATION_time_PERSHLTH_sum.png
├── BRL_file_generation.ipynb
├── #BRL.py#
├── BRL.py
├── classification.ipynb
├── classifier_t1-Copy0.ipynb
├── classifier_t1-Copy0.py
├── classifier_t1.ipynb
├── classifier_t3.py
├── clique_feature_coprus.p
├── Clique_Features.ipynb
├── #Clique_Features.py#
├── Clique_Features.py
├── Clustering_Scoring.ipynb
├── cohort_creation.py
├── convert_nfp_sas_to_csv.R
├── corpus.ipynb
├── create_dropout_files.py
├── cross_val_copy.py
├── cross_val.ipynb
├── cross_val.py
├── dal_test.ipynb
├── data_cleaning.ipynb
├── data_cleaning.py
├── data_creation_1.yaml
├── data_creation_2.yaml
├── data_creation_3.yaml
├── data_creation_4.yaml
├── data_creation_and_model_applicaition.py
├── data_creation_and_model_application_1.yaml
├── data_creation_and_model_application_2.yaml
├── data_creation_and_model_application_3.yaml
├── data_creation_and_model_application_4.yaml
├── data_creation_and_model_application.yaml
├── data_creation_for_dropout.py
├── data_creation.yaml
├── dataframe.py
├── datasets.flowingdata.com
├── data_visualization
├── data_wrangling
├── decision_tree.yaml
├── dropout
├── dropout_explore.ipynb
├── experiment.log
├── Feature_graph_for_interval_with_top_2_features_for_interval_10_month_to_12_month.dot
├── Feature_graph_for_interval_with_top_2_features_for_interval_12_month_to_14_month.dot
├── Feature_graph_for_interval_with_top_2_features_for_interval_14_month_to_18_month.dot
├── Feature_graph_for_interval_with_top_2_features_for_interval_18_month_20_month.dot
├── Feature_graph_for_interval_with_top_2_features_for_interval_18_month_to_20_month.dot
├── Feature_graph_for_interval_with_top_2_features_for_interval_4_month_to_6_month.dot
├── Feature_graph_for_interval_with_top_2_features_for_interval_6_month_to_10_month.dot
├── Feature_graph_for_interval_with_top_2_features_for_interval_birth_to_4_month.dot
├── Feature_graph_for_interval_with_top_2_features_for_interval_intake_to_birth.dot
├── Feature Importance.ipynb
├── find_model.ipynb
├── find_model.py
├── #.gitignore#
├── graph
├── graph_code.py
├── Histrogram_Feature_Creation.ipynb
├── how_to_merge.txt
├── Imputation.ipynb
├── Imputation.py
├── impute
├── impute_and_filter-Copy0.ipynb
├── impute_and_filter-Copy1.ipynb
├── impute_and_filter.ipynb
├── impute_and_filter.py
├── intake_to_birth_ISOMAP_CLIENT_HEALTH_PREGNANCY_0_WKS_PR_and_CLIENT_HEALTH_GENERAL_HEIGHT_1_I_and_PREPGBMI_and_PREPGKG_and_CLIENT_HEALTH_GENERAL_WEIGHT_0_P.png
├── intake_to_birth_ISOMAP_CLIENT_HEALTH_PREGNANCY_0_WKS_PR_and_CLIENT_HEALTH_GENERAL_HEIGHT_1_I_and_PREPGBMI_and_PREPGKG_and_NURSE_0_YEAR_NURSING_EXPERIENCE.png
├── intake_to_birth_LLE_CLIENT_HEALTH_PREGNANCY_0_WKS_PR_and_CLIENT_HEALTH_GENERAL_HEIGHT_1_I_and_PREPGBMI_and_PREPGKG_and_CLIENT_HEALTH_GENERAL_WEIGHT_0_P.png
├── intake_to_birth_LLE_CLIENT_HEALTH_PREGNANCY_0_WKS_PR_and_CLIENT_HEALTH_GENERAL_HEIGHT_1_I_and_PREPGBMI_and_PREPGKG_and_NURSE_0_YEAR_NURSING_EXPERIENCE.png
├── I_S_O_M_A_P_ _m_o_m_w_t_g_a_i_n___a_n_d___b_i_r_t_h_g_m_s_2___a_n_d___t_i_m_e_4___D_U_R_A_T_I_O_N___s_u_m___a_n_d___P_R_E_P_G_B_M_I___a_n_d___t_i_m_e_4___D_U_R_A_T_I_O_N___t_i_m_e___M_A_T_E_R_N_A_L___s_u_m.png
├── Jeff_Models-Copy0.ipynb
├── Jeff_recipe.txt
├── #KMS.txt#
├── KMS.txt
├── legend.html
├── load_data.py
├── media
├── merge.py
├── meta_data
├── metr
├── metrics_r_f_d.p
├── metrics_will_drop.p
├── model_pipeline_2-Copy0.ipynb
├── model_pipeline_2.ipynb
├── model_pipeline_2.py
├── model_pipeline_3.py
├── #model_pipeline_5.py#
├── model_pipeline_5.py
├── model_run_rf.txt
├── models
├── model_without_pca.yaml
├── model_with_pca.yaml
├── model.yaml
├── name_change.pl
├── nbstripout
├── N_Features.ipynb
├── nfp2-public
├── nfpt2.tree
├── notes
├── out
├── out.txt
├── paralllel_coordinates.ipynb
├── pickle_files
├── pipeline
├── pipeline_demo1.py
├── PipeLine_Phase1.ipynb
├── PipeLine_Phase1.py
├── pipeline_utilities.py
├── plot_binary.py
├── plot.yaml
├── Precision-Recall_curve_across_all_intervals.png
├── prediction_set_maker-Copy0.ipynb
├── prediction_set_maker-Copy1.ipynb
├── prediction_set_maker_for_dropout.ipynb
├── prediction_set_maker.ipynb
├── prediction_set_maker.py
├── Prep for R.ipynb
├── project-pipeline.dia
├── pyensemble
├── #pyliny_report.txt#
├── pyliny_report.txt
├── python_to_nb.py
├── Rafael_weeks.ipynb
├── RandomForestClassifier_on_interval_1.png
├── RandomForestClassifier_on_interval_2.png
├── RandomForestClassifier_on_interval_3.png
├── RandomForestClassifier_on_interval_4.png
├── RandomForestClassifier_on_interval_5.png
├── RandomForestClassifier_on_interval_6.png
├── R_code
├── README.md
├── Receiver_operating_characteristic_curve_across_all_intervals.png
├── results_pipeline2-Copy0.ipynb
├── results_pipeline2.html
├── results_pipeline2.ipynb
├── results_pipeline2.py
├── roc_auc_score_across_all_intervals.png
├── rollin_visit.ipynb
├── run.sh
├── run_sklearn_model.py
├── run_some_pipelines.sh
├── run_weka.pl
├── sanity_check_pipeline.ipynb
├── sanity_check_Rafael_pipeline.ipynb
├── sarah_a.ipynb
├── Secondary_feature_gen.ipynb
├── Secondary_feature_gen-Rafael-Copy0.ipynb
├── Secondary_feature_gen-Rafael.ipynb
├── Secondary_feature_gen-Rafael.py
├── secondary_features.ipynb
├── secondary_features_on_visit_data.ipynb
├── see_test_model_results.ipynb
├── sklearn_DT.yaml
├── sklearn.yaml
├── sklearn.yaml_bk
├── Slicer-Copy0.ipynb
├── Slicer.ipynb
├── summary_statistics.ipynb
├── temporal_data_creation_bk.ipynb
├── temporal_data_creation.ipynb
├── temporal_data_creation.py
├── test.d
├── testing_fiber_2_split.p
├── test_model.ipynb
├── test.py
├── time_based_cross_validation-Rafael.ipynb
├── time_cv_impute.ipynb
├── timeline_creation_driver.py
├── Timeline_Help.ipynb
├── tree.dot
├── tr_te_to_head.py
├── Untitled0.ipynb
├── Untitled1.ipynb
├── Untitled2.ipynb
├── Untitled3.ipynb
├── Untitled4.ipynb
├── Untitled5.ipynb
├── Untitled6.ipynb
├── Untitled7.ipynb
├── utils
├── Weka.ipynb
├── weka_to_pr_jeff.py
├── weka_to_pr_raf.py
├── weka_to_roc.py
└── weka_to_roc_time.py

```

---

# Good Directory Organization

```
.
├── config
├── descriptive_stats
│   ├── mains_streets_stats
│   └── water_work_orders
├── etl
│   ├── bin
│   ├── geology
│   ├── road_ratings
│   ├── soil
│   ├── street_line_data
│   ├── tax_data
│   ├── updated_main_data
│   ├── waterorders
│   └── water_system
├── model
│   ├── config
│   ├── features
│   └── log
├── models_evaluation
└── results
    └── figures

```




# Additional Resources/Inspiration for this Tutorial

- [10 Rules for Robust Software](http://oicr-gsi.github.io/robust-paper/#fn:2)
- [Good Enough Practices in Scientific Computing](https://arxiv.org/pdf/1609.00037.pdf)
- [Best Practices for Scientific Computing](http://journals.plos.org/plosbiology/article?id=10.1371%2Fjournal.pbio.1001745 )
- [Reproducible Research SSI](https://www.software.ac.uk/attach/ChangingResearchSoftwareAttitudes.pdf)
