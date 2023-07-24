"""
File that uses Streamlit to create a prototype to evaluate the model
Uses forms to collect personal identification data for two people
and then uses the model to predict the probability of a match
"""

# Importing libraries
import streamlit as st
import pandas as pd
import numpy as np
import Levenshtein as lev
from pgmpy.models import BayesianNetwork
from pgmpy.estimators import ExpectationMaximization
from pgmpy.inference import BeliefPropagation
from pgmpy.readwrite import BIFReader

# Creating the form
st.title('Prototype')

# Creating the form for the first person
st.subheader('Identity One')
first_name = st.text_input('First name', key='first_name')
first_middle_name = st.text_input('Middle name', key='first_middle_name')
first_surname = st.text_input('Last name', key='first_surname')
first_dob = st.date_input('Date of birth', key='first_dob')
first_address = st.text_input('Address', key='first_address')
first_id = st.text_input('ID number', key='first_id')


# Creating the form for the second person
st.subheader('Identity Two')
second_name = st.text_input('First name', key='second_name')
second_middle_name = st.text_input('Middle name', key='second_middle_name')
second_surname = st.text_input('Surname', key='second_surname')
second_dob = st.date_input('Date of birth', key='second_dob')
second_address = st.text_input('Address', key='second_address')
second_id = st.text_input('ID number', key='second_id')

# Creating the button to submit the form
submit = st.button('Submit')


# Display the results
if submit:
    # Convert the form data into a dataframe
    # Each row is a person and each column is a feature
    df = pd.DataFrame(columns=['first name', 'middle name', 'surname', 'dob', 'address', 'id'])
    df.loc[0] = [first_name, first_middle_name, first_surname, first_dob, first_address, first_id]
    df.loc[1] = [second_name, second_middle_name, second_surname, second_dob, second_address, second_id]

    def levenshtein_distance(
            s1: str,
            s2: str
    ) -> int:
        distance = lev.distance(s1, s2)
        try:
            return 1 - distance / float(max(len(s1), len(s2)))
        except ZeroDivisionError:
            return 0
        
    similarity_df = pd.DataFrame(columns=['First Name Similarity', 
                                        'Middle Name Similarity', 
                                        'Last Name Similarity', 
                                        'Date of Birth Similarity', 
                                        'Address Similarity', 
                                        'ID Similarity'
                                        'Identity Match'])

    reader = BIFReader('model.bif')
    model = reader.get_model()

    # Create a dataframe with the similarity scores using normalized Levenshtein distance
    for col in df.columns:
        similarity_df.iloc[0,df.get_loc(col)] = df[col].astype(str).apply(lambda x: pd.Series(levenshtein_distance(x.iloc[1], x.iloc[0])))

    # Discretize the similarity scores
    similarity_df = similarity_df.apply(lambda x: pd.qcut(x, 4, labels=False, duplicates='drop'))

    # TO DO

    belief_propagation = BeliefPropagation(model)
    belief_propagation.calibrate()

    match = belief_propagation.map_query(variables=['Identity Match'], evidence={similarity_df.to_dict()})

    # Display the results
    st.subheader('Results')
    st.write('The probability of a match is: ', str(match['Identity Match']))