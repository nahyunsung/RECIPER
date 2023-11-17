from streamlit_folium import st_folium
import folium
center = [37.541, 126.986]
m = folium.Map(location=center, zoom_start=12)
st_data = st_folium(m, width=725)
