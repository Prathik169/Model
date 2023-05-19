import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle
from sklearn.preprocessing import StandardScaler
st.title('Medical Diagnostic App')
st.markdown('Does the women have diabetes or not?')

# step1: load model
model=open('rfc_pickle','rb')
clf=pickle.load(model)
model.close()

# step 2: get the user input
pregs = st.number_input('Pregnancies', 0, 20, step = 1)
glucose = st.slider("Glucose", 40,200,20) #last20 is default
bp = st.slider("BloodPressure",20,140,20)
skin = st.slider("SkinThickness",5,100,5)
insulin = st.slider("Insulin", 14.0,846.0,14.0)
bmi = st.slider("BMI",15.0,70.0,15.0)
dpf = st.slider("DiabetesPedigreeFunction", 0.05, 2.50, 0.05)
age = st.slider("Age",21,90,21)

# step3 covert user input to model imput
data = {
    "Pregnancies":pregs,
    "Glucose":glucose,
    "BloodPressure":bp,
    "SkinThickness":skin,
    "Insulin":insulin,
    "BMI":bmi,
    "DiabetesPedigreeFunction":dpf,
    "Age":age
}


input_data=pd.DataFrame([data])
st.write(input_data)

# step4: get the model prediction and print it
prediction=clf.predict(input_data)
if st.button('Prediction'):
    if prediction==1:
        st.subheader('The woman has diabetes')
    if prediction==0:
        st.subheader('The woman is healthy')
