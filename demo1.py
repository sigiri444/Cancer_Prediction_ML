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

st.image(r"image.jpg",use_column_width= True,)
st.title("Cancer Prediction using M.L")

gender = ["Male","Female"]
tumor =['High', 'Low', 'Medium']
family = ["Yes","No"]
alcohol = ['Moderate', 'High', 'Low']
symptoms = ['Mild', 'Moderate', 'Severe']
smoking = ['Former Smoker', 'Current Smoker', 'Non-Smoker']
exercise = ['Never', 'Regularly', 'Rarely', 'Occasionally']

model = pickle.load(open("estimator_sss.pkl","rb"))

Age=st.number_input("Enter your Age:",step=1)
Gender= st.selectbox("Enter your gender:",gender)
Tumor_Size=st.slider("Enter your tumor size:",0.0,5.0,0.0,step=0.5)
Tumor_Grade=st.selectbox("Enter your tumor grade:",tumor)
Symptoms_Severity=st.selectbox("Enter your Severity:",symptoms)
Family_History=st.selectbox("Enter if any Family History:",family)
Smoking_History=st.selectbox("Rate your Smoking consumption rate",smoking)
Alcohol_Consumption=st.selectbox("Rate your Alcohol consumption rate",alcohol)
Exercise_Frequency=st.selectbox("Exercise Routine",exercise)

pre =[]
if st.button("Submit"):
    prediction = model.predict([[Age,Gender,Tumor_Size,Tumor_Grade,Symptoms_Severity,Family_History,Smoking_History,Alcohol_Consumption,Exercise_Frequency]])[0]
    st.write("The prediction is: ", prediction)
    pre.append(prediction)
    if pre[0] == 0:
        st.write("Chance of getting cancer is Zero")
    elif pre[0] == 1:
        st.write("Chance of getting cancer is High")



st.write("Thank you")
