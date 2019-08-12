import scipy

import numpy as np


#
# Import data as csv object in numpy
#

with open("zainab_data_marketing.csv") as fi:
	rows = fi.readlines()


#
# Parse rows
#

for i,row in enumerate(rows):

	# skip the header line
	if "company" in row[i]:
		continue

	# 

