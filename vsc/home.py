import streamlit as st
import pandas as pd
from tinydb import TinyDB, Query

db = TinyDB('db.json')


def buscar():
    x= {'Task': {0: ''}, 'Date': {0: ''}, 'Obs': {0: ''}}
    dict_data=table.to_dict()
    if x != dict_data:
        db.insert(table.to_dict())
    
def limparData():
    db.truncate()	

st.title("Tasks!")

table = st.data_editor(pd.DataFrame([{"Task":"", "Date":"","Obs":""}]), num_rows='dynamic', key='df')


option = st.selectbox(
    "See all tasks:",
    ("-", "Tasks"),
)

if option == 'Tasks':
    for linha in db:
        st.write(pd.DataFrame(linha))
    



st.button("Clear Tasks", on_click=limparData)

st.button("Save", on_click=buscar)







