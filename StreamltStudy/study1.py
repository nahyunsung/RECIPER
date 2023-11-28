import streamlit as st
from PIL import Image
import folium
from streamlit_folium import st_folium

def app():
    st.title('길고양이 증가에 따른 생태계 파괴')
    st.text('길 고양이를 볼때마다 사진을 찍어 인근 동물보호소에 연략을 줄 수 있는 사이트')
    image = Image.open('StreamltStudy/cat1.png')
    st.image(image)
    
    center = [37.5010,127.0509] 
    # center on Seoul pharmacy
    m = folium.Map(location=center, zoom_start=18)
    markers = plugins.MarkerCluster(transformed_coord_list)
    markers.add_to(m) 
    
    # call to render Folium map in Streamlit
    st_data = st_folium(m, width=725)
