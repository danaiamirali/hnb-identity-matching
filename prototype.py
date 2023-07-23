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

# Creating the form
st.title('Prototype')
st.header('Please fill in the following information for two people')

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


