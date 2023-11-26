import streamlit as st

from streamlit_option_menu import option_menu

import study1, page2

st.set_page_config(
    page_title="CAT",
)

class MultiApp:

    def __init__(self):
        self.apps = []
    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run():
        app = option_menu(
            menu_title='Pondering',
            options=['Home', 'Camera'],
            icons=['house-fill', 'camera-video-fill'],
            menu_icon='chat-text-fill',
            default_index=2,
            styles={
                "container": {"padding": "5!important", "background-color":'black'},
                "icon": {"color": "white", "font-size": "23px"},
                "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
                "nav-link-selected": {"background-color": "#02ab21"},}
        )

        if app=='Home':
            study1.app()
        if app == 'Camera':
            page2.app()

    run()