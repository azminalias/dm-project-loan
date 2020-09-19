#!/usr/bin/env python3.7.6

import streamlit as st
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Bank Loan Application Project')
st.markdown('**by** Azmin Alias, Muhammad Shafiq, Cheng Jia Sheng')
st.write('')

df = pd.read_csv('Bank_CS.csv')
df.drop(df.columns[0], inplace=True, axis=1)
df.drop(df.columns[0], inplace=True, axis=1)

### Cleaning
df['Loan_Amount'].fillna(df['Loan_Amount'].mean(), inplace=True)
df['Loan_Tenure_Year'].fillna(df['Loan_Tenure_Year'].median(), inplace=True)
df['Credit_Card_types'].fillna('Unknown', inplace=True)
df['Years_to_Financial_Freedom'].fillna(df['Years_to_Financial_Freedom'].median(), inplace=True)
df['Number_of_Credit_Card_Facility'].fillna(df['Number_of_Credit_Card_Facility'].median(), inplace=True)
df['Number_of_Properties'].fillna(df['Number_of_Properties'].median(), inplace=True)
df['Number_of_Bank_Products'].fillna(df['Number_of_Bank_Products'].median(), inplace=True)
df['Property_Type'].fillna('Unknown', inplace=True)
df['Years_for_Property_to_Completion'].fillna(df['Years_for_Property_to_Completion'].median(), inplace=True)
df['State'] = df['State'].replace('P.Pinang', 'Penang')
df['State'] = df['State'].replace('Pulau Penang', 'Penang')
df['State'] = df['State'].replace('K.L', 'Kuala Lumpur')
df['State'] = df['State'].replace('Johor B', 'Johor')
df['State'] = df['State'].replace('N.S', 'N.Sembilan')
df['State'] = df['State'].replace('SWK', 'Sarawak')
df['State'] = df['State'].replace('Trengganu', 'Terengganu')
df['Number_of_Side_Income'].fillna(df['Number_of_Side_Income'].median(), inplace=True)
df['Monthly_Salary'].fillna(df['Monthly_Salary'].mean(), inplace=True)
df['Total_Sum_of_Loan'].fillna(df['Total_Sum_of_Loan'].mean(), inplace=True)
df['Total_Income_for_Join_Application'].fillna(df['Total_Income_for_Join_Application'].mean(), inplace=True)

st.markdown('Loading the cleaned loan dataset:')
st.write(df)

### Disable warning
st.set_option('deprecation.showPyplotGlobalUse', False)

st.text('')
st.markdown('Exploratory Data Analysis:')
st.text('')
st.markdown('To understand how decisions are made based on Employment Type.')
plt.figure(figsize=(12,6))
#sns.countplot(x='Employment_Type', data=df, hue="Decision")
df.groupby(["Employment_Type","Decision"]).count()["Score"].unstack().plot(kind="bar",stacked=True)
plt.title('Decisions based on Employment Type')
plt.xlabel('Employment Type')
plt.ylabel('Number of people')
st.pyplot()

st.text('')
st.markdown('To understand if the having a luxury of higher tier Credit Card will affect the decision for loan application.')
plt.figure(figsize=(12,6))
df.groupby(["Credit_Card_types","Decision"]).count()["Score"].unstack().plot(kind="barh",stacked=True)
plt.title('Decisions based on the Credit Card Type')
plt.ylabel('Credit Card Type')
plt.xlabel('Number of people')
st.pyplot()

st.text('')
st.markdown('To understand which Employment Type uses what tier of Credit Card.')
plt.figure(figsize=(12,6))
sns.countplot(x='Employment_Type', data=df, hue="Credit_Card_types", palette='rocket')
plt.title('Type of Credit Card Type based on the Employment Type')
plt.xlabel('Employment Type')
plt.ylabel('Number of people')
st.pyplot()

st.text('')
st.markdown('To see the type of properties do each employment type lives.')
plt.figure(figsize=(12, 6))
sns.countplot(x='Employment_Type', data=df, hue="Property_Type", palette='rocket')
plt.legend(loc='upper left')
plt.title('Property Type based on the Employment Type')
plt.xlabel('Employment Type')
plt.ylabel('Number of people')
st.pyplot()

st.text('')
st.markdown('Distribution of monthly salary for each states')
plt.figure(figsize=(15, 8))
sns.boxplot(data=df,x="State", y="Monthly_Salary", palette="rocket")
plt.title('Monthly Salary based on each State')
plt.xlabel('States')
plt.ylabel('Monthly Salary')
plt.ylim(3000, 13000)
st.pyplot()

st.text('')
st.markdown('Distribution of the monthly salary for each employment type.')
plt.figure(figsize=(15, 8))
sns.boxplot(data=df,x="Employment_Type", y="Monthly_Salary", palette="rocket")
plt.title('Monthly Salary based on Employment Type')
plt.xlabel('Employment Type')
plt.ylabel('Monthly Salary')
plt.ylim(3000, 13000)
st.pyplot()

st.text('')
st.markdown('Distribution of Years to Financially Free.')
plt.figure(figsize=(12, 6))
sns.countplot(x="Years_to_Financial_Freedom", data=df, palette='rocket')
plt.title('Distribution of Years to Financial Freedom')
plt.xlabel('Years to Financial Freedom')
plt.ylabel('Frequency')
st.pyplot()

st.text('')
st.markdown('Distribution of the Loan Acceptance.')
sns.countplot(x="Decision", data=df, palette='rocket')
plt.title('Decision Made')
plt.xlabel('Decision')
plt.ylabel('Frequency')
st.pyplot()
