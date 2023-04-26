import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

food=pd.read_csv("C:/Users/Lenovo/Documents/DATA ANALYSIS/Python/Food.csv") 

df =food.copy()
df.drop('mp_commoditysource', axis=1, inplace=True)
df.drop('cur_id', axis=1, inplace=True)
df.rename(columns={
    df.columns[0]:'Country_ID',
    df.columns[1]:'Country_name',
    df.columns[2]:'Locality_ID',
    df.columns[3]:'Locality_name',
    df.columns[4]:'Market_ID',
    df.columns[5]:'Market_Name',
    df.columns[6]:'Commodity_Purchased ID',
    df.columns[7]:'Commodity_Purchased',
    df.columns[8]:'Name_of_Currency',
    df.columns[9]:'Market_TypeID',
    df.columns[10]:'Market_Type',
    df.columns[11]:'Measurment_ID',
    df.columns[12]:'Unit_of_Good_Measurment',
    df.columns[13]:'Month',
    df.columns[14]:'Year',
    df.columns[15]:'Price_Paid',
}, inplace=True)

st.title('Global Food Prices')
grp1 = df.groupby('Country_name')
# side bar 
with st.sidebar:
    st.subheader("pick a country to view more details")
    selected_country=st.selectbox("select a country", list(df.Country_name.unique()))
selected_country_details=grp1.get_group(selected_country)
st.subheader(f"{selected_country} market types")
st.write(selected_country_details[["Country_name","Market_Name"]].head(10))
    
if selected_country:
    with st.sidebar:
        st.subheader("Pick a commodity")
        lang=st.multiselect("select Commodity",["wheat flour", "potatoes", "oil", "Bread", "fuel", "Sugar"])
    used_selected_lang=selected_country_details["Commodity_Purchased"].str.split(';')
    
    st.subheader('Total Price Paid')
table_data=df.groupby('Country_name')["Price_Paid"].sum().sort_values(ascending=False).head(10)
st.write(table_data)

st.subheader('Commodity_Purchased')
table_data=df.groupby('Commodity_Purchased')["Price_Paid"].sum().sort_values(ascending=False).head(10)
st.write(table_data)

st.subheader('Highest Price Paid Countries')
grp1 = df.groupby('Country_name')
fig1,ax1=plt.subplots()
bar_data=grp1['Price_Paid'].sum().sort_values(ascending=False).head(10)
ax1.bar(bar_data.index,bar_data.values)
ax1.set_ylabel("Price_Paid")
plt.xticks(rotation=270)
st.write(fig1)

st.subheader('Highest Commdity Purchased')
fig1,ax1=plt.subplots()
pie_data=grp1['Commodity_Purchased'].value_counts().sort_values(ascending=False).head(10)
fig1,ax1=plt.subplots()
ax1.pie(pie_data, labels=pie_data.index, autopct='%1.2f%%')
st.pyplot(fig1)
plt.show()

st.subheader('Top 10 Countries')
fig2,ax1=plt.subplots(figsize=(10,8))
bar_data1=df['Country_name'].value_counts().head(10)
clr=['red','purple','green','black','pink','yellow','magenta','gold']
ax1.bar(x=bar_data1.index,height=bar_data1.values,color=['red','purple','green','black','pink','yellow','magenta','gold'])
ax1.set_ylabel("Country counts")
plt.xticks(rotation=270)
st.pyplot(fig2)

