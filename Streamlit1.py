import streamlit as st
import pandas as pd

st.write("# RECIPER")
Genders = ["남성", "여성"]
GenderRadio = st.radio("자신의 성을 고르세요", Genders)
age = st.slider("몇 살이세요?", 0, 100, 50)

if GenderRadio == "남성":
    st.write("남성 환영 ", age)
else:
    st.write("여성 환영 ", age)

