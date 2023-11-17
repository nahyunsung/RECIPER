import streamlit as st
import folium
m = folium.Map(location=[37.7749, -122.4194], zoom_start=10)
st.pydeck_chart(m)
