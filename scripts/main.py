## 
## Imports (dependencies, see: pip) 
## 

from scipy import stats
import numpy as np
import csv
import pprint
import copy
from matplotlib import pyplot

### 
### Functions (modules)
### 


###
### Main
###

#
# NOTE: indent using spaces, one indent = 4 * spaces
#

#
# Import data as csv object in numpy
#
with open("../data/zainab_data_marketing.csv") as fi:
    rows = list(csv.reader(fi, delimiter=','))

#
# Parse rows as integers, only keeping numerical data
#

#pprint.pprint(rows)

data = {}  # dict will store keys as companies and values as sub-dictionaries, each sub dict will be a different column in the original data, e.g. "2008_marketing_in_mil"

for i,row in enumerate(rows):

    # skip headers
    if i==0: 
        continue    

    print(row)

    # convert all the cols of each row of data into correct datatypes
    company_name = str(row[0])  # e.g. "Company_1"
    money_2008 = float(row[1])
    money_2009 = float(row[2])
    delta_2008_to_2009 = money_2008 - money_2009

    # @debugging
    print("\t"+str(company_name))
    print("\t"+str(money_2008))
    print("\t"+str(money_2009))
    print("\t"+str(delta_2008_to_2009))

    try:
        # Accumulate: data via appending to pre-instantiated keys for a given company (superkey)
        data[company_name]["money 2008"].append(money_2008)  
        data[company_name]["money 2009"].append(money_2009)
        data[company_name]["delta"].append(delta_2008_to_2009)

    except KeyError:
        # Try: keep adding subdicts (as values) to the company name (as key), else: initialize dict keys and values as subdicts 
        data[company_name] = {  "money 2008":[money_2008],\
                                "money 2009":[money_2009],\
                                "delta":[delta_2008_to_2009]} # delta = money(2008) - money(2009)



#
# Construct the numpy array from the dict datastructure above (so we can input to the wilcoxon rank test and visual functions to get p-value outputs and plotting outputs)
#

n_companies = copy.copy(i)

# build lists from the dicts above

company_names_vec = data.keys()  # since each key maps to a name of a company as str
money_2008_vec = [data[i]["money 2008"] for i in company_names_vec] # e.g. [[-1944.0], [1493.0], [2430.0], [-1247.0], [-1323.0], [-2007.0], [-2408.0], [-2248.0], [-2402.0], [-1266.0], [901.0], [-3384.0], [1382.0], [-1666.0], [-1653.0], [1087.0], [-3306.0], [-2070.0], [-1441.0], [560.0], [-452.0], [348.0], [273.0], [2142.0], [-1921.0], [-641.0], [-2305.0], [2875.0], [-2024.0], [-1784.0]]
money_2009_vec = [data[i]["money 2009"] for i in company_names_vec]
delta_2008_to_2009_vec = [data[i]["delta"] for i in company_names_vec]

# convert python lists into numpy arrays (1D vector arrays, technically 2D since we need to remove the nested and unecessary list wrappers around each element)

company_names_arr = np.array(company_names_vec)
money_2008_arr = np.array(money_2008_vec)
money_2009_arr = np.array(money_2009_vec)
delta_2008_to_2009_arr = np.array(delta_2008_to_2009_vec)

# flatten the lists, since each element i in each and every list (except for company_names_arr) here is a single-element list, e.g. [-1784.0], so flatten to remove unecessary list wrapper 

company_names_arr = np.array(company_names_vec)
money_2008_arr = money_2008_arr.flatten()
money_2009_arr = money_2009_arr.flatten()
delta_2008_to_2009_arr = delta_2008_to_2009_arr.flatten()

##
## STATISTICAL TESTING
##

#
# Wilcoxon signed rank test, input = money_2008_arr, money_2009_arr --> output = p-value
#

# USAGE: scipy.stats.wilcoxon(x, y=None, zero_method='wilcox', correction=False)  // see: https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.wilcoxon.html

# TEST1: Running the test on default settings

T, p = stats.wilcoxon(x=money_2008_arr, y=money_2009_arr, zero_method='wilcox', correction=False)

print((T,p)) # T = 121.0, p = 0.02182... // NOTE: the p-value in the dummy set is significant!? Hilarious..

# TEST2: Running the test on the delta array (where we specify the difference vector as x, only)

T, p = stats.wilcoxon(x=delta_2008_to_2009_arr, y=None, zero_method='wilcox', correction=False)

print((T,p)) # T = 121.0, p = 0.02182... // NOTE: Brilliant! we obtain exactly the same T and p values, which confirms the behaviour of the wilcoxon package is entirely consistent.


##
## Plotting the data
##

#
# Histograms: a first glance at our spending data, one for 2008 other for 2009 // see: https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.wilcoxon.html
#

# @DEBUGGING:@TODO:@2019-08-13: we get error: "ImportError: No module named _tkinter, please install the python-tk package", so we need to install python-tk via pip, USAGE: "sudo pip install python-tk"

import random
import numpy
from matplotlib import pyplot

x = [random.gauss(3,1) for _ in range(400)]
y = [random.gauss(4,2) for _ in range(400)]

bins = numpy.linspace(-10, 10, 100)

pyplot.hist(x, bins, alpha=0.5, label='x')
pyplot.hist(y, bins, alpha=0.5, label='y')
pyplot.legend(loc='upper right')
pyplot.show()
