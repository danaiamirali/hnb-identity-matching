"""
File that uses Streamlit to create a prototype to evaluate the model
Uses forms to collect personal identification data for two people
and then uses the model to predict the probability of a match
"""

# Importing libraries
import streamlit as st
import pandas as pd
import Levenshtein as lev
from pgmpy.inference import BeliefPropagation
from pgmpy.readwrite import XMLBIFReader

# Creating the form
st.title('Prototype')

# Creating the form for the first person
st.subheader('Identity One')
first_name = st.text_input('First name', key='first_name')
first_middle_name = st.text_input('Middle name', key='first_middle_name')
first_surname = st.text_input('Last name', key='first_surname')
first_dob = str(st.date_input('Date of birth', key='first_dob'))
first_address = st.text_input('Address', key='first_address')
first_id = st.text_input('ID number', key='first_id')


# Creating the form for the second person
st.subheader('Identity Two')
second_name = st.text_input('First name', key='second_name')
second_middle_name = st.text_input('Middle name', key='second_middle_name')
second_surname = st.text_input('Last name', key='second_surname')
second_dob = str(st.date_input('Date of birth', key='second_dob'))
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

    # Convert nan to empty string, and convert everything to string
    df = df.fillna('')
    df = df.astype(str)

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
                                        'ID Similarity'])

    reader = XMLBIFReader('model.xml')
    model = reader.get_model()

    # Create a dataframe with the similarity scores using normalized Levenshtein distance
    i = 0
    for col in df.columns:
        similarity_df.at[0,similarity_df.columns[i]] = levenshtein_distance(df[col].iloc[1], df[col].iloc[0])
        i += 1
    # Display each similarity score in a table
    st.subheader('Similarity Scores')
    st.write(similarity_df)

    # Discretize the similarity scores
    
    # TO DO

    belief_propagation = BeliefPropagation(model)
    belief_propagation.calibrate()

    def convert_to_state(value):
        # Convert the float to string, replace the '.' with '_', and append '0'
        state_str = str(value).replace('.', '_')
        return state_str


    evidence = similarity_df.to_dict()
    # Get rid of index in dict
    evidence = {k: convert_to_state(float(round(v[0]))) for k, v in evidence.items()}


    # for node in model.nodes():
    # st.write(f"Node: {node}, States: {model.get_cpds(node).state_names[node]}")

    # for k, v in evidence.items():
    #     if str(v) not in model.get_cpds(k).state_names[k]:
    #         st.write(f"Evidence value {v} for variable {k} does not exist in the model's states.")


    match = belief_propagation.map_query(variables=['Identity Match'], evidence=evidence)

    # Display the results
    st.subheader('Results')
    st.write('The probability of a match is: ', str(match['Identity Match']))