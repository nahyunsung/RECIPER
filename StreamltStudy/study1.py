import streamlit as st
from PIL import Image
import folium
from streamlit_folium import st_folium
from folium import plugins
import pandas as pd
import branca

def app():
    st.title('길고양이 증가에 따른 생태계 파괴')
    st.text('길 고양이를 볼때마다 사진을 찍어 인근 동물보호소에 연략을 줄 수 있는 사이트')
    image = Image.open('StreamltStudy/cat1.png')
    st.image(image)
    
    df = pd.read_csv("cat_url_list.csv", encoding='UTF8')
    df = df.dropna()
    m = folium.Map(location=[37.564214, 127.001699], zoom_start=12)


    
    for idx,geo_df_row in df.iterrows() :
        html = """
            <h1>asdf</h1><br>
            With a few lines of code...
            <p>geo_df_row['전화번호']
            <script>
                let c = 11;
                document.write(c, "<br>");
            </script>
            </p>
        """
        
        iframe = branca.element.IFrame(html=html, width=500, height=300)
        popup = folium.Popup(iframe, max_width=500)
        
        marker = folium.Marker(
            location=[geo_df_row["위도"], geo_df_row["경도"]],
            popup=popup,  # 마커에 표시될 설명
            icon=folium.Icon(color='blue',icon='star')  # 마커의 아이콘 설정
        )
        
        # 마커를 Folium 맵에 추가
        marker.add_to(m)
        
    # Folium 맵을 HTML 코드로 변환
    folium_html = m._repr_html_()
    
    # Streamlit에서 HTML 코드를 표시
    st.components.v1.html(folium_html, width=700, height=500)
