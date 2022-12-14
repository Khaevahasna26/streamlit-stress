import pickle
import streamlit as st
 
# load save model
model = pickle.load(open('Lvstress_model.sav', 'rb'))

# Judul Untuk Web
st.title('Data Mining Prediksi Tingkat level Stress')

st.subheader('Nama : Khaeva Hasna') 
st.subheader('Nim : 191351047')

 
# Form Input
Humidity = st.text_input('Masukan Nilai Humidity')

Temperature = st.text_input('Masukan Nilai Temperature') 

Step_count = st.text_input('Masukan  Nilai Step count')

# kode Prediksi

stress_diagnosis = ' '

#Button Prediksi
if st.button('Test'):
    stress_prediction = model.predict([[Humidity, Temperature, Step_count]])

    if(stress_prediction[0]==0):
        stress_diagnosis = 'Tingkat Stress Rendah'

    elif(stress_prediction[0]==1):
          stress_diagnosis = 'Tingkat Stress Sedang'

    else:
         stress_diagnosis = 'Tingkat Stress Tinggi'

st.success(stress_diagnosis) 
