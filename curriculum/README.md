# Data Science for Social Good Curriculum

## [Before You Start](0_before_you_start/)
So you want to start a DSSG project! First, please make sure you have gone through the [Prerequisites](0_before_you_start/prerequisites/) and [Software Setup](0_before_you_start/software-setup/) and are equipped 
with the basic knowledge and tools you'll need. Then use our 
[Project Scoping Intro](https://dssg.uchicago.edu/2016/10/27/scoping-data-science-for-social-good-projects/)
to help you decide on a project, or refine a project you already have in mind. 
Next, check out [Pipelines and Project Workflow](0_before_you_start/pipelines-and-project-workflow/) for an
overview of how the steps of your project (and, therefore, your code) will be organized.

## [Getting and Keeping Data](1_getting_and_keeping_data/)
Data comes in many forms, from many sources - you may get a database dump or 
[CSV files directly from a project partner](1_getting_and_keeping_data/csv-to-db/), or you may need to 
[scrape data from the web](1_getting_and_keeping_data/basic-web-scraping/). Either way,
once you've got your hands on some data, you'll need to bring it into a [database](1_getting_and_keeping_data/databases/),
and start cleaning and "wrangling" it. You'll definitely want to keep track of the steps to take your data from its 
original, raw form to being model-ready, so check out [Reproducible ETL](1_getting_and_keeping_data/reproducible-ETL/).
[Command line tools](1_getting_and_keeping_data/command-line-tools/) will start to come in handy here. 
Finally, data science for social good projects often involve sensitive data about real humans, which is what makes this 
work both interesting and important, but also makes it extra important to keep security in mind, so make sure to check 
out the [Data Security Primer](1_getting_and_keeping_data/data-security-primer/).

## [Data Exploration and Analysis](2_data_exploration_and_analysis/)
Once you've got some data, you're going to be eager to dig into it! Our tool of choice for data analysis is Python. Start off 
with [Intro to Git and Python](2_data_exploration_and_analysis/intro-to-git-and-python/), then move onto 
[Data Exploration in Python](2_data_exploration_and_analysis/data-exploration-in-python/). 
If you're combining data from multiple sources, you'll have to do 
[record linkage](2_data_exploration_and_analysis/record-linkage/) to match entities across datasets. Depending on your
particular project, you may need special methods and tools; at this time, we have resources 
for working with [text data](2_data_exploration_and_analysis/text-analysis/), [spatial data](2_data_exploration_and_analysis/postgis-workshop/) and [network data](2_data_exploration_and_analysis/network-analysis/).

## [Modeling and Machine Learning](3_modeling_and_machine_learning/)
Now you're ready to make some models! Most of the modeling techniques you'll use, whether supervised or unsupervised,
will fall under the umbrella of [machine learning](3_modeling_and_machine_learning/machine-learning/), but that's 
not all you need to know. Knowing some social science will go a long way when it comes to formulating models 
appropriately, designing experiments to evaluate model performance, and understanding what conclusions you can make 
based on your results. [Quantitative Social Science](3_modeling_and_machine_learning/quantitative-social-science/) and 
[Causal Inference with Observational Data](3_modeling_and_machine_learning/causal-inference/) will help you think these questions through. 

## [Programming Best Practices](4_programming_best_practices/)
As you begin to work on larger, more complicated projects, and work in teams with other programmers, you'll save yourself
and your teammates a lot of grief and frustration by writing [legible, good code](4_programming_best_practices/legible-good-code/) 
and [writing tests](4_programming_best_practices/test-test-test/). You'll also need to document and package up your work 
so that other people can understand and reproduce your results, so check out the 
[reproducible software](4_programming_best_practices/reproducible-software/) tutorial. As you continue to develop these
skills, you'll start to change settings and configurations for various applications, so check out 
[pimp my dotfiles](4_programming_best_practices/pimp-my-dotfiles/) for some tips on how to customize the environments 
you're working in.

## [Presentations and Communications](5_presentations_and_communications/)
Remember that there's no point to doing data science for social good work if no one understands 
what you did and can put it to good use. You'll need to be able to communicate your work:
[Data Visualization](https://github.com/jonkeane/data-visualization-intro) and [Presentation Skills](5_presentations_and_communications/presentation-skills/) will help with that, whether you're communicating your work to a public audience or to stakeholders. When you're
working directly with a project partner and are creating tools for them to use, keep
[Usability and User Interfaces](5_presentations_and_communications/usability-and-user-interfaces/) in mind to make sure that 
whatever tools you create will be useful and usable.

# How to Contribute
We welcome contributions and collaboration! 
If you find a broken link, or have a request or suggestion, please submit an issue. 
If you have materials to contribute, please submit a pull request. New tutorials should follow our [tutorial template](tutorial-template/). 
