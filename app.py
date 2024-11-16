import streamlit as st
import joblib 
import numpy as np

@st.cache(allow_output_mutation=True)
def load_model():
    model = joblib.load("jobgrind.ipynb") 
    return model

model = load_model()

st.title("Model Deployment with Streamlit")
st.write("This app uses a trained model to make predictions.")

input_1 = st.number_input("Input Feature 1", value=0.0)
input_2 = st.number_input("Input Feature 2", value=0.0)


# Predict button
if st.button("Predict"):
    # Prepare the input data
    input_data = np.array([[input_1, input_2]])  # Adjust based on your model
    prediction = model.predict(input_data)  # Use the appropriate prediction method
    st.write(f"Prediction: {prediction}")
