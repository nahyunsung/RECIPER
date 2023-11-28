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
    
    m = folium.Map(location=[37.7749, -122.4194], zoom_start=10)

    # Folium 맵을 HTML 파일로 저장
    m.save("folium_map.html")
    
    # Streamlit에서 HTML 파일을 로드하여 표시
    st.components.v1.iframe("folium_map.html", width=700, height=500)
