# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 20:07:24 2023

@author: SIDDHI MANGALAM
"""
import streamlit as st
from datetime import datetime, timedelta
import pandas as pd

# Streamlit app
def main():
    # Set app title
    st.title('Medication Adherence Reminder')
    
    # Add input fields
    patient_id = st.text_input('Patient ID')
    gender = st.selectbox('Gender', ['Male', 'Female'])
    medication_name = st.selectbox('Medication Name', ['Medication A', 'Medication B', 'Medication C'])
    medication_type = st.selectbox('Medication Type', ['Oral', 'Injection'])
    age = st.number_input('Age', min_value=0, step=1)
    duration_of_medication = st.number_input('Duration of Medication', min_value=0, step=1)
    hour_of_day = st.number_input('Reminder Hour', min_value=0, max_value=23, step=1)
    day_of_week = st.number_input('Reminder Day of Week', min_value=0, max_value=6, step=1)
    reminder_time = st.text_input('Reminder Time', 'HH:MM')
    # Add other input fields as needed
    
    # Create a dataframe from the input data
    input_data = pd.DataFrame({
        'patient_id': [patient_id],
        'gender': [gender],
        'medication_name': [medication_name],
        'medication_type': [medication_type],
        'age': [age],
        'duration_of_medication': [duration_of_medication],
        'hour_of_day': [hour_of_day],
        'day_of_week': [day_of_week]
        # Add other columns as needed
    })
    
    # Convert reminder time to datetime object
    reminder_datetime = datetime.strptime(reminder_time, 'HH:MM').time()
    
    # Get current time
    current_time = datetime.now().time()
    
    # Check if it's time for the reminder
    if current_time.hour == reminder_datetime.hour and current_time.minute == reminder_datetime.minute:
        st.write('Reminder: Take medication', medication_name)
    
    # Add other conditions or actions based on your requirements
 
    
    # Add your name at the end
    st.text("Created by Siddhi Manglam")
    
    # Add a spacer for layout adjustment
    st.empty()
    
    # Add Remind button at the bottom
    if st.button('Remind'):
        st.write('Reminder sent: Take Medication ,',medication_name)

# Run the Streamlit app
if __name__ == '__main__':
    main()
