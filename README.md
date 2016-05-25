#Curriculum Outline
We've distilled 4 years of [DSSG](http://dssg.uchicago.edu/) and [DSaPP](http://dsapp.uchicago.edu/) projects and many (sort of) early mornings spent waxing poetic over Dunkin Donuts into our idea of "what makes a data scientist for social good." This departs from the (already nebulous) definition of a data scientist, placing more weight on the ability to understand social context and to work with partners from nonprofits and government agencies. Here is our blood, sweat, and tears distilled into one Github repo/manifesto: *The Hitchhiker's Guide to DSSG*.

There's a whole lot to know, so we split it up into 8 categories: 
- **Programming,** because you'll need to tell your computer what to do, usually by writing code. 
- **Computer science,** because you'll need to manage your data and programs efficiently.  
- **Math and stats,** because [everything else in life is just applied math](https://xkcd.com/435/).
- **Machine learning,** because you'll want to do predictive modeling or look for structure in your data.
- **Social science,** because you need to understand how your work *can* and *can't* generalize.
- **Scoping and project management,** because you'll need to turn a real world problem into something you can model.   
- **Privacy, ethics, and security,** because data is people.
- **Communications,** because you want your work to be implemented and understood.
- **Social issues,** because you care about people and need to think through the context you're working in.


As the saying goes, when at DSSG do as the cool kids and data witches do. But cool kids and data witches aren't built in a day. We get a lot of questions about what fellows need to apply for the program or before they arrive, and what they can expect to learn over the summer. If you are coming to DSSG, check out the [DSSG 2016 orientation schedule](#orientation-2016). If you won't be joining us this year, we're working on assembling the resources in our [skills outline](#skills-outline).

#Skills Outline
The following five skill levels can help you gauge where you stand and what things would be useful to brush up on or seek out:   
*   [Level 0 - Fellow](#fellow): what you should know before you arrive.
*   [Level 1 - Rookie](#rookie): what you should know after orientation.
*   [Level 2 - Cool Kid](#cool-kid): what you should know at the end of the fellowship. 
*   [Level 3 - Data Scientist for Social Good](#data-scientist-for-social-good): what you should know to practice in this field.
*   [Level 4 - Data Witch](#data-witch): skills that are nice to have if you get the chance to pick them up.

##Fellow   
  Check out the [prerequisites](prerequisites/). 
   
##Rookie
###Programming
-   Python: [An Informal Introduction to Python](https://docs.python.org/2/tutorial/introduction.html)
    - Ipython notebooks, pandas, numpy, scipy, sklearn, matplotlib
-   Git
    -   [Try Git](http://try.github.com/)
    -   [Github basics](https://guides.github.com/activities/hello-world/)
-   UNIX Command Line: [A Command Line Primer for Beginners](http://lifehacker.com/5633909/who-needs-a-mouse-learn-to-use-the-command-line-for-almost-anything)
-   Introduction to databases
    - creating schemas/dbs, getting data in (copy command), getting data out (command line, python, R), SQL GUIs (dbeaver, dbvisualizer) 
- AWS/Cloud
    - ec2, rds, s3, Redshift

###Computer Science

###Math and Stats



##Cool Kid 
###Programming
using D3
using APIs to get data
Scraping
R
Parallelization
parallel for loops
mapreduce
spark
SQL DBs: types of DBs - postgres, mysql, sqllite, ms sql server, oracle
NoSQ	 DBs	
Types - pros and cons
Using one of them from python

###Computer Science
Algorithmic complexity

###Math and Stats

###Machine Learning

###Social Science
data bias
econ macro/micro
experiments
A/B
MAB


##Data Scientist for Social Good
###Programming


###Computer Science
Algorithmic complexity
Data structures: lists/hashes
Algorithms

###Math and Stats
###Machine Learning
###Social Science






##Data Witch

###Programming
front-end frameworks
JS frameworks
css

###Computer Science
###Math and Stats
Linear algebra
Simulation
Optimization
Proofs/formal logic

###Machine Learning
###Social Science
natural experiments
diff in diff
causal inference with observational data methods
regression discontinuity
matching
instrumental variables

##Conceptual and Unleveled Skills
The following skills haven't been assigned to a level or don't fit in to one. 

###Programming
how to do documentation
programming best practices
places to look up errors/debug (stackoverflow)
Complexity and Time/Space Constraints: BigO, relational vs non-relational DBs
Making nice plots in Python
parallelization: mapreduce, spark, parallel for-loops
Cleaning
Integration
record linkage (rule based and ml based)


###Scoping and Management

Project scoping
Agile 
Managing expectations with partners - how to ensure organizational support and how not to overpromise and underdeliver 
Agile

###Privacy, Ethics, and Security 
impact of data bias
prediction bias
prediction error bias
common terms
hippa
Ferpa
privacy utility tradeoff
privacy measures
k anonymity
l diversity
differential privacy


###Communications
Model Interpretation and Transparency
how to interpret different types of models
feature importances
case based explanations
communicating the possibilities/vision
communicating data
communicating models
communicating results
communicating the impact of the work

###Social Issues
Poverty
Racism
Equity
Education
Health
Environment
Politics
Government
Crime
Transportation
Jobs / economic development
International development

###Math and Stats
Time series analysis 
Linear/logistic regression
Hypothesis testing
Probability (basic theory and distributions)
Markov chains/stochastic processes 
Maximum likelihood estimation
Consistent/efficient estimators 
Bias variance tradeoff (ML)
Correlation/causation
Experimental design: randomization/replication/blocking
Nonparametric statistics, density estimation

###Machine Learning
Feature Generation
Feature selection
Methods
Unsupervised
Supervised
ranking
classification
probability estimates
Semi-supervised
For loops
Evaluation
methodology
out of sample
Cross validation
temporal cross validation
metrics
accuracy, precision, recall, auc
precision @ k
Field Trial design
Model updates and maintenance
Different types of data
text analysis
search/indexing
classification
clustering
information extraction
images
sound
video
network/graphs

#DSSG Orientation

- **Themes/philosophy**:
   - *You get out what you put in* - Fellows are encouraged to take an active role in shaping and teaching the curriculum as well as learning from it. 
   - *You learn best by doing* - Clearly motivate lessons and talks (For tech sessions: What task will require this skill or tool? What other tools exist to do similar things? Why use this tool instead of others? For conceptual talks: Why do we feel the need to present this topic? What are some concrete examples of it going well or going wrong in the past?)
- Each day starts with 10 minutes recap of yesterday & outlook for today. There will be 15 minute AM break and a 30 minute PM break. Activities begin and end on time. State the motivation behind all activities as explicitly and as clearly as possible.
- If you are assigned to a session, it is now on your calendar and it is your responsibility to do it, or to delegate it to somebody else (e.g. TMs/PMs).
- **Tech Sessions:** Last 45 minutes at the maximum and should be practical, how-to accompanied by a worksheet/exercises (with solutions) and a cheat sheet with relevant commands. Include a slide that suggests more advanced or theoretical aspects of the topic for future fellow teachouts. Provide a summary, a list of commands, and links to further resources in a markdown file. See [very serious template](tech-tutorials/tutorialtemplate/)
- **ALL SESSIONS:** By 5/27, have materials prepared and added to repo. 

Orientation (the first two weeks of the fellowship) will cover the following topics:
The first two weeks of DSSG will include the following topics: 
- [DSSG Culture and What to Expect](dssg-knowledge/logistics)
- [Software Setup](tech-tutorials/softwaresetup)
- [DSSG Logistics and Summer Overview](dssg-knowledge/logistics)
- [Pipelines and Project Workflow](dssg-knowledge/pipelines)
- [Git and Github](tech-tutorials/gitandgithub)
- [DSSG: Making the Fellowship](dssg-knowledge/makingthefellowship)
- [DSSG: Skills You Need to do Data Science for Social Good](dssg-knowledge/skillsyouneed)
- [DSSG: The Work We Do](dssg-knowledge/workwedo)
- [Command Line Tools](tech-tutorials/commandlinetools)
- [Data Security Primer](tech-tutorials/datasecurityprimer)
- [DSSG 2016 Project Overview](dssg-knowledge/projectoverview)
- [Project Management: Partners and Communications](dssg-knowledge/projectmanagement)
- [Data Exploration in Python](tech-tutorials/dataexplorationpython)
- [Project Scoping](dssg-knowledge/projectscoping)
- [CSV to DB](tech-tutorials/csvtodb)
- [Usability and User Interface](tech-tutorials/usabilityandinterfaces/)
- [Intro to Quantitative Social Science](dssg-knowledge/quantsocialscience/)
- [Best Practices for Writing Legible, Good Code](dssg-knowledge/bestpractices/)
- [Remotes, AWS & Pimp My Dotfiles](tech-tutorials/pimpmydotfiles/)
