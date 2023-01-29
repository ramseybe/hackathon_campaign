import streamlit as st
import pandas as pd
import numpy as np

# checkBoxes={"abortion":False,"gun_control":False,"climate_change":False,"gender_identity":False,"pro_marijuana":False,"capital_punishment":False,"fracking":False,"defense_spending":False,"immigration":False,"net_neutrality":False}
issues=["abortion","gun_control", "climate_change", "gender_identity", "pro_marijuana", "capital_punishment", "fracking", "defense_spending", "immigration", "net_neutrality"]
checked=[]

DATA_URL='https://raw.githubusercontent.com/ramseybe/hackathon_campaign/main/50_toss_up1.csv'

left_column, right_column = st.columns([2,5])

@st.cache
def load_data(file):
    data = pd.read_csv(file)
    data=data.drop(["Unnamed: 0"],axis=1)
    dict = data.to_dict()
    return dict

thing = load_data(DATA_URL)
for key, val in thing.items():
    needed = val
    break


def checkbox_container(data):
    st.subheader('Check the important issues to you:')
    for i in data:
        st.checkbox(i, key='dynamic_checkbox_' + i)

def get_selected_checkboxes():
    return [i.replace('dynamic_checkbox_','') for i in st.session_state.keys() if i.startswith('dynamic_checkbox_') and st.session_state[i]]

with left_column:
    checkbox_container(issues)
    st.write('You selected:')
    st.write(get_selected_checkboxes())

checked = get_selected_checkboxes()

