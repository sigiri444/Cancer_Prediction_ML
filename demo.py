import streamlit as st
import pandas as pd


st.title("Welcome to the Streamlit demo application")
st.header("by Sunil")

name = st.text_input("Enter your name")
st.write("Hey!",name,", How are you?")

age = st.number_input(' Enter your age : ',step=1,min_value=18)
st.write("Thank you, Noted!")

choice  = st.number_input("enter your choice of course 1-3:",min_value=1,max_value=3,step=1)
if choice == 0:
    st.write("Data Science")
elif choice==1:
    st.write("ML Engineer")
elif choice==2:
    st.write("Data Analyst")
else:
    st.write("GEN AI")

df = pd.read_csv(r"C:\Users\Sai Sunil\streamlit_innomatics\cancer_prediction_data (2).csv")
df.head()

st.table(df.head())