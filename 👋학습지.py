import streamlit as st
import pandas as pd
import pydeck as pdk
from urllib.error import URLError

st.set_page_config(
    page_title="νμ΅μ§",
    page_icon="π",
)

st.sidebar.success("μ λ©λ΄λ₯Ό κ³ λ₯΄μμ€.")

st.title('νμμ μ΄λ¦μ μμ±νμΈμ!')


inputtext = st.text_input(label="User Name", value="")

button = st.button("Confirm")


st.write(button)
if button:
    con = st.container()
    con.caption("Result")
    if not str(inputtext):
        con.error("Input your name please~")
    else:
        con.write(f"λ°κ°μμ~ {str(inputtext)}λ")
        con.write(f"μ’μΈ‘ λ©λ΄λ°μμ μμ μμ²­ν κ°μλ¬Έ μμ±μ ν΄λ¦­νμΈμ!")







    