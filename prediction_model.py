import joblib
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import GridSearchCV

from constants import *

# Read data from csv
df = pd.read_csv("CO2 Emissions_Canada.csv")

# Remove the extra columns
extra_columns= ['Make', 'Model', 'Cylinders','Transmission', 'Fuel Consumption City (L/100 km)','Fuel Consumption Hwy (L/100 km)', 'Fuel Consumption Comb (mpg)']
data= df.drop(extra_columns,axis=1)

X = data.drop('CO2 Emissions(g/km)',axis=1)
y = data['CO2 Emissions(g/km)']
     
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

# Define columns
categorical_features = ['Vehicle Class', 'Fuel Type']
numerical_features = ['Engine Size(L)', 'Fuel Consumption Comb (L/100 km)']

# Create pipeline
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_features),
        ('cat', OneHotEncoder(sparse_output=False, handle_unknown='ignore'), categorical_features) # Update to use OneHotEncoder
    ])
# Create and run pipeline
pipe = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor())
])

# Fit pipeline
pipe.fit(X_train, y_train)

# Define the parameter grid,
param_grid = {
    'regressor__n_estimators': [100, 200, 300],
    'regressor__max_depth': [None, 5, 10],
    'regressor__min_samples_split': [2, 5, 10],
    'regressor__min_samples_leaf': [1, 2, 4]
}

# Create a GridSearchCV object
grid_search = GridSearchCV(pipe, param_grid=param_grid, cv=5)

# Fit the GridSearchCV object to your data
grid_search.fit(X, y)

# Get the best parameters and the best model
best_params = grid_search.best_params_
best_model = grid_search.best_estimator_

joblib.dump(pipe, MODEL_PKL_NAME)