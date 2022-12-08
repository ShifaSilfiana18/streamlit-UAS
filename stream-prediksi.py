import pickle 
import numpy as np 
import streamlit as st

model = pickle.load(open('patient_predictions.sav', 'rb'))

st.title('Prediksi Kelangsungan Hidup Pasien Setelah Operasi Payudara')

Age = st.text_input('Usia pasien pada saat operasi')

Op_year = st.text_input('Tahun operasi pasien')

Axil_nodes = st.text_input('Jumlah kelenjar aksila positif yang terdeteksi')

patient_diagnosis = ''

if st.button('Prediksi Kelangsungan Hidup Pasien'):
    patient_prediction = model.predict([[Age, Op_year, Axil_nodes]])
    
    if (patient_prediction[0]==1):
        patient_diagnosis = 'Pasien meninggal dalam 5 tahun'
    else:
        patient_diagnosis = 'Pasien bertahan 5 tahun atau lebih'
st.success(patient_diagnosis)            