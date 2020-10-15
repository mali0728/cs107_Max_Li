# Problem 2 -- Model Performance -- for Homework 3 of CS107
# Author: Max Li

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import Regression as reg

dataset = datasets.load_boston()
X_train, X_test, y_train, y_test = train_test_split(dataset['data'], 
                                                    dataset['target'], 
                                                    test_size=0.2, 
                                                    random_state=42)

linear_model = reg.LinearRegression()
ridge_model = reg.RidgeRegression()

alphas = np.logspace(-2, 1, 20)

linear_model.fit(X_train, y_train)
linear_model_scores = [linear_model.score(X_test, y_test)] * len(alphas)

ridge_model_scores = []

for alpha in alphas:
    ridge_model.set_params(alpha = alpha)
    ridge_model.fit(X_train, y_train)
    score = ridge_model.score(X_test, y_test)
    ridge_model_scores.append(score)


plt.xlabel('alpha')
plt.ylabel('R-squared')
line1 = plt.plot(alphas, linear_model_scores,label = 'OLS')

line2 = plt.plot(alphas, ridge_model_scores, label = 'Ridge')
plt.legend(loc = 'lower left')
plt.xscale('log')
plt.show()