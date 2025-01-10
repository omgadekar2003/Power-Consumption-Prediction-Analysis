
import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the trained model (assuming you have a 'model.joblib' file)
@st.cache_resource
def load_model():
    # Load the model using joblib
    model = joblib.load('predict_data.pkl')
    return model

# Function to predict power consumption based on input features
def predict_power_consumption(temp, humidity, wind_speed, gen_diffuse_flows, diffuse_flows, day, month):
    # Prepare input data for prediction
    input_data = np.array([[temp, humidity, wind_speed, gen_diffuse_flows, diffuse_flows, day, month]])
    
    # Load the model and make predictions
    model = load_model()
    prediction = model.predict(input_data)
    
    # Return the predicted power consumption for each zone
    return prediction[0]

# Set up the Streamlit interface
st.title('Power Consumption Prediction')
st.write("""
    This app predicts the power consumption for three zones based on environmental and time-based factors.
""")

# Input fields (all values are now floating point numbers to avoid type mismatch)
temp = st.number_input('Temperature (°C)', min_value=-100.0, max_value=100.0, value=0.0)
humidity = st.number_input('Humidity (%)', min_value=0.0, max_value=100.0, value=75.0)
wind_speed = st.number_input('Wind Speed (m/s)', min_value=0.0, max_value=50.0, value=5.0)
gen_diffuse_flows = st.number_input('General Diffuse Flows', min_value=0.0, value=0.0001)
diffuse_flows = st.number_input('Diffuse Flows', min_value=0.0, value=0.0005)
day = st.number_input('Day of the Year (1-365)', min_value=1.0, max_value=365.0, value=1.0)
month = st.number_input('Month (1-12)', min_value=1.0, max_value=12.0, value=1.0)

# When the user presses the "Predict" button
if st.button('Predict'):
    # Call the function to get predictions
    predicted_consumption = predict_power_consumption(temp, humidity, wind_speed, gen_diffuse_flows, diffuse_flows, day, month)
    
    # Display results
    st.subheader('Predicted Power Consumption:')
    st.write(f"Power Consumption Zone 1: {predicted_consumption[0]:.2f} kWh")
    st.write(f"Power Consumption Zone 2: {predicted_consumption[1]:.2f} kWh")
    st.write(f"Power Consumption Zone 3: {predicted_consumption[2]:.2f} kWh")


# Add a video with heading 'Power Consumption Analysis'
st.header('Power Consumption Analysis')
st.write("Watch the video below for more insights on power consumption analysis and how predictions are made.")
    
# Use st.video to display a video
# Option 1: Video from local file (make sure the video file is in the same directory)
st.video("project_video.mp4")
