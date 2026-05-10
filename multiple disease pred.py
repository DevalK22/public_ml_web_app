# -*- coding: utf-8 -*-
"""
Created on Fri May  8 20:50:11 2026

@author: Deval
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models

# diabetes_model = pickle.load(open('C:/Users/Deval/Desktop/AIML_YT/Multiple Disease Prediction System/saved_models/diabetes_model.sav','rb'))
# heart_disease_model = pickle.load(open('C:/Users/Deval/Desktop/AIML_YT/Multiple Disease Prediction System/saved_models/heart_disease_model.sav','rb'))
# parkinson_model = pickle.load(open('C:/Users/Deval/Desktop/AIML_YT/Multiple Disease Prediction System/saved_models/parkinson_model.sav','rb'))

# for deployment removed the path

diabetes_model = pickle.load(open('diabetes_model.sav','rb'))

heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))

parkinson_model = pickle.load(open('parkinson_model.sav','rb'))

# sidebar for navigate

with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System using ML',
                           
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinson Prediction'],
                           
                           icons = ['activity','heart','person'],
                           
                           default_index=0)

# diabetes prediction page

if(selected == 'Diabetes Prediction'):
    # page title
    st.title('Diabetes Prediction using ML')
    
    # getting the input from the user
    col1,col2,col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI Values')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    with col2:
        Age = st.text_input('Age of the person')
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        if(diab_prediction[0]==1):
            diab_diagnosis ='The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'
    st.success(diab_diagnosis)
    
    
    
    

if(selected == 'Heart Disease Prediction'):
    # page title
    st.title('Heart Disease Prediction using ML')
    
    
    # getting the input from the user
    col1,col2,col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age of the person')
    with col2:
        sex = st.text_input('Sex')
    with col3:
        cp = st.text_input('CP')
    with col1:
        trestbps = st.text_input('TRESTBPS')
    with col2:
        chol = st.text_input('CHOL')
    with col3:
        fbs = st.text_input('FBS')
    with col1:
        restecg = st.text_input('RESTECG')
    with col2:
        thalach = st.text_input('THALACH')
    with col3:
        exang = st.text_input('EXANG')
    with col1:
        oldpeak = st.text_input('OLDPEAK')
    with col2:
        slope = st.text_input('SLOPE')
    with col3:
        ca = st.text_input('CA')
    with col1:
        thal = st.text_input('THAL')
    
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for prediction
    
    if st.button('Heart Test Result'):
        heart_prediction = heart_disease_model.predict([[int(age),int(sex),int(trestbps),int(cp),int(chol),int(fbs),int(restecg),int(thalach),int(exang),float(oldpeak),int(slope),int(ca),int(thal)]])
        if(heart_prediction[0]==1):
            heart_diagnosis ='The person has Heart Disease'
        else:
            heart_diagnosis = 'The person does not have Heart Disease'
    st.success(heart_diagnosis)

if(selected == 'Parkinson Prediction'):
    # page title
    st.title('Parkinson Prediction using ML')
    
    # getting the input from the user
    col1,col2,col3 = st.columns(3)
    
    with col1:
        MDVP_Fo_Hz = st.text_input('MDVP:Fo(Hz)')
    with col2:
        MDVP_Fhi_Hz = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        MDVP_Flo_Hz = st.text_input('MDVP:Flo(Hz)')
    with col1:
        MDVP_Jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col2:
        MDVP_Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    with col3:
        MDVP_RAP = st.text_input('MDVP:RAP')
    with col1:
        MDVP_PPQ = st.text_input('MDVP:PPQ')
    with col2:
        Jitter_DDP = st.text_input('Jitter:DDP')
    with col3:
        MDVP_Shimmer = st.text_input('MDVP:Shimmer')
    with col1:
        MDVP_Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    with col2:
        Shimmer_APQ3 = st.text_input('Shimmer:APQ3')
    with col3:
        Shimmer_APQ5 = st.text_input('Shimmer:APQ5')
    with col1:
        MDVP_APQ = st.text_input('MDVP:APQ')
    with col2:
        Shimmer_DDA = st.text_input('Shimmer:DDA')
    with col3:
        NHR = st.text_input('NHR')
    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    with col1:
        spread1 = st.text_input('spread1')
    with col2:
        spread2 = st.text_input('spread2')
    with col3:
        D2 = st.text_input('D2')
    with col1:
        PPE = st.text_input('PPE')
    
    
    # code for Prediction
    parkinson_diagnosis = ''
    
    # creating a button for prediction
    
    if st.button('Parkinson Test Result'):

        parkinson_prediction = parkinson_model.predict([[float(MDVP_Fo_Hz), float(MDVP_Fhi_Hz), float(MDVP_Flo_Hz), float(MDVP_Jitter_percent), float(MDVP_Jitter_Abs), float(MDVP_RAP), float(MDVP_PPQ), float(Jitter_DDP), float(MDVP_Shimmer), float(MDVP_Shimmer_dB), float(Shimmer_APQ3), float(Shimmer_APQ5), float(MDVP_APQ), float(Shimmer_DDA), float(NHR), float(HNR), float(RPDE), float(DFA), float(spread1), float(spread2), float(D2), float(PPE)]])

        if(parkinson_prediction[0] == 1):
            parkinson_diagnosis = 'The person has Parkinson'
        else:
            parkinson_diagnosis = 'The person does not have Parkinson'

    st.success(parkinson_diagnosis)