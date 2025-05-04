import streamlit as st
import pandas as pd




def home_page():
  st.title("Tasks!")
  task_page()
  

  
  
def task_page():

  df = pd.DataFrame(
      [
        {"Task": "", "Date":"","Obs":""},
    ]
  )
  
  st.data_editor(df, num_rows="dynamic")