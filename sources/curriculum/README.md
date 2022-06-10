## Before You Start
So you want to start a DSSG project! First, please make sure you have
gone through the [Prerequisites](setup/software-setup/README.md) and are
equipped
with the basic knowledge and tools you'll need. Then use our
[Project Scoping Intro](https://dsapp.uchicago.edu/home/resources/data-science-project-scoping-guide/)
to help you decide on a project, or refine a project you already have in mind.
Next, check out [Pipelines and Project Workflow](0_before_you_start/pipelines-and-project-workflow/) for an
overview of how the steps of your project (and, therefore, your code) will be organized.

## Getting, Keeping, and Linking Data
Data comes in many forms, from many sources - you may get a database dump or
[CSV files directly from a project partner](1_getting_and_keeping_data/csv-to-db/), or you may need to
[scrape data from the web](1_getting_and_keeping_data/basic-web-scraping/). Either way,
once you've got your hands on some data, you'll need to bring it into a [database](1_getting_and_keeping_data/databases/),
and start cleaning and "wrangling" it. You'll definitely want to keep track of the steps to take your data from its
original, raw form to being model-ready, so check out [Reproducible ETL](1_getting_and_keeping_data/reproducible_ETL/).
[Command line tools](1_getting_and_keeping_data/command-line-tools/) will start to come in handy here.
Finally, data science for social good projects often involve sensitive data about real humans, which is what makes this
work both interesting and important, but also makes it extra important to keep security in mind, so make sure to check
out the [Data Security Primer](get_data/data-security-primer/).

## Data Exploration and Analysis
Once you've got some data, you're going to be eager to dig into it! Our tool of choice for data analysis is Python. Start off
with [Intro to Git](setup/git-and-github) and [Python](software/basic_python/), then move onto
[Data Exploration in Python](2_data_exploration_and_analysis/data-exploration-in-python/).
If you're combining data from multiple sources, you'll have to do
[record linkage](2_data_exploration_and_analysis/record-linkage/) to match entities across datasets. Depending on your
particular project, you may need special methods and tools; at this time, we have resources
for working with [text
data](2_data_exploration_and_analysis/text-analysis/), [spatial
data](2_data_exploration_and_analysis/gis_analysis/) and [network
data](2_data_exploration_and_analysis/network-analysis/).

## Analytical Formulation and Baselines
Distinct from the initial scoping, a true analytical formulation of your problem can only come after you have developed an understanding of the data at hand, which in turn will often result in a greater understanding of the problem itself. Here, you’ll ask how specifically your target variable (if relevant) is defined in the data, what types of information are available as predictors, and what baseline you’ll be measure performance against. Very rarely is the appropriate baseline as simple as "random choice" or the population prevalence. Rather, it should reflect what would be expected to happen otherwise: perhaps a simple decision rule that an expert would come up with or even a pre-existing statistical model that the current effort is seeking to replace.

## Modeling and Machine Learning
Now you're ready to make some models! Most of the modeling techniques you'll use, whether supervised or unsupervised,
will fall under the umbrella of [machine learning](3_modeling_and_machine_learning/machine-learning/), but that's
not all you need to know. Knowing some social science will go a long way when it comes to formulating models
appropriately, designing experiments to evaluate model performance, and understanding what conclusions you can make
based on your results. [Quantitative Social Science](3_modeling_and_machine_learning/quantitative-social-science/) and
[Causal Inference with Observational Data](3_modeling_and_machine_learning/causal-inference/) will help you think these questions through.

## Programming Best Practices
As you begin to work on larger, more complicated projects, and work in teams with other programmers, you'll save yourself
and your teammates a lot of grief and frustration by writing [legible, good code](4_programming_best_practices/legible-good-code/)
and [writing tests](4_programming_best_practices/test-test-test/). You'll also need to document and package up your work
so that other people can understand and reproduce your results, so check out the
[reproducible software](4_programming_best_practices/reproducible-software/) tutorial. As you continue to develop these
skills, you'll start to change settings and configurations for various applications, so check out
[pimp my dotfiles](4_programming_best_practices/pimp-my-dotfiles/) for some tips on how to customize the environments
you're working in.

## Presentations and Communications
Remember that there's no point to doing data science for social good work if no one understands
what you did and can put it to good use. You'll need to be able to communicate your work:
[Data Visualization](https://github.com/jonkeane/data-visualization-intro) and [Presentation Skills](5_presentations_and_communications/presentation-skills/) will help with that, whether you're communicating your work to a public audience or to stakeholders. When you're
working directly with a project partner and are creating tools for them to use, keep
[Usability and User Interfaces](5_presentations_and_communications/usability-and-user-interfaces/) in mind to make sure that
whatever tools you create will be useful and usable.

# How to Contribute
We welcome contributions and collaboration!
If you find a broken link, or have a request or suggestion, please submit an issue.
If you have materials to contribute, please submit a pull request. New tutorials should follow our [tutorial template](tutorial-template/), and keep in mind the teaching philosophy outlined below.

## Teaching Philosophy
Our guiding teaching philosophy is as follows:
- *You get out what you put in.* Fellows are encouraged to take an active role in teaching and shaping the curriculum,
as well as learning from it. Learning also takes initiative and participation on the student side.
- *Clearly motivate topics and tools.* For more technical topics: what actual task that a data scientist does will require
this tool? What other options are there to do similar tasks? What are pitfalls, and what will it look like when something
goes wrong? What are common mistakes or bugs? For conceptual topics: Why do we feel the need to communicate this topic?
What are some concrete examples of where it's been done well or poorly in the past?
- *Lessons should be user friendly.* Lectures should be concise - 45 minutes at the outside - and materials should be
practical. Slides should be accompanied by a worksheet or exercises so fellows can follow along and learn by doing,
and a cheat sheet with relevant commands or code snippets should be included where possible.
