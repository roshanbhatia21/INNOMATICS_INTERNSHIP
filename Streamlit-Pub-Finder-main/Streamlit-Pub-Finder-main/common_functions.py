# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 09:10:29 2022

@author: ACER
"""
import pandas as pd
import streamlit as st

def get_dataset():
    """ Get the Dataset """
    df = pd.read_csv(r"C:\Users\ACER\Python Tutorial\Innomatics Research Labs Internship Questions\Streamlit App Development\dataset\clean_dataset.csv")
    return df 

def markdown_runner(md_code):
    """ A function to run HTML in MD code """    
    st.markdown(md_code, unsafe_allow_html=True)
    
def writer(data):
    """ A function to write data to Streamlit App """
    st.write(data)
    
def table_maker(data):
    """ A function to write data to Streamlit App """
    st.table(data)

def subheading(data):
    """ Adding Subheadings to various opertaions performed """
    sub = """<h3> <span style='color: red'> {} </span> </h3>""".format(data)
    return sub

def subheading2(data):
    """ Adding Subheadings to various opertaions performed """
    sub = """<h2> <span style='color: red'> {} </span> </h2>""".format(data)
    return sub