# -*- coding: utf-8 -*-
"""1. Simple Decision Tree Classifier.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NqgNGLjClgkcTQFUD9RYSHMaAOK4Kah5
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.model_selection as ms
from sklearn.model_selection import train_test_split, StratifiedKFold, RandomizedSearchCV, GridSearchCV
from sklearn import tree
from sklearn import datasets
from sklearn import linear_model
from sklearn.linear_model import LogisticRegression
from datetime import datetime
from xgboost import XGBClassifier
import warnings
warnings.filterwarnings("ignore")

"""**Read and clean data**"""

df = pd.read_csv("titanic.csv").dropna()

X = df.drop(["Name", "Survived", "Sex"], axis = 1)

# Transform 1st, 2nd, 3rd to 1, 2, 3
X['PClass'] = pd.factorize(X['PClass'])[0] + 1

y = df.Survived

"""**Split into train/test** """

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

"""**Define model type and fit**"""

tree_model = tree.DecisionTreeClassifier()

tree_model.fit(X_train, y_train)

"""**Scoring**"""

train_score = tree_model.score(X_train, y_train)
train_error = 1 - train_score

print("Score on data used in training =", train_score, "==>error =", train_error)

test_score = tree_model.score(X_test, y_test)
test_error = 1 - test_score

print("Score on test (unseen) data =", test_score, "==>error =", test_error)