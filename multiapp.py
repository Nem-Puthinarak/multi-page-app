import streamlit as st

class MultiApp:
    """Framework for combining multiple Streamlit applications."""
    
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        """Adds a new application.
        
        Parameters
        ----------
        title : str
            Title of the app. Appears in the dropdown in the sidebar.
        func : function
            The Python function to render this app.
        """
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        """Runs the selected application."""
        # Display select box in the sidebar for navigation
        selected_app = st.sidebar.selectbox(
            'Navigation',
            self.apps,
            format_func=lambda app: app['title']
        )

        # Get the function corresponding to the selected app
        selected_app_function = selected_app['function']

        # Execute the selected app's function
        selected_app_function()
