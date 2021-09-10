import collections
from numpy.core.defchararray import lower
import streamlit as st
import numpy as np
import tensorflow as tf
import cv2
from PIL import Image, ImageOps

@st.cache(allow_output_mutation=True)
def load_model():
    model=tf.keras.models.load_model('/Users/kanzashaikh/Documents/NED21/FYP/Sign_Language_Recognition_and_Translation_System/model_for_urdu_alphabets.hdf5')
    return model

@st.cache(allow_output_mutation=True)
def vars():
    if not ('arr' in globals()):
        global arr
        arr = []
    if not ('word' in globals()):
        global word
        word = ""
    return arr, word


def import_and_predict(image_data, model):
    image1 = np.array(image_data)
    new_image = cv2.resize(image1, (64, 64))
    grayscale = cv2.cvtColor(new_image, cv2.COLOR_BGR2GRAY)
    color = cv2.cvtColor(grayscale, cv2.COLOR_BGR2RGB)
    img_reshape = color[np.newaxis,...]
    prediction_on_image = model.predict(img_reshape)
    
    return prediction_on_image

def app():
    with st.spinner('Model is being loaded..'):
        model=load_model()

    #st.markdown("## Sign Language Translation")
    st.markdown("<h1 style='text-align: center; color: #FF8C00;'>Sign Language Translation</h1>", unsafe_allow_html=True)    
    st.write("\n")

    word_dict = {0:'ا', #
             1:'ب', #
             2:'ث', #
             3:'ح', #
             4:'خ', #
             5:'د', #
             6:'ر', #
             7:'ز', #
             8:'س', #
             9:'ص', #
             10:'ط', #
             11:'ف', #
             12:'ل', #
             13:'و', #
             14:'چ', #
             15:'ک', #
             16:'ے'} #

    # Code to read a single file 
    file = st.file_uploader("Please upload a file", type=["jpg", "png"])
    st.set_option('deprecation.showfileUploaderEncoding', False)

    if file is None:
        st.text("Please upload an image file")
    else:
        image = Image.open(file).convert('RGB') 
        arr, word = vars()
        st.image(image, use_column_width=True)
        col1, col2, col3, col4 = st.columns(4)
        if col1.button('Translate'):
            prediction = import_and_predict(image, model)
            letter = word_dict[np.argmax(prediction)]
            arr.append(letter)

            for unit in arr:
                word = word + unit
            
            col1.subheader('The alphabet in image: '+letter)
            
        if col2.button('Add Space'):
            arr.append(' ')

        if col3.button('Delete'):
            arr.pop()

        if col4.button('Clear Output'):
            arr.clear()

        st.header('Output: ' + word)

