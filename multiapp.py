import streamlit as st
from streamlit_option_menu import option_menu

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})

    def run(self):
        st.sidebar.title("Navigation")
        app_titles = [app["title"] for app in self.apps]
        selected_title = st.sidebar.selectbox("Choose an App", app_titles)

        # Find the selected app and execute its function
        for app in self.apps:
            if app["title"] == selected_title:
                app["function"]()
