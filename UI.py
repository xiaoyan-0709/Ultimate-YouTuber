#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 20:14:25 2020

@author: fengbin.wang
"""
import streamlit as st
import numpy as np
import pandas as pd
import unicodedata
import nltk
from nltk.stem import WordNetLemmatizer 
from nltk.stem import PorterStemmer 
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from PIL import Image
import pickle

st.title("Utimate Youtuber Guide")
image = Image.open('Become-a-successful-Youtuber.jpg')
st.image(image, use_column_width=True)

option = st.selectbox( 'What is the category of your video?',
                      ('Entertainment', 'Music', 'Comedy','People & Blogs','News & Politics','Howto & Style','Sports','Film & Animation','Science & Technology','Education','Gaming','Pets & Animals','Travel & Events','Autos & Vehicles'))
st.write('You selected:', option)
category_dict = {'Entertainment':24, 'Music':10, 'Comedy':23,'People & Blogs':22,
                 'News & Politics':25,'Howto & Style':26,'Sports':17,'Film & Animation':1,
                 'Science & Technology':28,'Education':27,'Gaming':20,'Pets & Animals':15,
                 'Travel & Events':19,'Autos & Vehicles':2}

title = st.text_input('Input your title','')
#clean title

# @st.cache
def load_model_t():
    model = pickle.load(open('df_%d_t.sav'%category_dict[option], 'rb'))
    return model
x_t = [title]

if x_t == ['']:
    st.write('Your title was not detected')
else:
    y_t = load_model_t().predict(x_t)[0]
    if y_t == 5:
        st.write('**According to our model, your title score is:**',y_t,'!',':clap:'*3)
    elif y_t == 4:
        st.write('**According to our model, your title score is:**',y_t,'!',':clap:'*2)
    elif y_t == 3:
        st.write('**According to our model, your title score is:**',y_t,'!',':clap:')
    elif y_t == 2:
        st.write('**According to our model, your title score is:**',y_t,'!',':new_moon_with_face:')
    elif y_t == 1:
        st.write('**According to our model, your title score is:**',y_t,'!',':new_moon_with_face:',':worried:')
    

description = st.text_input('Input your description')
def load_model_d():
    model = pickle.load(open('df_%d_d.sav'%category_dict[option], 'rb'))
    return model
x_d = [description]

if x_d == ['']:
    st.write('Your description was not detected')
else:
    y_d = load_model_d().predict(x_d)[0]
    if y_d == 5:
        st.write('**According to our model, your title score is:**',y_d,'!',':clap:'*3)
    elif y_d == 4:
        st.write('**According to our model, your title score is:**',y_d,'!',':clap:'*2)
    elif y_d == 3:
        st.write('**According to our model, your title score is:**',y_d,'!',':clap:')
    elif y_d == 2:
        st.write('**According to our model, your title score is:**',y_d,'!',':new_moon_with_face:')
    elif y_d == 1:
        st.write('**According to our model, your title score is:**',y_d,'!',':new_moon_with_face:',':worried:')
