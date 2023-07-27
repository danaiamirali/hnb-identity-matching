# Hierarchical Naive Bayes for Identity Matching

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
Run 'process.ipynb' to produce a new tsv of fully processed data + pickled bins object used for discretizing data in model.ipynb.

Run Model (`model.ipynb`):
```
replace data/labeledident.csv with your own file csv file
replace bins object with your own pickled file
```

more info on wiki page...
