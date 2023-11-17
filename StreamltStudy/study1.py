import folium
import streamlit as st

from streamlit_folium import st_folium

center = [37.5010,127.0509] 
# center on Seoul pharmacy
m = folium.Map(location=center, zoom_start=18)

# call to render Folium map in Streamlit
st_data = st_folium(m, width=725)
