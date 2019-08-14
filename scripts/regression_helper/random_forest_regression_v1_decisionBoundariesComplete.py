# Regression Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('../../data/zainab_data_marketing_actual.csv')   # @TODO:@1451: replace with delta vectors
X = dataset.iloc[:, 1:2].values    # independent variable OR 2008 salary

revenue_dataset = pd.read_csv('../../data/zainab_data_revenue_actual.csv')   # @TODO:@1634:@DEBUG(possible?) it might be better to create one variable for the marketing dataset and one for revenue so they are not overwriting one another (reference errors)
y = dataset.iloc[:, 3].values      # dependent variable OR 2009 salary

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)

# Fitting the Regression Model to the dataset
# Create your regressor here
from sklearn.ensemble import RandomForestRegressor

regressor = RandomForestRegressor(n_estimators = 10, random_state = 0)

regressor.fit(X, y)

# Predicting a new result
regressor.predict(6.5)

# Visualising the Regression results
plt.scatter(X, y, color="r")

X_grid = np.arange(min(X), max(X), step=0.01)
X_grid = X_grid.reshape(len(X_grid), 1) # reshape into array

plt.plot(X_grid, regressor.predict(X_grid), color="b")


plt.title("Random Forest Regression")

plt.xlabel("Level")

plt.ylabel("Salary")