import streamlit as st
import sklearn
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler,OneHotEncoder,OrdinalEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
import pickle


model = pickle.load(open("estimator_sss.pkl","rb"))

Age=st.number_input("Enter your Age:",step=1)
Gender= st.text_input("Enter your gender:")
Tumor_Size=st.number_input("Enter your tumor size:")
Tumor_Grade=st.text_input("Enter your tumor grade:")
Symptoms_Severity=st.text_input("Enter your Severity:")
Family_History=st.text_input("Enter if any Family History:")
Smoking_History=st.text_input("Rate your Smoking consumption rate")
Alcohol_Consumption=st.text_input("Rate your Alcohol consumption rate")
Exercise_Frequency=st.text_input("Exercise Routine")


if st.button("Submit"):
    prediction = model.predict([[Age,Gender,Tumor_Size,Tumor_Grade,Symptoms_Severity,Family_History,Smoking_History,Alcohol_Consumption,Exercise_Frequency]])[0]
    st.write("The prediction is: ", prediction)


st.write("Thank you")