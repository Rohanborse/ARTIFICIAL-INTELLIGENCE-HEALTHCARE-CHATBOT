import re
import streamlit as st
import pandas as pd
import pyttsx3
from sklearn import preprocessing
from sklearn.tree import DecisionTreeClassifier, _tree
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
import csv
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

def main():
    st.title("HealthCare ChatBot")

    st.sidebar.title("Options")
    selected_option = st.sidebar.selectbox("Select an option", ["Home", "ChatBot"])

    if selected_option == "Home":
        st.header("Welcome to HealthCare ChatBot")
        st.write("This is a Streamlit app version of the HealthCare ChatBot.")

    elif selected_option == "ChatBot":
        st.header("HealthCare ChatBot")
        st.write("Enter the required information to use the ChatBot.")

        # Your existing ChatBot code here (excluding the imports and functions)

if __name__ == "__main__":
    main()
