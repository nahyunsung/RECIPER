import folium
import streamlit as st

from streamlit_folium import st_folium

# center on Liberty Bell, add marker
latData = 37.689140353876326 # 안양공업고등학교 위도
lonData = 127.754518810868 # 안양공업고등학교 경도

center = [37.541, 126.986]

m = folium.Map(location=center, zoom_start=12)

# call to render Folium map in Streamlit
st_data = st_folium(m, width=725)