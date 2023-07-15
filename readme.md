# Hierarchical Naive Bayes for Identity Matching

This repository follows "A hierarchical Naïve Bayes model for approximate identity matching" by Wang, Atabaksh, and Chen in creating a Hierarchical Naive Bayes model to solve an identity matching task. There are two notebooks, `process.ipynb` and `model.ipynb` that preprocess the data prior to labeling, and train the model following labeling. 

`process.ipynb` must be run first to preprocess the data, which should be stored in a folder called `data`. The notebook currently assumes the data in the data folder as a `.tsv` file called directorident (`data/directoryident.tsv`). After execution, `process.ipynb` outputs a `.csv` containing pairs of identities, containing information about the identities, as well as discretized similarity measures needed for the model. At this point, human intervention is necessary to label the data (identifying pairs of identities that are duplicates).

`model.ipynb` should be run after the `unlabeledident.csv` produced by `process.ipynb` is labeled. According to Wang, Atabaksh, and Chen, the Hierarchical Naive Bayes model is at its best in a supervised learning state where 80% of the records are labeled and 20% are not. We leave it up to the discretion of the user to choose how much of the data to label, but recommend that the user refer to the research article to make an informed decision. Following labeling, `model.ipynb` should train the model. 

---


## process.ipynb
This notebook preprocesses the data and produces a spreadsheet containing pairs of duplicates, containing all the original fields in the records, as well as discretized similarity measures to be used my the model later. These similarity measures should not be altered/changed. 

The notebook expects a the file `data/directoryident.tsv` containing some sort of ID field, a DOB field, first, middle, and last names, as well as an address field. It is critical to check in the first couple cells that the order of these columns is aligned with the code. Otherwise, assuming the spreadsheet is formatted correctly, no other modifications should be necessary to the code.

In alignment with Wang, Atabaksh, and Chen, we build the similarity measures using a normalized Levenshtein distance, and then discretize these measures to fit the multinomial model. For the specific methodology, refer to the research paper.


## model.ipynb
This notebook uses the pgmpy library...