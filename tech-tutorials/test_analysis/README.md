# Text Analysis Example 

## Motivation and Background

Text Analysis is used for summarizing or getting useful information out of a large amount of unstructured text stored in documents. 
This opens up the opportunity of using text data alongside more conventional data sources (e.g., surveys and administrative data). The
goal of text analysis is to take a large corpus of complex and unstructured text data and extract important and meaningful messages
in a comprehensible, scaleable, adaptive and cost-effective way. 

Text Analysis can help with the following tasks:

* **Searches and information retrieval**: Help find relevant information in large databases such a systematic literature review. 
* **Clustering and text categorization**: Techniques like topic modeling modeling can summarize a large corpus of text by finding the most important phrases.
* **Text Summarizing**: Create category-sensitive text summaries of a large corpus of text.
* **Machine Translation**: Translate from one language to another.

In this tutorial we are going to analyze reddit posts from May 2015 in order to classify which subreddit a post originated 
from and also do topic modeling to categorize posts.

## Dependencies 
To run this notebook you will need the packages listed in `requirements.txt`. To install run 

```pip install -r requirements.txt``` 

in the command line. 

You will also need `jupyter notebook` and `python3` installed. 

## Data
The data was filtered from this [dataset](https://www.reddit.com/r/datasets/comments/3bxlg7/i_have_every_publicly_available_reddit_comment/). 

To unzip the data, run ```gunzip ./data/RC_2015-05.json.gz```

## Furthur Resources

1. [Natural Language Processing with Python](http://victoria.lviv.ua/html/fl5/NaturalLanguageProcessingWithPython.pdf)
2. [Getting Started with NLP](http://desilinguist.org/pdf/crossroads.pdf)

