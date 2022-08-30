# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 09:07:13 2022

@author: ACER
"""

import streamlit as st
import numpy as np 
from common_functions import get_dataset, subheading, table_maker, markdown_runner
import pandas as pd

df = get_dataset()

def cal_distance(lat1, lon1, lat2, lon2): 
    point1 = np.array((lat1, lon1))
    point2 = np.array((lat2, lon2))
    sum_vectors = np.sum(np.square(point1 - point2))
    dist = (np.sqrt(sum_vectors))
    return dist

nearby = []
def pub_finder(lat_user, lon_user):
    latitudes = df['latitude']
    longitudes = df['longitude']
    name = df['name']
    
    for i in range(len(latitudes)):
        dist = cal_distance(lat_user, lon_user, latitudes[i], longitudes[i])
        nearby.append([dist, latitudes[i], longitudes[i], name[i]])
    
    nearby.sort()
    df1 = pd.DataFrame(nearby, columns=["dist", "lat", "lon", "name"])
    markdown_runner(subheading("The MAP is as follows: "))
    st.map(df1.head())
    markdown_runner(subheading("Name of the pubs are as follows: "))
    table_maker(df1["name"].head())
    
def main():
    lat = st.number_input(label="Enter your Latitude: ")
    lon = st.number_input(label="Enter yor longitude: ")
    if st.button(label="Get Nearby Pubs"):
        pub_finder(lat, lon)
