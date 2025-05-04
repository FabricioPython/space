import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="VisualCSV",
    page_icon=":arrow_up:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "fabricio.mh@protonmail.com"
    }
)




def criaData(coluna:list[str], df:pd.DataFrame, n:int):
    return st.dataframe(df[coluna].head(n), width=700, height=558)
  
def estatisticas():
  try:
    st.write(dataframe.describe())
  except:
    st.error('Você precisa carregar o arquivo.', icon="🚨")



# itens
itens: list = []

#sidebar
with st.sidebar:
  st.title("Visual:blue[CSV]")
  
  uploaded_file = st.file_uploader("Upload your files to view column information and statistical metrics.")
  

  if uploaded_file is not None:
    
    dataframe = pd.read_csv(uploaded_file)
    title = st.number_input("Escolha o número de linhas:", step=1, max_value=dataframe.shape[0], min_value=0)


    for box in dataframe.columns:
      bxn = st.checkbox(box)

      if bxn:
        itens.append(box)


  on = st.toggle("Describe")
  
  if on:
    estatisticas()
    
#cols
col1, col2, = st.columns([0.3, 0.7])

#data call
if len(itens) > 0:
  #title = st.number_input("Escolha um numero de linhas:", step=1, max_value=dataframe.shape[0])
  if title > 0:
    with col1:
      st.header("More")
    with col2:
      criaData(itens, dataframe, n=title)
  
  

  

    






