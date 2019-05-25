# Text Analysis 

## Motivation and Background

This provides an overview of how we can make use
of text data using computational data analysis methods. We cover the types of analysis that can be done with text data (search, topic detection, classification, etc.) and give an overview of how to do these analysis, tasks that they’re useful for, and how to evaluate the results. We provide a set of tools that are commonly used for doing text analysis and provide.

We often deal with text data that comes from a variety of sources - open ended survey responses, phone call transcriptions, social media data, notes from electronic health records, and news. A challenge we face when dealing with these types of data is how to efficiently analyze it just like we do structured (tabular) data. For example, when analyzing survey responses or electronic health records data, both of which contain narrative text (from the respondents and medical practitioners respectively), the text data often gets ignored or read by the analysts (manually) and used anecdotally. Text analysis techniques described here allow you to use all of the data available (structured and unstructured), and efficiently incorporate large amounts of text data in your analysis. 

Things you should learn after this:
- How is text data different than “structured” data?
- What types of analysis can be done with text data?
    - Use it by itself
    - Combine it with structured data
- List the types of analysis and examples
- How do we do the analysis
 - Processing Pipeline
    - Tokenization
    - Stemming
    - Stopwords
    - Linguistic analysis
    - Turning text into a matrix
    - Term weights
    - TFIDF
- Analysis (what it is, how to do it, how to evaluate it, and applications/examples in social science)
    - Finding similar documents
    - Finding themes and topics (describe the methods, examples, and evaluation process)
    - Clustering
    - Topic models
    - Classification  (describe the methods, examples, and evaluation process)
    - Deep Learning and Word Embeddings
- Tools
- Summary


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

## Further Resources

1. [Natural Language Processing with Python](http://victoria.lviv.ua/html/fl5/NaturalLanguageProcessingWithPython.pdf)
2. [Getting Started with NLP](http://desilinguist.org/pdf/crossroads.pdf)

