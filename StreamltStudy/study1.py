import streamlit as st
from streamlit_folium import st_folium
import folium

m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
folium.Marker([39.949610, -75.150282],
              popup="Liberty bell",
              tooltip="Liberty Bell").add_to(m)

st_data = st_folium(m, width = 725)