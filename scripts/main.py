import scipy
import numpy as np
import csv
import pprint

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

