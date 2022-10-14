import streamlit as st
import pandas as pd
import csv

st.write("# RECIPER")
Genders = ["남성", "여성"]
GenderRadio = st.radio("자신의 성을 고르세요", Genders)
age = st.slider("몇 살이세요?", 0, 100, 50)
Food_File = open("Food_data.csv", "r")
Food_Data = csv.reader(Food_File)

if GenderRadio == "남성":
    st.write("남성 환영 ", age)
else:
    st.write("여성 환영 ", age)

for x in range(1, 6):
    st.write(Food_Data[x])
