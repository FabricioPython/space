import streamlit as st
import pandas as pd



st.title("Tasks!")

st.data_editor(pd.DataFrame([{"Task":"", "Date":"","Obs":""}]), num_rows='dynamic')






