from datetime import date
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
age = st.slider("몇 살이세요?", 0, 100, 18)
month = date.today()
month = month.month
st.write("## 이번 달 ", month)

FoodFile = pd.read_csv("Food_data.csv", encoding="utf-8")
FoodRecipe = pd.read_csv("recipe_list.csv", encoding="utf-8")
df = load_data()

if GenderRadio == "남성":
    st.write("남성 환영 ", age)
    df = df.sort_values("남성", ascending=False)
else:
    st.write("여성 환영 ", age)
    df = df.sort_values("여성", ascending=False)

st.checkbox("너비 맞추기", value=False, key="use_container_width")

st.dataframe(df, use_container_width=st.session_state.use_container_width)

col1, col2, col3 = st.columns(3)

with col1:
    if(st.button(FoodRecipe["FoodName"][0])):
        st.write(FoodRecipe["FoodName"][0])
with col2:
    if(st.button(FoodRecipe["FoodName"][1])):
        st.write(FoodRecipe["FoodName"][1])
with col3:
    if(st.button(FoodRecipe["FoodName"][2])):
        st.write(FoodRecipe["FoodName"][2])

txt = st.text_area('Text to analyze', '''
    It was the best of times, it was the worst of times, it was
    the age of wisdom, it was the age of foolishness, it was
    the epoch of belief, it was the epoch of incredulity, it
    was the season of Light, it was the season of Darkness, it
    was the spring of hope, it was the winter of despair, (...)
    ''')
st.write('Sentiment:', txt)

with col1:
    Resourcedata1 = st.text_input("주요 재료1", "돼지고기")

with col2:
    Resourcedata2 = st.text_input("주요 재료2", "마늘")

with col3:
    Resourcedata3 = st.text_input("주요 재료3", "달걀")

if st.button("검색"):
    st.write("검색 시작")