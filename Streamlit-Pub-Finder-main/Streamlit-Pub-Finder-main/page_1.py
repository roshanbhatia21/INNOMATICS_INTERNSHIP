# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 09:06:40 2022

@author: ACER
"""

from common_functions import markdown_runner, get_dataset, table_maker, subheading
from PIL import Image
import streamlit as st 
import time
import plotly.express as px

df = get_dataset()

def intro_func():
    """ provides title and intro """
    title_text = '''<p style="font-size:45px;"> Welcome to
            <span style='color:blue'> Pub Locator </span></p>'''
    markdown_runner(title_text)
    st.subheader("It will help you in finding the nearset Pub")   
    
def side_menu():
    """ Side-menu function and operations """
    add_selectbox = st.sidebar.selectbox(
    "What would you like to see ?", options=("Home", "Data Set Info", "Graph")
    )
    if add_selectbox == "Home": 
        intro_func()
        image = Image.open(r"C:\Users\ACER\Python Tutorial\Innomatics Research Labs Internship Questions\Streamlit App Development\pic.jpg", mode='r')
        st.image(image, caption='Pub Image')
        
    elif add_selectbox == "Data Set Info":
        data_statics()
    
    else: 
        graphs()
      
       
def data_statics():
    with st.sidebar:
        side_menu_stats = st.radio(
        "Select from the options",
        ("Head", "Tail", "Describe Data", "Pub count based on Name"))

    if side_menu_stats == "Head":
        markdown_runner(subheading("Info about data Head: "))
        table_maker(df.head())
    
    elif side_menu_stats == "Tail":
        markdown_runner(subheading("Info about data Tail: "))
        table_maker(df.tail())
    
    elif side_menu_stats == "Describe Data":
        markdown_runner(subheading("Description of Data: "))
        table_maker(df.describe())
    
    elif side_menu_stats == "Pub count based on Name":
        markdown_runner(subheading("Count of clubs as per name: "))
        with st.spinner('Hold On...We are Processing!!'):
            time.sleep(2)
        table_maker(df["name"].value_counts())

def graphs():
    with st.sidebar:
        side_menu_graphs = st.radio(
        "Select from the options",
        ("Number of Pubs per Location",
         "Number of pubs per postal code", "Lat-Long Realationship"))
        
    if side_menu_graphs == "Number of Pubs per Location":
            markdown_runner(subheading("Number of Pubs per Location: "))
            count = df["local_authority"].value_counts()
            count2 = df["local_authority"].unique()
        
            fig = px.bar(df,
                       x=count2,
                       y=count,
                       title="Number of Pubs per location",
                       labels={'x': 'Locations','y':'Pub Count'},
                       color=count)
            
            st.plotly_chart(fig, use_container_width=False, sharing="streamlit")
    
    elif side_menu_graphs == "Number of pubs per postal code":
        markdown_runner(subheading("Number of pubs per postal code: "))
        count = df["postcode"].value_counts()
        count2 = df["postcode"].unique()
        
        fig = px.bar(df,
                     x=count2,
                     y=count,
                     title="Number of Pubs per location",
                     labels={'x': 'Locations','y':'Pub Count'},
                     color=count)
        st.plotly_chart(fig, use_container_width=False, sharing="streamlit")
        
    elif side_menu_graphs == "Lat-Long Realationship":
        markdown_runner(subheading("Lat-Long Realationship: "))
        fig = px.scatter(x=df["latitude"],
                         y=df["longitude"],
                         labels={'x': 'Latitude','y':'Longitude'},
                         color=df["latitude"])
        st.plotly_chart(fig, use_container_width=False, sharing="streamlit")

    
    