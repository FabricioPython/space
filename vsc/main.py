import streamlit as st
from home import home_page
from fileup import fileup_page
from chat import chat_page




pg = st.navigation([
    st.Page(home_page, title="Office"),
    st.Page("data.py", title="Data visualization"),
    st.Page(fileup_page, title="Send files over the network"),
    st.Page(chat_page, title="Chat")
])

pg.run()