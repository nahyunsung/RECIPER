import streamlit as st
import pandas as pd

def load_data():
    return pd.DataFrame({
        "음식이름": FoodFile["음식이름"],
        "검색량": FoodFile["검색량"],
        "1월": FoodFile["1월"],
        "2월": FoodFile["2월"],
        "3월": FoodFile["3월"],
        "4월": FoodFile["4월"],
        "5월": FoodFile["5월"],
        "6월": FoodFile["6월"],
        "7월": FoodFile["7월"],
        "8월": FoodFile["8월"],
        "9월": FoodFile["9월"],
        "10월": FoodFile["10월"],
        "11월": FoodFile["11월"],
        "12월": FoodFile["12월"],
        "10대": FoodFile["10대"],
        "20대": FoodFile["20대"],
        "30대": FoodFile["30대"],
        "40대": FoodFile["40대"],
        "50대": FoodFile["50대"],
        "남성": FoodFile["남성"],
        "여성": FoodFile["여성"],
    })

st.write("# RECIPER")
Genders = ["남성", "여성"]
GenderRadio = st.radio("자신의 성을 고르세요", Genders)
age = st.slider("몇 살이세요?", 0, 100, 50)

FoodFile = pd.read_csv("Food_data.csv", encoding="utf-8")
df = load_data()

if GenderRadio == "남성":
    st.write("남성 환영 ", age)
    df = df.sort_values("남성", ascending=False)
else:
    st.write("여성 환영 ", age)
    df = df.sort_values("여성", ascending=False)

st.checkbox("너비 맞추기", value=False, key="use_container_width")

st.dataframe(df, use_container_width=st.session_state.use_container_width)

