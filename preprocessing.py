# -*- coding: utf-8 -*-
"""Preprocessing.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1D0sEilwDxosqTqQSWATaZqoNn12bsbZa
"""

# Code for uploading data
from google.colab import files
uploaded = files.upload()

# Load necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
data = pd.read_csv('/content/dataset for assignment 2.csv')
data.head()

# Check for missing values
print(data.isnull().sum())

# Handle missing values (example: filling with mean for numerical columns only)
numerical_columns = ['Age', 'App Sessions', 'Distance Travelled (km)', 'Calories Burned']
data[numerical_columns] = data[numerical_columns].fillna(data[numerical_columns].mean())

# Encode categorical variables
categorical_columns = ['Gender', 'Activity Level', 'Location']
data = pd.get_dummies(data, columns=categorical_columns, drop_first=True)
data.head()