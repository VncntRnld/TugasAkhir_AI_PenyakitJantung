import pickle
import numpy as np
import streamlit as st

# load saved model
model = pickle.load(open("penyakit_jantung.sav", "rb"))

# judul web
st.title("Prediksi penyakit jantung")

col1, col2, col3 = st.columns(3)

# input
with col1:
    age = st.text_input("Umur")
with col2:
    sex = st.text_input("Jenis Kelamin")
with col3:
    cp = st.text_input("Jenis Nyeri Dada")
with col1:
    trestbps = st.text_input("Tekanan Darah")
with col2:
    chol = st.text_input("Nilai Kolestrol")
with col3:
    fbs = st.text_input("Gula Darah")
with col1:
    restecg = st.text_input("Hasil Elektrokadriografi")
with col2:
    thalach = st.text_input("Detak Jantung Maximum")
with col3:
    exang = st.text_input("Induksi Angina")
with col1:
    oldpeak = st.text_input("ST Deperesion")
with col2:
    slope = st.text_input("Slope")
with col3:
    ca = st.text_input("Nilai CA")
with col1:
    thal = st.text_input("Nilai Thal")

# Prediction
heartDiagnosis = ""

# Tombol prediction
with col3:
    if st.button("Prediksi penyakit jantung"):
        heartPrediction = model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])

        if(heartPrediction[0]==1):
            heartDiagnosis = 'Pasien Terkena Penyakit Jantung'
        else:
            heartDiagnosis = 'Pasien Tidak Terkena Penyakit Jantung'