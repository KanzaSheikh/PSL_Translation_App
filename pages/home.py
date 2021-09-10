import streamlit as st 
from PIL import Image

def app():
    image = Image.open('/Users/kanzashaikh/Documents/NED21/FYP/Sign_Language_Recognition_and_Translation_System/Logo.png')
    st.image(image, width= None)
    col1, col2 = st.columns(2)
    col1.markdown("<h2 style='text-align: center; color: #FF8C00;'>Translation System</h2>", unsafe_allow_html=True)
    col2.markdown("<h2 style='text-align: center; color: #FF8C00;'>Signs Catalog</h2>", unsafe_allow_html=True)
    
    base="light"
    backgroundColor="#d4cdcd"