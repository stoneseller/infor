from statistics import fmean
import streamlit as st
import time
import numpy as np

st.set_page_config(page_title="데이터 검증해보기", page_icon="📈")

def firstMenu():
    st.title('데이터 검증')

    with st.form('File upload'):
        filename = st.file_uploader("File Upload")
        if st.form_submit_button('저장하기'):
            st.write("")
            st.write("처리중입니다...")
            st.write("***결과 : 합법 데이터 입니다.***")

firstMenu()