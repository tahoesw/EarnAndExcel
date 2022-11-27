# -*- coding: utf-8 -*-
"""Logistic Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XCW9glRTt89t283FDdzPgZBuei7y1ztD
"""

import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn import linear_model
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

DATA_DIR = "/Users/wel51x/Box/MyBox/Data/"
logistic = LogisticRegression

df = pd.read_csv(DATA_DIR + "titanic.csv").dropna()
#df

"""**Clean data and create independent df**"""

X = df.drop(["Name", "Survived", "Sex"], axis = 1)

# Transform 1st, 2nd, 3rd to 1, 2, 3
X['PClass'] = pd.factorize(X['PClass'])[0] + 1
#X

y = df.Survived
#y

from operator import le
# Step 1: define model type
model = LogisticRegression()

# Step 2: fit X to y
model.fit(X, y)
print(model.coef_, model.intercept_, model.score(X, y))

model_inputs = [[1, 30, 1], [3, 60, 0], [2, 60, 1], [2, 30, 0], [1, 20, 0]]
for i in model_inputs:
  print(i, model.predict(np.array([i])))

import math
def my_model(X):
  val = -1.2161317 * (X[0]) + -0.03793036 * (X[1]) + 2.52183243 * (X[2]) + 2.29604106
  # Logit function
  return math.e ** val / (1 +  math.e ** val)
#  return -1.2161317 * (X[0]) + -0.03793036 * (X[1]) + 2.52183243 * (X[2]) + 2.29604106

for i in model_inputs:
  print(i, my_model(i))