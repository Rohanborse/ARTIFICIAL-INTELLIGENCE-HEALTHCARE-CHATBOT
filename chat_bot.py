import streamlit as st
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import preprocessing

# Load necessary data and preprocess it
training = pd.read_csv('Data/Training.csv')
cols = training.columns
cols = cols[:-1]
x = training[cols]
y = training['prognosis']
le = preprocessing.LabelEncoder()
le.fit(y)
y = le.transform(y)

x_train, _, y_train, _ = train_test_split(x, y, test_size=0.33, random_state=42)

clf1 = DecisionTreeClassifier()
clf = clf1.fit(x_train, y_train)

model = SVC()
model.fit(x_train, y_train)

# Define functions for your chatbot's logic
def predict_disease(symptoms_exp):
    # Replace this function with your actual disease prediction logic
    # This is just a placeholder
    return ["Disease 1", "Disease 2"]

# Streamlit app starts here
def main():
    st.title("HealthCare ChatBot")

    name = st.text_input("Your Name")
    st.write(f"Hello, {name}")

    disease_input = st.text_input("Enter the symptom you are experiencing")
    num_days = st.number_input("From how many days?", value=1, step=1)

    if st.button("Predict"):
        # Call your prediction function here
        predicted_diseases = predict_disease([disease_input])
        
        st.write("Predicted Diseases:")
        for disease in predicted_diseases:
            st.write(disease)

        # Add more components for displaying results and interacting with the chatbot

if __name__ == "__main__":
    main()
