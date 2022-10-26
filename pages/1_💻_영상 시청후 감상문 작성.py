from statistics import fmean
import streamlit as st
import time
import numpy as np

st.title('영상 시청후 감상문 작성')
col1,col2 = st.columns(2)
with col1:
    st.video("https://www.youtube.com/watch?v=fxI6zuG_YR0")
with col2:
    st.video("https://www.youtube.com/watch?v=ciLOLRGydCg")

def jechul():
    st.text_input('위 두 영상을 시청한 후 느낀점을 입력하세요.')
    if st.button('제출하기'):
        st.balloons()
        st.success('잘하셨습니다! 메뉴에서 "데이터 검증하기"를 클릭하세요. ')
        

jechul()
