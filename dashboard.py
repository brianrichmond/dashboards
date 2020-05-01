#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 18:02:00 2020

@author: brianrichmond
"""


import streamlit as st
import pandas as pd #will be used for processing the data

st.title("Exploratory Dashboard")

# print("hello")

#%%

# dataset link  https://www.kaggle.com/lava18/google-play-store-apps

# @st.cache
def load_data():
    data = pd.read_csv('/Users/brianrichmond/Documents/Data/Python/Dashboards/googleplaystore.csv')
    return data


#%%
data = load_data()
#%%
# remove empty rows & columns with NaN

data.dropna(subset = ["Rating"],inplace = True)
data = data.dropna(axis = 1, how ="all")

# convert reviews to numeric
data['Reviews'] = pd.to_numeric(data['Reviews'], errors = 'coerce')

#%%

# Add check box to dashboard to view or hide
if st.checkbox('Show Data'):
   data

#%%
# Streamlit supports most of the popular chart libraries such as vega-lite, Plotly, bokeh and more. Vega-Lite chart through Streamlit Vega-Lite api as below
# Structure: st.vega_lite_chart(data=None, spec=None, width=0, use_container_width=False, **kwargs)


st.vega_lite_chart(data, {
     'width': 'container',
     'height': 400,
     'mark':'circle',
     'encoding':{
        'x':{
           'field':'Rating',
           'type': 'quantitative'
         },
        'y':{
           'field':'Reviews',
           'type':'quantitative'
          },
        'size':{
           'field':'Rating',
           'type':'quantitative'
          },
        'color':{
           'field':'Content Rating',
           'type':'nominal'}
         }
       }, use_container_width=True)

#%%
# Create plot interactive filter 

######  ERROR 'ypeError: only list-like objects are allowed to be passed to isin(), you passed a [str]'
    
# Genres = st.selectbox("Genres", data['Genres'].unique())
# if Genres:
#     data = data[data.Genres.isin(Genres)]
    
#%%
    
    
    
    
    
   
