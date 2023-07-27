# Hierarchical Naive Bayes for Identity Matching
## Project Description
This repository follows "A hierarchical Naïve Bayes model for approximate identity matching" by Wang, Atabaksh, and Chen in creating a Hierarchical Naive Bayes model to solve an identity matching task. Given two identity records, this model aims to predict whether the pair is a match or non-match. There are two notebooks, process.ipynb and model.ipynb that preprocess the data prior to labeling, and train the model following labeling. 

## Getting Started

First set up virtual env:
```
pip install virtualenv
```
Implement virtual env:
```
python3 -m venv env
```
```
source env/bin/activate
```
Download dependencies:
```
pip install -r requirements.txt
```
Set up pgmpy and the following dependencies, and then set up data (`process.ipynb`):
```
replace data/directoryident.tsv with your own file tsv file
```
Run 'process.ipynb' to produce a new tsv of fully processed data used for discretizing data in model.ipynb + a pickled bins object for a prototype of the model in `prototype.py`.

Run Model (`model.ipynb`):
```
replace data/labeledident.csv with your own file csv file
```

Run Prototype (`prototype.py`):
```
streamlit run prototype.py
```

more info on wiki page...
