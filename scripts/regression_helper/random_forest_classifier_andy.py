# Logistic Regression

#
# Importing the libraries
#
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#
# Import the Dataset
#

### Alternative 1 (prior to changes dated @2018-08-15:@0021) {{ 
#dataset = pd.read_csv("Social_Network_Ads.csv")
#X = dataset.iloc[:, [2, 3]].values
#y = dataset.iloc[:, 4].values
### }} Alternative 1 (prior to changes dated @2018-08-15:@0021) 


### Alternative 2(after changes dated @2018-08-15:@0022) {{
# Importing the dataset
dataset = pd.read_csv('../../data/zainab_data_marketing_actual.csv')   # @TODO:@1451: replace with delta vectors
X = dataset.iloc[:, 1:2].values    # independent variable OR 2008 salary

dataset = pd.read_csv('../../data/zainab_data_revenue_actual.csv')   # @TODO:@1634:@DEBUG(possible?) it might be better to create one variable for the marketing dataset and one for revenue so they are not overwriting one another (reference errors)
y = dataset.iloc[:, 3].values      # dependent variable OR 2009 salary
### }} Alternative 12(after changes dated @2018-08-15:@0022) 



## Importing the dataset
#dataset = pd.read_csv('../../data/zainab_data_marketing_actual.csv')   # @TODO:@1451: replace with delta vectors
#X = dataset.iloc[:, 1:2].values    # independent variable OR 2008 salary
#
#dataset = pd.read_csv('../../data/zainab_data_revenue_actual.csv')   # @TODO:@1451: replace with delta vectors
#y = dataset.iloc[:, 3].values      # dependent variable OR 2009 salary

#
# Split into training vs. test sets
#
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size = 0.2, 
                                                     random_state = 0 )
#
# Feature scaling
#
from sklearn.preprocessing import StandardScaler

sc_X = StandardScaler()

X_train = sc_X.fit_transform(X_train)
X_test = sc_X.fit_transform(X_test)

#
# Classifier (e.g. logistic regression, change to other if need be)
#
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, y_train)

#### ALTERNATIVE 2: this is what we want {{ 
## Fitting the Regression Model to the dataset
## Create your regressor here
#from sklearn.ensemble import RandomForestRegressor
#
#regressor = RandomForestRegressor(n_estimators = 10, random_state = 0)
#
#regressor.fit(X_train, y_train)
#
## Predicting a new result
#regressor.predict(6.5)
## }} ALTERNATIVE 2


#
# Predict results
#
y_pred = classifier.predict(X_test)

#
# Performance Statistics
#
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

#
# Visualisation of Performance
#
from matplotlib.colors import ListedColormap

colors = ListedColormap(["red","green"])
labels = ["Purchased'", "Purchased"]

X_set, y_set = X_train, y_train

X_age, X_salary = np.meshgrid( 
        np.arange(min(X_set[:, 0])-1, max(X_set[:, 0])+1, step = 0.01), 
        np.arange(min(X_set[:, 1])-1, max(X_set[:, 1])+1, step = 0.01) ) #..
        #..obtain two coordinate matrices, a pair of elements points to a region..
        #..in the age-salary feature space

X_plane = np.array([X_age.ravel(), X_salary.ravel()]).T # flatten the coordinate..
#..matrices, .ravel(), and transpose, .T, to obtain pairs of coordinates in..
#..feature space, so we can..:

y_plane = classifier.predict(X_plane) # ..predict Y-values corresponding to X features

# Draw decision boundary
plt.contourf(X_age, X_salary, 
             y_plane.reshape(X_age.shape), # "un-ravel" the y_plane
             alpha=0.5, 
             cmap=colors)

# Plot data points in feature space, colour according to Y-class (red, green)
for j in np.unique(y_set):
    plt.scatter( X_train[y_set==j, 0], X_train[y_set==j, 1], # all rows where y={0,1}
                 c=colors(j),      
                 label=labels[j])  # label for making a legend
plt.legend()
plt.title("Logistic Regression-based classification of training data")
plt.xlabel("Age")
plt.ylabel("Salary")
