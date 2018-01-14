# ST-DBSCAN
Implements the ST-DBSCAN algorithm to find clusters in a spatial-temporal database

To use the code one should provide 5 variables which will be stored in r0-r5

Each value can be stored in array. The value will then be converted to a new data structure called Data

r0 = id of each row (this will not be included in calculation of cluster)

r1 = latitude

r2 = longitude

r3 = y1 = other value that can be calculated as distance along with y2

r4 = y2 = other value that can be calculated as distance along with y1

r5 = value = other value that will not be calculated for clustering process 

lattitude and longitude distance will be calculated using euclidean distance using function eps1

y1 and y2 also will be calculated using euclidean distance using function eps2




