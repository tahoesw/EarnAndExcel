# -*- coding: utf-8 -*-
"""Multiple Linear Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1X7Y9df1IQArJtSgAERMOSlBaOz6pBPN6
"""

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn import linear_model

iris = load_iris()
data1 = pd.DataFrame(data=np.c_[iris["data"], iris["target"]],
                     columns=iris["feature_names"] + ["target"])

#data1

"""
X = independent (input) variable

Y = dependent (output) variable

[[]] - maintain as df; [] - create series
"""

# Select first 3 cols ('sepal length (cm)', 'sepal width (cm)', 'petal length (cm)')
X_cols = list(data1.columns[0:3])

# Inputs (independent vars) - in df format
X = data1[X_cols]
#X

# Output (dependent var) - in series format
y = data1['petal width (cm)']
#y

# Step 1: define model type
model = linear_model.LinearRegression()

# Step 2: fit X to y
model.fit(X, y)

print("coeff(sepal length (cm)) = ", model.coef_[0],
      "\ncoeff(sepal width (cm)) = ", model.coef_[1],
      "\ncoeff(petal length (cm)) = ", model.coef_[2],
      "\nintercept = ", model.intercept_)

# This function is equivalent to what ML model is giving
def my_model(X):
  return -0.20726607375742606 * (X[0]) + 0.22282854386092998 * (X[1]) + 0.5240831147784291 * (X[2]) - 0.24030738911226113

model_inputs = [[2.2, 3.3, 4.4], [5.5, 2.2, 3.3], [4.4, 5.5, 2.2], [3.3, 4.4, 5.5]]
for i in model_inputs:
  print(i, my_model(i))

"""**.Predict**"""

# Does same as my_model
for i in model_inputs:
  print(i, model.predict(np.array([i])))

# Linear Reg can give squirrely results:
print(model.predict([[5, 2, 1]]))

print("coefficient of determination =", model.score(X, y))