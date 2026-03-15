# -*- coding: utf-8 -*-
"""Health insurance model training and saving"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import pickle

# Load the dataset
df = pd.read_csv('D:/health insurance/insurance.csv')

# Display the first few rows
print(df.head())

# Display some information about the dataset
print("Dataset Shape:", df.shape)
print("Dataset Info:")
print(df.info())
print("Missing Values:")
print(df.isnull().sum())
print("Statistical Summary:")
print(df.describe())

# Visualizations
sns.set()
plt.figure(figsize=(6,6))
sns.histplot(df['age'], kde=True)
plt.title('Age Distribution')
plt.show()

plt.figure(figsize=(6,6))
sns.countplot(x='sex', data=df)
plt.title('Sex Distribution')
plt.show()

plt.figure(figsize=(6,6))
sns.histplot(df['bmi'], kde=True)
plt.title('BMI Distribution')
plt.show()

plt.figure(figsize=(6,6))
sns.countplot(x='children', data=df)
plt.title('Number of Children')
plt.show()

plt.figure(figsize=(6,6))
sns.countplot(x='smoker', data=df)
plt.title('Smoker Distribution')
plt.show()

plt.figure(figsize=(6,6))
sns.countplot(x='region', data=df)
plt.title('Region Distribution')
plt.show()

plt.figure(figsize=(6,6))
sns.histplot(df['charges'], kde=True)
plt.title('Charges Distribution')
plt.show()

# Encoding categorical variables
df.replace({'sex': {'male': 0, 'female': 1}}, inplace=True)
df.replace({'smoker': {'yes': 0, 'no': 1}}, inplace=True)
df.replace({'region': {'southeast': 0, 'southwest': 1, 'northeast': 2, 'northwest': 3}}, inplace=True)

# Features and target variable
X = df.drop(columns='charges')
y = df['charges']

# Splitting the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)

# Training the model
model = LinearRegression()
model.fit(X_train, y_train)

# Saving the model
with open('D:/health insurance/insurance_model.pkl', 'wb') as f:
    pickle.dump(model, f)

# Model evaluation
train_pred = model.predict(X_train)
test_pred = model.predict(X_test)

print("Training R^2 Score:", metrics.r2_score(y_train, train_pred))
print("Testing R^2 Score:", metrics.r2_score(y_test, test_pred))

# Example prediction
input_data = (31, 1, 25.74, 0, 1, 0)
input_data_np = np.asarray(input_data).reshape(1, -1)
prediction = model.predict(input_data_np)
print("Predicted Insurance Cost: Rs", prediction[0])
