#Import dependencies
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn import tree
import pickle

#Random Forest Dependencies
from sklearn.ensemble import RandomForestClassifier

# # Diabetes Model - Random Forest
read_path = os.path.join('Resources/')
diabetes = pd.read_csv(f'{read_path}diabetes-dataset.csv')

#Define target
target = diabetes['Outcome']
target_names = ['negative', 'positive']

#Define data
data = diabetes.drop(['Outcome', 'Pregnancies','BloodPressure', 'SkinThickness','Insulin', 'DiabetesPedigreeFunction'], axis=1)
feature_name = data.columns

# Split the data using train_test_split
X_train, X_test, y_train, y_test = train_test_split(data, target, random_state=42)

#Create a random forest classifier
rf = RandomForestClassifier(n_estimators=200)
rf = rf.fit(X_train, y_train)
rf.score(X_test, y_test)

# Feature importance
importances = rf.feature_importances_

sorted(zip(rf.feature_importances_, feature_name), reverse=True)

file = 'rf_model.pkl'
pickle.dump(rf, open(file, 'wb'))