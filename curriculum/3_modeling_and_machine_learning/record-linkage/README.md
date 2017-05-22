# Record Linkage

## Background and Motivation

The goal of record linkage is to determine if pairs of records describe
the same entity. This is important for removing duplicates from a data
source or joining two separate data sources together. Record linkages
also goes by the terms -- data matching, merge/purge, duplication detection, 
de-duping, reference matching, co-reference/anaphora -- in various fields. There
are several approaches to record linkage that includes exact matching, 
rule-based linking and probabilistic linking. An example of exact matching
is joining records based on social security number. Rule-based matching
involves applying a cascading set of rules that reflect the domain knowledge
of the records being linked. In probabilistic record linkage, linkage weights
are calculated based on records and a threshold is applied to make a decision
of whether to link records or not. 

## Installation

The tutorial is Python2/3 compatible. The dependencies can be found in the
`requirements.txt` file. 

Create a virtual environment:
```
virtualenv --no-site-packages rl-venv
source rl-venv/bin/activate
pip install -r requirements.txt
```
