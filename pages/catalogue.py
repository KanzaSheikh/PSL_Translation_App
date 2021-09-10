import collections
from sys import path
from numpy.core.defchararray import lower
import streamlit as st
import numpy as np
import pandas as pd
#from pages import utils
import tensorflow as tf
import cv2
from PIL import Image, ImageOps
import numpy as np
import os

from tensorflow.python.keras.backend import sign

def app():
    st.markdown("<h1 style='text-align: center; color: #FF8C00;'>PSL Signs Catalogue</h1>", unsafe_allow_html=True)
    letters = ['ا',
               'ب',
               'ث',
               'ح',
               'خ',
               'د',
               'ر',
               'ز',
               'س',
               'ص',
               'ط',
               'ف',
               'ل',
               'و',
               'چ',
               'ک',
               'ے'
               ]
    image_dir = '/Users/kanzashaikh/Documents/NED21/FYP/Sign_Language_Recognition_and_Translation_System/images'

    col1, col2, col3= st.columns(3)
    for letter in letters:
        img_str = image_dir + '/' + letter + '.jpg'
        sign = Image.open(img_str)
        col2.image(sign, use_column_width=True)
        col2.header(letter)