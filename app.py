import pickle 
import streamlit as st
import pandas as pd

# Membaca model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

# Membaca data dari file CSV
data = pd.read_csv('data.csv')

# Judul Web
st.title('Data Mining Prediksi Diabetes by Abror')

# Membagi kolom
col1, col2 = st.columns(2)

with col1:
    st.markdown('<style>div.stTextInput.st-cc input {border: 1px solid black;}</style>', unsafe_allow_html=True)
    Pregnancies = st.text_input('Masukkan bulan kehamilan')

with col2:
    st.markdown('<style>div.stTextInput.st-cc input {border: 1px solid black;}</style>', unsafe_allow_html=True)
    Glucose = st.text_input('Masukkan tingkat kadar gula')

with col1:
    st.markdown('<style>div.stTextInput.st-cc input {border: 1px solid black;}</style>', unsafe_allow_html=True)
    BloodPressure = st.text_input('Masukkan tingkat tekanan darah')

with col2:
    st.markdown('<style>div.stTextInput.st-cc input {border: 1px solid black;}</style>', unsafe_allow_html=True)
    SkinThickness = st.text_input('Masukkan ketebalan kulit')

with col1:
    st.markdown('<style>div.stTextInput.st-cc input {border: 1px solid black;}</style>', unsafe_allow_html=True)
    Insulin = st.text_input('Masukkan tingkat Insulin')

with col2:
    st.markdown('<style>div.stTextInput.st-cc input {border: 1px solid black;}</style>', unsafe_allow_html=True)
    BMI = st.text_input('Masukkan nilai BMI')

with col1:
    st.markdown('<style>div.stTextInput.st-cc input {border: 1px solid black;}</style>', unsafe_allow_html=True)
    DiabetesPedigreeFunction = st.text_input('Masukkan total keluarga yang memiliki riwayat diabetes')

with col2:
    st.markdown('<style>div.stTextInput.st-cc input {border: 1px solid black;}</style>', unsafe_allow_html=True)
    Age = st.text_input('Masukkan umur Anda')

# Kode untuk prediksi
diab_diagnosis = ''

# Tombol prediksi
if st.button('Test Prediksi Diabetes'):
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    if diab_prediction[0] == 1:
        diab_diagnosis = 'Pasien terkena penyakit Diabetes'
    else:
        diab_diagnosis = 'Pasien tidak terkena penyakit Diabetes'

    st.success(diab_diagnosis)
