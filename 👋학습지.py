import streamlit as st
import pandas as pd
import pydeck as pdk
from urllib.error import URLError

st.set_page_config(
    page_title="학습지",
    page_icon="👋",
)

st.sidebar.success("위 메뉴를 고르시오.")

st.title('학생의 이름을 작성하세요!')


inputtext = st.text_input(label="User Name", value="")

button = st.button("Confirm")


st.write(button)
if button:
    con = st.container()
    con.caption("Result")
    if not str(inputtext):
        con.error("Input your name please~")
    else:
        con.write(f"반가워요~ {str(inputtext)}님")
        con.write(f"좌측 메뉴바에서 영상 시청후 감상문 작성을 클릭하세요!")







    