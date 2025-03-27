import streamlit as st
from tensorflow.keras.models import load_model
import pickle
import pandas as pd

model = load_model('model.keras')

with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

with open('gender_fit_encoder.pkl', 'rb') as file:
    gender_fit_encoder = pickle.load(file)
    
with open('geography_fit_encoder.pkl', 'rb') as file:
    geography_fit_encoder = pickle.load(file)


credit_score = st.slider("Credit Score ", 1, 800, 650)
geography = st.selectbox("Country", geography_fit_encoder.categories_[0])
gender = st.selectbox("Gender", gender_fit_encoder.classes_)
age = st.text_input("Age", 25)
tenure = st.text_input("Tenure", 5)
balance = st.text_input("Balance", 10000)
numberOfProducts = st.selectbox("Number of products", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
hasCC = st.selectbox("Has a credit card?", ["Yes", "No"])
activeMember = st.selectbox("Active member?", ["Yes", "No"])
estSalary = st.text_input("Estimate salary", 100000)


def on_click():
    input = {
        "CreditScore": credit_score,
        "Geography": geography,
        "Gender": gender,
        "Age": age,
        "Tenure": tenure,
        "Balance": balance,
        "NumOfProducts": numberOfProducts,
        "HasCrCard": hasCC == "Yes", 
        "IsActiveMember": activeMember == "Yes",
        "EstimatedSalary": estSalary
    }

    input_df = pd.DataFrame([input])
    
    encoded_geography = geography_fit_encoder.transform([[input['Geography']]])
    
    encoded_geography_df = pd.DataFrame(encoded_geography.toarray(), columns=geography_fit_encoder.get_feature_names_out(['Geography']))

    input_df = pd.concat([input_df.drop('Geography', axis=1), encoded_geography_df], axis=1)

    label_gender = gender_fit_encoder.transform([input['Gender']])
    input_df = pd.concat([input_df.drop('Gender', axis=1), pd.DataFrame(label_gender, columns=['Gender_Encoded'])], axis=1)

    scaled_input = scaler.transform(input_df)

    prediction = model.predict(scaled_input)[0][0]
    print("Prediction: ", prediction)
    st.text("Prediction: {prediction}".format(prediction=prediction))

    if (prediction > 0.5):
        st.text("You will exit the bank")
    else:
        st.text("You will not exit the bank")



st.button("Submit", on_click=on_click)
