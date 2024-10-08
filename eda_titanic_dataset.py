# -*- coding: utf-8 -*-
"""eda-titanic-dataset.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11bavJveu2sBDCWMjDLqV2Pi08krFPVIN
"""

from google.colab import files
uploaded = files.upload()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('train.csv')
print("First few rows of the dataset:")
df.head()
print("\nMissing values in each column:")
print(df.isnull().sum())
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
df.drop(columns='Cabin', inplace=True)
print("\nSummary statistics of the dataset:")
print(df.describe())
print("\nData types of each column:")
print(df.dtypes)
df['Sex'] = df['Sex'].map({'male': 1, 'female': 0})
plt.figure(figsize=(8, 6))
sns.countplot(x='Survived', data=df, palette='Set2')
plt.title('Survival Distribution')
plt.xlabel('Survived')
plt.ylabel('Count')
plt.show()
plt.figure(figsize=(8, 6))
sns.barplot(x='Sex', y='Survived', data=df, palette='Set1')
plt.title('Survival Rate by Gender')
plt.xlabel('Gender (1=Male, 0=Female)')
plt.ylabel('Survival Rate')
plt.show()
plt.figure(figsize=(8, 6))
sns.histplot(df['Age'], bins=30, kde=True, color='green')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
plt.figure(figsize=(8, 6))
sns.barplot(x='Pclass', y='Survived', data=df, palette='Set2')
plt.title('Survival Rate by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Survival Rate')
plt.show()
plt.figure(figsize=(10, 8))
corr_matrix = df.drop(columns=['Name','Ticket']).corr() # Drop non-numerical columns for correlation analysis
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()
sns.pairplot(df[['Survived', 'Pclass', 'Age', 'Fare', 'SibSp', 'Parch']])
plt.show()
plt.figure(figsize=(8, 6))
sns.barplot(x='Embarked', y='Survived', data=df, palette='Set3')
plt.title('Survival Rate by Embarked Location')
plt.xlabel('Embarked (C = Cherbourg, Q = Queenstown, S = Southampton)')
plt.ylabel('Survival Rate')
plt.show()