from statistics import fmean
import streamlit as st
import time
import numpy as np

st.set_page_config(page_title="불/합법 분류해보기", page_icon="📈")

def SecondMenu():
    st.title('합법 데이터 고르기')

    with st.form('Select'):
        language = ['무단 크롤링', '유튜브 영상 이용', '공공 데이터 사용', '위키 복사', '회원정보 수집']
        st.multiselect('합법 데이터 인 것만을 고르시오. 복수선택', language)
        if st.form_submit_button('제출하기'):
            st.write("잘 맞추셨습니다!")


SecondMenu()
