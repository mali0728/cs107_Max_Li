# Problem 2 -- Linear Regression Classes -- for Homework 3 of CS107
# Author: Max Li

import numpy as np

class Regression():

    def __init__(self):
        self.params = {}

    def get_params(self):
        return self.params

    def set_params(self, **kwargs):
        raise NotImplementedError

    def fit(self, X, y):
        raise NotImplementedError

    def predict(self, X):
        if self.params:  
            X_0 = np.ones((len(X), 1))
            full_X = np.append(np.array(X), X_0, axis=1)            
            prediction = np.dot(np.array(full_X), np.append(self.params['coeff'], self.params['intercept']))
            return prediction.tolist()
        else:
            raise NotImplementedError

    def score(self, X, y):
        y_bar = sum(y) / len(y)
        y_pred = self.predict(X)
        SST = 0.0
        SSE = 0.0
        for i in range(len(y)):
            SST += (y[i] - y_bar) ** 2
            SSE += (y[i] - y_pred[i]) ** 2
        
        r_squared = 1 - SSE / SST    
        return r_squared
            
            
class LinearRegression(Regression):

    def fit(self, X, y):
        X_0 = np.ones((len(X), 1))
        full_X = np.append(np.array(X), X_0, axis=1)
        X_T = np.transpose(full_X)
        X_product = np.dot(X_T,full_X)
        beta_hat = np.dot(np.dot(np.linalg.pinv(X_product), X_T), y)
        beta, beta_0 = beta_hat[:-1], beta_hat[-1]
        self.params['coeff'] = beta
        self.params['intercept'] = beta_0
        
        
class RidgeRegression(LinearRegression):
    
    def fit(self, X, y):
        X_0 = np.ones((len(X), 1))
        full_X = np.append(np.array(X), X_0, axis=1)
        X_T = np.transpose(full_X)
        X_product = np.dot(X_T,full_X)
        
        ita = self.params['alpha'] * np.identity(len(full_X[0]))
        ita_T = np.transpose(ita)
        ita_product = np.dot(ita_T,ita)
        
        beta_hat = np.dot(np.dot(np.linalg.pinv(X_product + ita_product), X_T), y)
        beta, beta_0 = beta_hat[:-1], beta_hat[-1]
        self.params['coeff'] = beta
        self.params['intercept'] = beta_0           

    def set_params(self, **kwargs):
        self.params['alpha'] = kwargs['alpha']   
            