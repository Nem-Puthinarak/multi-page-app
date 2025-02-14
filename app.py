import streamlit as st
from multiapp import MultiApp
from apps import home, data, model, eln, charts

app = MultiApp()

st.markdown("""
# Multi-Page App

This multi-page app is using the [streamlit-multiapps]
""")

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Data", data.app)
app.add_app("Model", model.app)
app.add_app("Elnur", eln.app)
app.add_app("Charts", lambda: charts.draw_charts(data.load_data()))  # Pass the DataFrame from load_data() here
# The main app
app.run()

