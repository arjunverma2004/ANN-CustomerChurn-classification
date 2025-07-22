import streamlit as st
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
import pandas as pd
import pickle

# Load the trained model
model = tf.keras.models.load_model('models/model.h5')

# Load the encoders and scaler
with open('models/label_encoder_gender.pkl', 'rb') as file:
    label_encoder_gender = pickle.load(file)

with open('models/onehot_encoder_geo.pkl', 'rb') as file:
    onehot_encoder_geo = pickle.load(file)

with open('models/scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)


## streamlit app
st.title('Customer Churn Prediction')

# Input columns
cols = st.columns(2)

# User input
with cols[0].container(height=110):
    geography = st.selectbox('Geography', onehot_encoder_geo.categories_[0])
with cols[1].container(height=110):
    gender = st.selectbox('Gender', label_encoder_gender.classes_)
with cols[0].container(height=110):
    age = st.slider('Age', 18, 92)
with cols[1].container(height=110):
    balance = st.number_input('Balance')
with cols[0].container(height=110):
    credit_score = st.number_input('Credit Score')
with cols[1].container(height=110):
    estimated_salary = st.number_input('Estimated Salary')
with cols[0].container(height=110):
    tenure = st.slider('Tenure', 0, 10)
with cols[1].container(height=110):
    num_of_products = st.slider('Number of Products', 1, 4)
with cols[0].container(height=110):
    has_cr_card = st.selectbox('Has Credit Card', ['Yes', 'No'])
    if has_cr_card=='Yes':
        has_cr_card_val=1
    else:
        has_cr_card_val=0
with cols[1].container(height=110):
    is_active_member = st.selectbox('Is Active Member', ['Yes', 'No'])
    if is_active_member=='Yes':
        is_active_member_val=1
    else:
        is_active_member_val=0

# Prepare the input data
input_data = pd.DataFrame({
    'CreditScore': [credit_score],
    'Gender': [label_encoder_gender.transform([gender])[0]],
    'Age': [age],
    'Tenure': [tenure],
    'Balance': [balance],
    'NumOfProducts': [num_of_products],
    'HasCrCard': [has_cr_card_val],
    'IsActiveMember': [is_active_member_val],
    'EstimatedSalary': [estimated_salary]
})

# One-hot encode 'Geography'
geo_encoded = onehot_encoder_geo.transform([[geography]]).toarray()
geo_encoded_df = pd.DataFrame(geo_encoded, columns=onehot_encoder_geo.get_feature_names_out(['Geography']))

# Combine one-hot encoded columns with input data
input_data = pd.concat([input_data.reset_index(drop=True), geo_encoded_df], axis=1)

# Scale the input data



if st.button("Predict"):
    try:
        # Scale the input data
        input_data_scaled = scaler.transform(input_data)
        # Predict churn
        prediction = model.predict(input_data_scaled)
        prediction_proba = prediction[0][0]

        
        # Output
        if prediction_proba > 0.5:
            st.subheader(f"🧠 Prediction Result: {prediction_proba:,.2f}")
            st.error('The customer is likely to churn.')
            
        else:
            st.subheader(f"🧠 Prediction Result: {prediction_proba:,.2f}")
            st.success('The customer is not likely to churn.')
        

    except Exception as e:
        st.error(f"Error during prediction: {e}")
