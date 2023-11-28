import streamlit as st
from PIL import Image
import folium
from streamlit_folium import st_folium
from folium import plugins
import pandas as pd

def app():
    st.title('길고양이 증가에 따른 생태계 파괴')
    st.text('길 고양이를 볼때마다 사진을 찍어 인근 동물보호소에 연략을 줄 수 있는 사이트')
    image = Image.open('StreamltStudy/cat1.png')
    st.image(image)
    
    df = pd.read_csv("cat_url_list.csv", encoding='UTF8')
    df = df.dropna()
    m = folium.Map(location=[37.564214, 127.001699], zoom_start=12)
    
    for idx, geo_df_row in df.iterrows() :
        folium.Marker(radius=200, location=[geo_df_row["위도"], geo_df_row["경도"]], popup="asdf").add_to(m)

    
    # Folium 맵을 HTML 코드로 변환
    folium_html = m._repr_html_()
    
    # Streamlit에서 HTML 코드를 표시
    st.components.v1.html(folium_html, width=700, height=500)
