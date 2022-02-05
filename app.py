
from email import header
import imp
from statistics import mode
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.linear_model import LinearRegression
import numpy as np
#import altair as at


st.title("Experience vs Salary")
data = pd.read_csv("Salary_Data.csv")
x = np.array(data["YearsExperience"]).reshape(-1, 1)
lr = LinearRegression()
lr.fit(x, np.array(data["Salary"]))


sidebar = st.sidebar
rad = sidebar.radio("Navigation", ["Home", "Prediction", "Contribute to dataset"])


#Home
if rad=="Home":
    st.image("salary.jpg", width = 600)
    if st.checkbox("show data"):  
        st.table(data)

    graph = st.selectbox("What kind of plot you want", ["interactive", "Non interactive"])
    sliderValue = st.slider("Filter by experience", 1, 20)
    data = data.loc[data["YearsExperience"] >= sliderValue ]
    #st.write(slider)

    if graph=="Non interactive":
        plt.figure(figsize=(10, 10))
        fig, ax = plt.subplots()
        ax.scatter(data["YearsExperience"],data["Salary"])
        plt.xlabel("years of experience")
        plt.ylabel("Salary")
        plt.tight_layout()
        st.pyplot(fig)

    if graph=="interactive":
        fig = px.scatter(data, "YearsExperience","Salary")
        st.plotly_chart(fig)
    

#Prediction
if rad=="Prediction":
    st.header("Know your salary")
    val = st.number_input("Enter your experience",min_value=0.0, max_value=20.0, step=.25)
    val = np.reshape (val, (-1, 1))
    pred = lr.predict(val)[0]
    #st.write(val)

    if st.button("predict"):
        st.success(f"predicted salary is {round(pred)}")


#Contribute
if rad == "Contribute to dataset":
    st.header("Contribute to survey")
    exp = st.number_input("enter your experience",0.0, 20.0,)
    sal = st.number_input("Enter your Salary", 0.0, 1000000.0, step=0.25)
    
    #index = len(data.index)+1
    #st.table(to_add)
    #st.write(len(data.index)+1)

    
    
    if st.button("Submit"):
        addedValue = {"YearsExperience":[exp],"Salary":[sal]}
        toAdd = pd.DataFrame(addedValue)
        data = data.append(toAdd)
        data.to_csv("Salary_Data.csv")
        st.success("Submitted")
        



    
