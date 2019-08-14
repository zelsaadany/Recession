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
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 0)

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

regressor.fit(X_train, y_train)

# Predicting a new result
regressor.predict(6.5)


#
# # @ALTERNATIVE 1: @DONE:@1638:save this plot for the raw data, which works, refer to *_v1*.py for a working version {{  
#
## Visualising the Regression results
#plt.scatter(X, y, color="r")
#X_grid = np.arange(min(X), max(X), step=0.01)  # @DONE:@1638:save this plot for the raw data, which works, refer to *_v1*.py for a working version
#X_grid = X_grid.reshape(len(X_grid), 1) # reshape into array  # @DONE:@1638:save this plot for the raw data, which works, refer to *_v1*.py for a working version
#plt.plot(X_grid, regressor.predict(X_grid), color="b")  # @DONE:@1638:save this plot for the raw data, which works, refer to *_v1*.py for a working version
#
# }} # @DONE:@1638:save this plot for the raw data, which works, refer to *_v1*.py for a working version
#

def get_index_of_max_value(vec,n):
    """ find the maximum value of a vector and returns it's index """
    
    vec = list(vec)
    
    n_iterations_vec = [i for i in range(0,n,1)]
    
    max_collection = []
    
    for iteration in n_iterations_vec:
        
        max_vec = [(a,b==max(vec)) for (a,b) in enumerate(vec)]
    
        for i,j in max_vec:
            
            if j==np.array([ True], dtype=bool):
                outlier = vec[i]
                max_collection.append(outlier)
                vec.remove(outlier)
    return max_collection

def get_index_of_min_value(vec,n):
    """ find the maximum value of a vector and returns it's index """
    
    vec = list(vec)
    
    n_iterations_vec = [i for i in range(0,n,1)]
    
    max_collection = []
    
    for iteration in n_iterations_vec:
        
        max_vec = [(a,b==min(vec)) for (a,b) in enumerate(vec)]
    
        for i,j in max_vec:
            
            if j==np.array([ True], dtype=bool):
                outlier = vec[i]
                max_collection.append(outlier)
                vec.remove(outlier)
    return max_collection

#
# Remove the n-biggest outliers from the dataset
#


#
# # @ALTERNATIVE 2: @TODO:@1641: try getting it to use X-train and Y-train instead of raw data \X and Y {{  
#
plt.scatter(X_train, y_train, color="r")
X_grid = np.arange(min(X_train), max(X_train), step=0.01)  # @TODO:@1641: try getting it to use X-train and Y-train instead of raw data \X and Y
X_grid = X_grid.reshape(len(X_grid), 1) # reshape into array  # @TODO:@1641: try getting it to use X-train and Y-train instead of raw data \X and Y
plt.plot(X_grid, regressor.predict(X_grid), color="b")  # @TODO:@1641: try getting it to use X-train and Y-train instead of raw data \X and Y

#
# }} # @ALTERNATIVE 2: @TODO:@1641: try getting it to use X-train and Y-train instead of raw data \X and Y {{
#

plt.title("Random Forest Regression")
plt.xlabel("2008 (?)")

plt.ylabel("2009 (?)")