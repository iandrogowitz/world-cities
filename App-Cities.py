import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

st.title('California Housing Data (1990) by Ian Drogowitz")
df=pd.read_csv('housing.csv')
         
price_filter= st.slider('Median House Price:', 0,500001,20000)
                        
housing_filter= st.sidebar.multiselect(
        'Choose Location'
        df.ocean.proximity.unique())
                        
income_filter= st.sidebar.radio(
    'Choose income'
    ('Low, Medium, High'))
                        
df=df[df.median_house_value >=price_filter]
df=df[df.ocean_proximity.(housing_filter))
      
if income filter ='Low':
      df=df.[df.median_income<=2.5]
elif income_filter=='Medium':
      df=df[(df.median_income> 2.5) & (df.median_income < 4.5)]
elif income_filter == 'High':
      df=df[(df.median_income>= 4.5)]
      
st. subheader('See more filters in the sidebar:')
    
st.map(df)
      
st.subheader('Histogram of Median House Value ')
      
fix, ax = plt.subplots()
df.median_house_value.hist(ax=ax, bins=30)
st.pyplot(fig)  
