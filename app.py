import streamlit as st
import numpy as np
import joblib

model = joblib.load("model.pkl")

st.title("Fraud Detection AI App")

v1 = st.number_input("V1")
v2 = st.number_input("V2")
v3 = st.number_input("V3")
v4 = st.number_input("V4")
v5 = st.number_input("V5")
amount = st.number_input("Amount")

if st.button("Predict"):
    data = np.array([[v1, v2, v3, v4, v5, amount] + [0]*24])
    pred = model.predict(data)[0]

    if pred == 1:
        st.error("FRAUD DETECTED")
    else:
        st.success("LEGITIMATE")