# Data Science for Social Good Curriculum
Our number one priority is to train fellows to do data science for social good work. To this end, we've developed
a Data Science for Social Good curriculum, which includes many things you'd find in a data science course or bootcamp,
but includes an emphasis on social science, ethics, privacy, and social issues.

Our guiding teaching philosophy is as follows (see [meringue-making template](tutorial-template/) 
for an example):
- *You get out what you put in.* Fellows are encouraged to take an active role in teaching and shaping the curriculum,
as well as learning from it. Learning also takes initiative and participation on the student side.
- *Clearly motivate topics and tools.* For more technical topics: what actual task that a data scientist does will require
this tool? What other options are there to do similar tasks? What are pitfalls, and what will it look like when something
goes wrong? What are common mistakes or bugs? For conceptual topics: Why do we feel the need to communicate this topic?
What are some concrete examples of where it's been done well or poorly in the past?
- *Lessons should be user friendly.* Lectures should be concise - 45 minutes at the outside - and materials should be 
practical. Slides should be accompanied by a worksheet or exercises so fellows can follow along and learn by doing,
and a cheat sheet with relevant commands or code snippets should be included where possible.  

This guide is for DSSG summer fellows, for those who want to learn more about the program, for universities or 
companies hoping to start a similar program, and for anyone who wants to do data science for social good.

## Orientation
We expect that every incoming fellow has experience programming in Python, basic knowledge of statistics and social 
science, and an interest in doing social good. However, we understand that everyone comes from a different background, 
so to ensure that everyone is able to contribute as a productive member of the team and the fellowship, we start the first 
few weeks off with an [intensive orientation](https://github.com/dssg/hitchhikers-guide/tree/master/dssg-manual/summer-overview/DSSG2016OrientationSchedule.pdf), getting everyone "up to speed" with the basic skills and tools they'll need. 

- **Week One**
  - [Prerequisites](prerequisites/)
  - [Software Setup](software-setup/)
  - [Pipelines and Project Workflow](pipelines-and-project-workflow/)
  - [Git and Github](git-and-github/) 
  - Making the Fellowship
  - [Skills You Need](https://github.com/dssg/hitchhikers-guide/tree/master/dssg-manual/skills-you-need)
  - [Command Line Tools](command-line-tools/)
  - [Project Management, Partners, and Communications](project-management/)
  - [Data Exploration in Python](data-exploration-in-python/)
  - [Project Scoping Intro](https://dssg.uchicago.edu/2016/10/27/scoping-data-science-for-social-good-projects/)
- **Week Two**
  - [Usability and User Interfaces](usability-and-user-interfaces/)
  - [CSV to DB](csv-to-db/)
  - Legal Agreements
  - [Data Security Primer](data-security-primer/)
  - [Legible, Good Code](legible-good-code/)
  - [Conduct, Culture, and Communications](https://github.com/dssg/hitchhikers-guide/blob/master/dssg-manual/conduct-culture-and-communications/README.md)
- **Week Three**
  - [Reproducible ETL](reproducible-ETL/)
  - The Work We Do
  - [Record Linkage](record-linkage/)
  - [Databases](databases/)
  - [Quantitative Social Science](quantitative-social-science/)

##  Ongoing Curriculum
Training continues on throughout the summer in the form of "lunch and learns" - less formal lessons over lunch - and 
teachouts by staff or fellows who have relevant specializations. Sometimes we ask for volunteers to do a teachout on 
a topic we think is important, like data visualization or inference with observational data, and a few fellows will work
together to put together a lesson. Sometimes a DSSGer will suggest a topic that they have a pet interest in, or that they
think will be relevant to one or more of the summer projects. We have lunch and learns scheduled twice a week through the
summer, and some fellows choose to offer optional teachouts at the end of the workday.

Although we don't expect all twelve teams to be working in unison, there is a [general structure](https://github.com/dssg/hitchhikers-guide/blob/master/dssg-manual/summer-overview/high-level-summer-plan.pdf) 
to the summer that guides how we pace the remaining curriculum - we try to schedule topics so that fellows know about 
them with enough time to incorporate them into their projects, but not so early that they've forgotten about what they 
learned by the time the knowledge would be useful. As we get nearer to the end of the summer, there are fewer required
topics, so there are more open time slots for fellows to do teachouts.

- **The Rest of the Summer**
  - Educational Data and Testing (Kevin Wilson)
  - Social Good Business Models (Allison Weil and Paul van der Boor)
  - [Basic Web Scraping](basic-web-scraping/) (Matt Bauman)
  - Pipelines and Evaluation
  - Feature Generation Workshop
  - [Test, Test, Test](test-test-test/) (Benedict Kuester)
  - Beyond the Deep Learning Hype (Reza Borhani)
  - [Causal Inference with Observational Data](causal-inference/) (Dean Magee, Monica Alexander, Zhe Zhang, and Jackie Gutman)
  - Model Evaluation
  - Spatial Analysis Tools
  - [Operations Research](operations-research/) (Jan Vlachy)
  - Theory and Theorizing in the Social Sciences (Tom Davidson)
  - Web Classification (Yaeli Cohen)
  - [Presentation Skills](presentation-skills/) (Allison Weil)
  - [Data Visualization](https://github.com/jonkeane/data-visualization-intro) (Jon Keane, Monica Alexander, Diego Olano, Ned Yoxall)
  - [Natural Language Processing](text-analysis/) (Garren Gaut)
  - Open and Closed Data (Jen Helsby) 

# Data Science Project Example 
When you first start a project, first make sure you have gone through the [Prerequisites](prerequisites/)
and [Software Setup](software-setup/) and are equipped with the basic knowledge and tools you'll need.
Then, you need to get some data and decide on a good project to use the data for - look at our 
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

Now you're ready to start digging into the data! Python is a good tool for exploratory data analysis; 
[Data Exploration in Python](data-exploration-in-python/). If you need to link data from multiple sources,
[Record Linkage](record-linkage/) will be useful here. By now you'll also want to be using 
[Git and Github](git-and-github/) to keep track of the progress of your project, and to work with collaborators
and teammates. If you have text data, [Natural Language Processing](text-analysis/) will be useful.

Now you're ready to make some models. See the machine learning notebook. As your models produce results,
it's important to provide context and interpretations for the results of said models; [Quantitative Social Science](quantitative-social-science/) and [Causal Inference with Observational Data](causal-inference/)
will help you think through what conclusions you can make from your analysis. As you start to write more 
production code, check out [Legible, Good Code](legible-good-code/) to be sure that you're following 
best practices to make your code readable and reusable, and [Test, Test, Test](test-test-test/) (Benedict Kuester)
to learn how to write tests to keep your code base in tip-top shape.

Remember that there's no point to doing data science for social good work if you don't have some audience
that can understand it and put your insights to good use. You'll need to be able to communicate your work: 
[Data Visualization](https://github.com/jonkeane/data-visualization-intro) and [Presentation Skills](presentation-skills/) will help with that, both when communicating your work to a public audience, and to stakeholders. When you're 
working directly with a project partner and are creating tools for them to use, keep 
[Usability and User Interfaces](usability-and-user-interfaces/) in mind.


