# Problem 2 -- Model Scoring -- for Homework 3 of CS107
# Author: Max Li

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
ridge_model.set_params(alpha = 0.1)
models = [linear_model, ridge_model]
scores = []

for model in models:
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    scores.append(score)
    print("R-squared: " + str(score))
    print(model.get_params())
    
