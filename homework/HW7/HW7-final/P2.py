# Problem 2 -- Databases -- for Homework 7 of CS107
# Author: Max Li

import sqlite3
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer

# Part A
db = sqlite3.connect('regression.sqlite')
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS model_params")
cursor.execute("DROP TABLE IF EXISTS model_coefs")
cursor.execute("DROP TABLE IF EXISTS model_results")

cursor.execute("PRAGMA foreign_keys=1")

cursor.execute('''CREATE TABLE model_params (
               id INTEGER NOT NULL, 
               desc TEXT, 
               param_name TEXT, 
               value NUMERIC)''')

db.commit()

cursor.execute('''CREATE TABLE model_coefs (
          id INTEGER NOT NULL, 
          desc TEXT, 
          feature_name TEXT, 
          value NUMERIC)''')

db.commit()

cursor.execute('''CREATE TABLE model_results (
          id INTEGER NOT NULL, 
          desc TEXT, 
          train_score NUMERIC, 
          test_score NUMERIC)''')

db.commit()


# Part B
# Load data
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=87)

# 2. Write a function to save data to the database

# get feature name
feature_names = data.feature_names

def save_to_database(model_id, model_desc, db, model, X_train, X_test, y_train, y_test):

    train_score = model.score(X_train, y_train)
    val_score = model.score(X_test, y_test)    
        
    sqliteConnection = sqlite3.connect(db)
    cursor = sqliteConnection.cursor()
     
    INSERT_INTO_model_params  = '''INSERT INTO model_params (id, desc, param_name, value) VALUES(?, ?, ?, ?)'''
    INSERT_INTO_model_coefs = '''INSERT INTO model_coefs (id, desc, feature_name, value) VALUES(?, ?, ?, ?)'''
    INSERT_INTO_model_results = '''INSERT INTO model_results (id, desc, train_score, test_score) VALUES(?, ?, ?, ?)'''
        
    for param_name, value in model.get_params().items():
        data_input = (model_id, model_desc, param_name, value)
        cursor.execute(INSERT_INTO_model_params, data_input)
        sqliteConnection.commit()
        
    for feature_name, value in zip(feature_names, model.coef_[0]):
        data_input = (model_id, model_desc, feature_name, value)
        cursor.execute(INSERT_INTO_model_coefs, data_input)
        sqliteConnection.commit()
            
    data_input = (model_id, model_desc, 'intercept', model.intercept_[0])
    cursor.execute(INSERT_INTO_model_coefs, data_input)
    sqliteConnection.commit()
 
    data_input = (model_id, model_desc, train_score, val_score)
    cursor.execute(INSERT_INTO_model_results, data_input)
    sqliteConnection.commit()
        
    cursor.close()


# 3. Baseline logistic regression model
baseline_model = LogisticRegression(solver='liblinear')
baseline_model.fit(X_train, y_train)  
save_to_database(1,"Baseline model", 'regression.sqlite', baseline_model, X_train, X_test, y_train, y_test)


# 4. Reduced logistic regression model
feature_cols = ['mean radius', 
                'texture error',
                'worst radius',
                'worst compactness',
                'worst concavity']

X_train_reduced = X_train[feature_cols]
X_test_reduced = X_test[feature_cols]

reduced_model = LogisticRegression(solver='liblinear')
reduced_model.fit(X_train_reduced, y_train)

save_to_database(2, 'Reduced model', 'regression.sqlite', reduced_model, X_train_reduced, X_test_reduced, y_train, y_test)

# 5. Logistic regression model with L1 penalty
penalized_model = LogisticRegression(solver='liblinear', penalty='l1', random_state=87, max_iter=150)
penalized_model.fit(X_train, y_train)

save_to_database(3, 'L1 penalty model', 'regression.sqlite', penalized_model, X_train, X_test, y_train, y_test)


# Part C
query = '''SELECT id FROM model_results ORDER BY test_score DESC LIMIT 1'''
best_model_id = cursor.execute(query).fetchall()
query = '''SELECT MAX(test_score) FROM model_results '''
best_validation_score = cursor.execute(query).fetchall()
print("Best model id: ", best_model_id[0][0])
print("Best validation score: ", best_validation_score[0][0])


query = '''SELECT feature_name, value FROM model_coefs WHERE id = 3'''
result = cursor.execute(query).fetchall()
best_coefs = []
best_intercept = []

print("\nPrinting coefficients: ")
for x in result:
    print(x[0],':', x[1])
    
    if x[0] == 'intercept':
        best_intercept.append(x[1])
    else:
        best_coefs.append(x[1])

print()
test_model = LogisticRegression(solver='liblinear')
test_model.fit(X_train, y_train)

# Manually change fit parameters
test_model.coef_ = np.array([best_coefs])
test_model.intercept_ = np.array([best_intercept])

test_score = test_model.score(X_test, y_test)
print(f'Reproduced best validation score: {test_score}')

db.commit()
db.close()