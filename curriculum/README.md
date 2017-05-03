# Data Science for Social Good Curriculum

When you first start a project, first make sure you have gone through the [Prerequisites](prerequisites/)
and [Software Setup](software-setup/) and are equipped with the basic knowledge and tools you'll need.
Then, you need to get some data (see [Legal and Data Use Agreements](https://dsapp.uchicago.edu/resources/legal-agreements/))
and decide on a good project to use the data for - look at our
[Project Scoping Intro](https://dssg.uchicago.edu/2016/10/27/scoping-data-science-for-social-good-projects/)
for a primer, then check out [Pipelines and Project Workflow](pipelines-and-project-workflow/) for an
overview of how the steps of your project (and, therefore, your code) will be organized.

Data comes in many forms, and from many sources - you may get a database dump directly from the source,
or you may need to scrape data from the web (see [Basic Web Scraping](basic-web-scraping/)). Either way,
once you've got your hands on data, you'll need to bring it into a database (see [Databases](databases/)),
and start formatting it in such a way that you can use it for analysis, and you want to keep track of what
steps you took to go from raw data to model-ready data ([Reproducible ETL](reproducible-ETL/)).
[Command Line Tools](command-line-tools/) will start to come in handy here.
Often data science for social good projects will involve sensitive data, so be aware that you're keeping
it safe: [Data Security Primer](data-security-primer/).

Now you're ready to start digging into the data! Before you start, check out our [Intro to Git and Python](intro-to-git-and-python/), then move onto [Data Exploration in Python](data-exploration-in-python/).
If you need to link data from multiple sources, [Record Linkage](record-linkage/) will be useful here.
By now you'll also want to be using [Git and Github](git-and-github/) to keep track of the progress of your project,
and to work with collaborators and teammates. Some types of data require special methods and tools; we have resources
for text data ([Natural Language Processing](text-analysis/)), spatial data ([PostGIS Workshop](postgis-workshop/))
and network data ([Network Analysis](network/)).

Now you're ready to make some models! Check out the [machine learning](machine-learning/) section. As your models
produce results, it's important to provide context and interpretations for the results of said models;
[Quantitative Social Science](quantitative-social-science/) and [Causal Inference with Observational Data](causal-inference/)
will help you think through what conclusions you can make from your analysis. As you start to write more
production code, check out [Legible, Good Code](legible-good-code/), [Test, Test, Test](test-test-test/)
and [Reproducible Software](reproducible-software/) to learn how to keep your code base in tip-top shape.

Remember that there's no point to doing data science for social good work if you don't have some audience
that can understand it and put your insights to good use. You'll need to be able to communicate your work:
[Data Visualization](https://github.com/jonkeane/data-visualization-intro) and [Presentation Skills](presentation-skills/) will help with that, both when communicating your work to a public audience, and to stakeholders. When you're
working directly with a project partner and are creating tools for them to use, keep
[Usability and User Interfaces](usability-and-user-interfaces/) in mind.
