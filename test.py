import streamlit as st
import pandas as pd

m = 0

with st.sidebar:
    st.title('Main Menu')
    if st.button('Menu #1'):
        m = 1
    st.checkbox('Menu #2')

st.title('학습지')

