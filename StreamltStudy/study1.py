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

    latData = 37.39905896377514 # 안양공업고등학교 위도
    lonData = 126.91454564601396 # 안양공업고등학교 경도
    
    center = [37.541, 126.986]
    
    m = folium.Map(location=center, zoom_start=12)
    
    # Folium 맵을 HTML 코드로 변환
    folium_html = m._repr_html_()
    
    # Streamlit에서 HTML 코드를 표시
    st.components.v1.html(folium_html, width=700, height=500)
