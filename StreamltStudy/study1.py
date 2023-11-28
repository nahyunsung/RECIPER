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
    icon_image = Image.open("aniicon.png")
    shadow_image = Image.open("leaf-shadow.png")
    
    icon = folium.CustomIcon(
        icon_image,
        icon_size=(38, 95),
        icon_anchor=(22, 94),
        shadow_image=shadow_image,
        shadow_size=(50, 64),
        shadow_anchor=(4, 62),
        popup_anchor=(-3, -76),
    )
    
    for idx, geo_df_row in df.iterrows() :
        marker = folium.Marker(
            location=[geo_df_row["위도"], geo_df_row["경도"]],
            popup=geo_df_row['전화번호'],  # 마커에 표시될 설명
            icon=icon  # 마커의 아이콘 설정
        )
        
        # 마커를 Folium 맵에 추가
        marker.add_to(m)
        
    # Folium 맵을 HTML 코드로 변환
    folium_html = m._repr_html_()
    
    # Streamlit에서 HTML 코드를 표시
    st.components.v1.html(folium_html, width=700, height=500)
