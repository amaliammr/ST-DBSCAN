# -*- coding: utf-8 -*-
import math
from xlrd import *
Noise = 999999
Unmarked = 99999

rw = 100
#rw = 30
D = {}
C = {}
X = {}
T = {}
K = {}
Cluster_Label = 0
Minpts = math.log(rw)
#print(Minpts)
count = 0
stack = 0

print(Minpts)

def eps1(x, y):
    return math.sqrt((x.lat - y.lat)**2 + (x.lon - y.lon)**2)

def eps2(x, y):
    return math.sqrt((x.y1 - y.y1)**2 + (x.y2 - y.y2)**2)

def Retrieve_Neighbours(x, n):
    T = {}
    Y = {}
    count = 0
    for r in range(rw):
        if n == r:
            continue
        else:
            e1 = eps1(x, D[r])
            e2 = eps2(x, D[r])
            print(e1, e2)
            if(e1 < 0.1 and e2 < 3):
                Y[count] = Data(D[r].acode, D[r].lat, D[r].lon,  D[r].y1, D[r].y2, D[r].value)
                T[count] = r
                count += 1
                print(count)
    return Y,T
    
Z={}
Z[0] = Data(D[0].acode, D[0].lat, D[0].lon,  D[0].y1, D[0].y2, D[0].value)
print(Z[count].acode)

def push(x):
     Y = {}
     for j in range(count):
         Y[stack] = Data(D[T[j]].acode, D[T[j]].lat, D[T[j]].lon,  D[T[j]].y1, D[T[j]].y2, D[T[j]].value)
         K[stack] = T[j]
         stack = stack + 1

def pop():
    stack = stack - 1
    return Y[stack]

class Data:
    acode = 0.0
    lat = 0.0
    lon = 0.0
    y1 = 0.0
    y2 = 0.0
    value = 0.0
    clabel = Unmarked
    def __init__(self, acode, lat, lon, y1, y2, value):
        self.lat = lat
        self.lon = lon
        self.y1 = y1
        self.y2 = y2
        self.acode = acode
        self.value = value
        
for r in range(rw):
    r0 = float(csheet.cell(r,0).value)
    r1 = float(csheet.cell(r,3).value)
    r2 = float(csheet.cell(r,4).value)
    r3 = float(csheet.cell(r,1).value)
    r4 = float(csheet.cell(r,2).value)
    r5 = float(csheet.cell(r,5).value)
    D[r] = Data(r0, r1, r2, r3, r4, r5)

Y[0].value


r0= df['Obs'].as_matrix()
r1= df['Lat'].as_matrix()
r2= df['Longi'].as_matrix()
r3= new_zon
r4= new_mer
r5= df['AirTemp'].as_matrix()

#convert data into new data structure using class Data
rw = 100
for r in range(rw):
    D[r] = Data(r0[r], r1[r], r2[r], r3[r], r4[r], r5[r])
    
   
Cluster_label = 0
for r in range(rw):
    if D[r].clabel == Unmarked:
        X,T = Retrieve_Neighbours(D[r], r)

        if len(X) < Minpts:
            D[r].clabel = Noise
            #print("masuk sini ",count)
        else :
            #print("masuk sana")
            Cluster_label = Cluster_label + 1
            for j in range(len(X)):
                D[T[j]].clabel = Cluster_label
                print(D[T[j]].acode, D[T[j]].clabel)
                push(D[T[j]])

                while(stack < 0):
                    CurrentObj = pop()
                    X = Retrieve_Neighbors(CurrentObj, K[stack])

                    if len(X) < Minpts:
                        for j in range(len(X)):
                            if D[T[j]].clabel != Noise or D[T[j]].clabel == Unmarked:
                                D[T[j]].clabel = Cluster_label
                                push(D[T[j]])

import numpy as np
G = []                  
for i in range(100):
    g = [D[i].acode,D[i].lat,D[i].lon,D[i].y1,D[i].y2,D[i].value,D[i].clabel]
    g = np.asarray(g)
    G.append(g)

G = np.asarray(G)
                




                



    
