
"""
Created on Fri july 22 12:50:04 2022

@author: Ashish k
"""


import numpy as np
import pickle
import pandas as pd
import streamlit as st 
from PIL import Image

pickle_in = open("classifire.pkl","rb")
classifire=pickle.load(pickle_in)


def welcome():
    return "Welcome All"

def predict_note_authentication(age,systolic_bp,diastolic_bp,cholesterol):
    
  
   
    prediction=classifire.predict([[age,systolic_bp,diastolic_bp,cholesterol]])
    print(prediction)
    return prediction



def main():
    st.title("Diabetic Retinopathy Predictor")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Diabitic Retinopathy ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    age = st.text_input("age","Type Here")
    systolic_bp = st.text_input("systolic_bp","Type Here")
    diastolic_bp = st.text_input("diastolic_bp","Type Here")
    cholesterol = st.text_input("cholesterol","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(age,systolic_bp,diastolic_bp,cholesterol)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("a very basic web app to predict the retinopathy in patients")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    
    
    
