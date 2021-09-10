import streamlit as st

# Custom imports 
from multipage import MultiPage
from pages import home, translation, catalogue

# Create an instance of the app 
app = MultiPage()

# Title of the main page
st.markdown("<h1 style='text-align: center; color: #FF8C00;'>Pakistan Sign Language Application</h1>", unsafe_allow_html=True)


# Add all your applications (pages) here
app.add_page("Home", home.app)
app.add_page("PSL Signs Catalogue", catalogue.app)
app.add_page("Translation System", translation.app)


# The main app
app.run()
