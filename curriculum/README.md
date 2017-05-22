# Data Science for Social Good Curriculum

## [Getting Started](0_before_you_start/)
So you want to start a DSSG project! First, please make sure you have gone through the [Prerequisites](0_before_you_start/prerequisites/)
and [Software Setup](0_before_you_start/software-setup/) and are equipped with the basic knowledge and tools you'll need.
Then use our [Project Scoping Intro](https://dssg.uchicago.edu/2016/10/27/scoping-data-science-for-social-good-projects/)
to help you decide on a project or refine a project you already have in mind. 
Then, check out [Pipelines and Project Workflow](0_before_you_start/pipelines-and-project-workflow/) for an
overview of how the steps of your project (and, therefore, your code) will be organized.

## [Getting and Keeping Data](1_getting_and_keeping_data/)
Data comes in many forms, from many sources - you may get a database dump or 
[CSV files directly from a project partner](2_getting_and_keeping_data/csv-to-db/), or you may need to 
[scrape data from the web](2_getting_and_keeping_data/basic-web-scraping/). Either way,
once you've got your hands on some data, you'll need to bring it into a [database](2_getting_and_keeping_data/databases/),
and start cleaning and "wrangling" it. You'll definitely want to keep track of the steps to take your data from its 
original, raw form to being model-ready, so check out [Reproducible ETL](2_getting_and_keeping_data/reproducible-ETL/).
[Command Line Tools](2_getting_and_keeping_data/command-line-tools/) will start to come in handy here. 
Finally, data science for social good projects often involve sensitive data about real humans, which is what makes this 
work both interesting and important, but also makes it extra important to keep security in mind, so make sure to check 
out the [Data Security Primer](2_getting_and_keeping_data/data-security-primer/).

## Data Exploration and Analysis
Now you're ready to start digging into the data! Before you start, check out our [Intro to Git and Python](intro-to-git-and-python/), then move onto [Data Exploration in Python](data-exploration-in-python/).
If you need to link data from multiple sources, [Record Linkage](record-linkage/) will be useful here.
By now you'll also want to be using [Git and Github](git-and-github/) to keep track of the progress of your project,
and to work with collaborators and teammates. Some types of data require special methods and tools; we have resources
for text data ([Natural Language Processing](text-analysis/)), spatial data ([PostGIS Workshop](postgis-workshop/))
and network data ([Network Analysis](network/)).

## Modeling and Machine Learning
Now you're ready to make some models! Check out the [machine learning](machine-learning/) section. As your models
produce results, it's important to provide context and interpretations for the results of said models;
[Quantitative Social Science](quantitative-social-science/) and [Causal Inference with Observational Data](causal-inference/)
will help you think through what conclusions you can make from your analysis. As you start to write more
production code, check out [Legible, Good Code](legible-good-code/), [Test, Test, Test](test-test-test/)
and [Reproducible Software](reproducible-software/) to learn how to keep your code base in tip-top shape.

## Social Science 

## Programming Best Practices 

## Communications and Project Management
Remember that there's no point to doing data science for social good work if you don't have some audience
that can understand it and put your insights to good use. You'll need to be able to communicate your work:
[Data Visualization](https://github.com/jonkeane/data-visualization-intro) and [Presentation Skills](presentation-skills/) will help with that, both when communicating your work to a public audience, and to stakeholders. When you're
working directly with a project partner and are creating tools for them to use, keep
[Usability and User Interfaces](usability-and-user-interfaces/) in mind.


# How to Contribute
We welcome contributions and collaboration! 
If you find a broken link, or have a request or suggestion, please submit an issue. 
If you have materials to contribute, please submit a pull request. New tutorials should follow our [tutorial template](tutorial-template/). 
