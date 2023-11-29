import streamlit as st
from PIL import Image
import folium
from streamlit_folium import st_folium
from folium import plugins
import pandas as pd
import branca

def on_button_click():
    new_url = "https://www.notion.so/c0585c3c07ed40f9b172f50a109ab3fc"
    st.markdown(new_url, unsafe_allow_html=True)

def app():
    image = Image.open('homeimage3.jpg')
    st.image(image)
    st.text('길 고양이를 볼때마다 사진을 찍어 인근 동물보호소에 연략을 줄 수 있는 사이트')
    image = Image.open('StreamltStudy/cat1.png')
    st.image(image)
    
    df = pd.read_csv("cat_url_list.csv", encoding='UTF8')
    df = df.dropna()
    m = folium.Map(location=[37.564214, 127.001699], zoom_start=12)
    
    #folium.Icon(color='blue')
    custom_icon = folium.CustomIcon(
        icon_image='aniicon.png',  # 사용자 지정 이미지 파일의 경로
        icon_size=(30, 30),  # 이미지의 크기
        icon_anchor=(15, 15),  # 이미지의 앵커 위치 (중심점)
        popup_anchor=(0, -15)  # 팝업의 앵커 위치 (마커 아이콘 위쪽)
    )
    
    for idx,geo_df_row in df.iterrows():
        html = f"""
            <h1>{geo_df_row['보호센터명']}</h1><br>
            <h3>{geo_df_row['보호센터주소']}</h3><br>
            <p>{geo_df_row['전화번호']}</p>
        """
        
        iframe = branca.element.IFrame(html=html, width=500, height=300)
        popup = folium.Popup(iframe, max_width=500)
        
        marker = folium.Marker(
            location=[geo_df_row["위도"], geo_df_row["경도"]],
            popup=popup,  # 마커에 표시될 설명
            icon=folium.Icon(color='blue')  # 마커의 아이콘 설정
        )
        
        # 마커를 Folium 맵에 추가
        marker.add_to(m)
        
    # Folium 맵을 HTML 코드로 변환
    folium_html = m._repr_html_()
    
    # Streamlit에서 HTML 코드를 표시
    st.components.v1.html(folium_html, width=700, height=500)

    image = Image.open('homeimage1.jpg')
    st.image(image)

    image = "homeimage2.jpg"
    st.image(image)
    
    if st.button('글쓰기'):
        on_button_click()
