import streamlit as st
from PIL import Image
import folium
from streamlit_folium import st_folium
from folium import plugins

def app():
    st.title('길고양이 증가에 따른 생태계 파괴')
    st.text('길 고양이를 볼때마다 사진을 찍어 인근 동물보호소에 연략을 줄 수 있는 사이트')
    image = Image.open('StreamltStudy/cat1.png')
    st.image(image)
    
    m = folium.Map(location=[45, -122], zoom_start=4)
