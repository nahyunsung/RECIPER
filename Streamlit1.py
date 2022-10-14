import streamlit as st
import pandas as pd
import csv

def load_data(data):
    return pd.DataFrame({
        data[0][0]: data[0][1:],
        data[1][0]: data[1][1:],
        data[2][0]: data[2][1:],
        data[3][0]: data[3][1:],
        data[4][0]: data[4][1:],
        data[5][0]: data[5][1:],
        data[6][0]: data[6][1:],
        data[7][0]: data[7][1:],
        data[8][0]: data[8][1:],
        data[9][0]: data[9][1:],
        data[10][0]: data[10][1:],
        data[11][0]: data[11][1:],
        data[12][0]: data[12][1:],
        data[13][0]: data[13][1:],
        data[14][0]: data[14][1:],
        data[15][0]: data[15][1:],
        data[16][0]: data[16][1:],
        data[17][0]: data[17][1:],
        data[18][0]: data[18][1:],
        data[19][0]: data[19][1:],
        data[20][0]: data[20][1:]
    })



st.write("# RECIPER")
Genders = ["남성", "여성"]
GenderRadio = st.radio("자신의 성을 고르세요", Genders)
age = st.slider("몇 살이세요?", 0, 100, 50)

if GenderRadio == "남성":
    st.write("남성 환영 ", age)
else:
    st.write("여성 환영 ", age)

with open('Food_data.csv','r') as f:
    reader = csv.reader(f)
    df = pd.DataFrame(reader)
    st.checkbox("Use container width", value=False, key="use_container_width")

    df1 = load_data(df)

    st.dataframe(df1, use_container_width=st.session_state.use_container_width)



