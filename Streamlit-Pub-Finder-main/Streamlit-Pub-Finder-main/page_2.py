# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 09:06:59 2022

@author: ACER
"""

from common_functions import get_dataset, table_maker, subheading, markdown_runner
import streamlit as st 

df = get_dataset()

def search_data(search_key):
    count = df[search_key].value_counts()
    indices = count.index.tolist()
    return count, indices

def pub_pincodes():
    search_by = st.sidebar.selectbox(
         "Search using: ", ("Postal code", "local authority"))
     
    if search_by == "Postal code":
        search_key = "postcode"
        count, indices = search_data(search_key)
        add_selectbox = st.sidebar.selectbox(
            "Select the postal code ?", indices)
    
    else: 
        search_key = "local_authority"
        count, indices = search_data(search_key)
        add_selectbox = st.sidebar.selectbox(
            "Select the City Name ?", indices)
        
    
    num = (count[add_selectbox])
    
    if num == 1:
        markdown_runner(subheading("There is only " + str(num)  + " Pub in this area."))
    else: 
        markdown_runner(subheading("There are about " + str(num)  + " Pubs in this area."))
        
    re = df[df[search_key]==add_selectbox]
    rel = re[['latitude', 'longitude', 'name']]
    
    markdown_runner(subheading("The map is as follows: "))
    st.map(rel, use_container_width=True)
    
    markdown_runner(subheading("There names are as follows: "))
    table_maker(rel['name'])
    
    
    