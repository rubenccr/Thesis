from math import sqrt
from scipy.optimize import least_squares
import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import (MultipleLocator, 
                               FormatStrFormatter, 
                               AutoMinorLocator) 



temp1 = []
temp2 = []
temp3 = []

df1 = pd.read_csv("exp1p1.csv",sep=';')
for i in range(0,len(df1["Range"])):
  temp1.append(i)

df2 = pd.read_csv("exp1p2.csv",sep=';')
for i in range(0,len(df2["Range"])):
  temp2.append(i)

df3 = pd.read_csv("exp1p3.csv",sep=';')
for i in range(0,len(df3["Range"])):
  temp3.append(i)



x = np.array(temp1)
y = np.array(df1["Range"])

fig, ax = plt.subplots() 
  
ax.set_title('P1 Ranges') 
  
ax.set_ylabel('RANGES') 
ax.set_xlabel('READINGS') 
  
 
ax.yaxis.set_major_locator(MultipleLocator(base=0.05)) 
ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

 
ax.scatter(x, y) 
ax.set_ylim(ymin=1.70,ymax=2.10)
plt.show()  


x = np.array(temp2)
y = np.array(df2["Range"])

fig, ax = plt.subplots() 
  
ax.set_title('P2 Ranges') 
  
ax.set_ylabel('RANGES') 
ax.set_xlabel('READINGS') 
  
 
ax.yaxis.set_major_locator(MultipleLocator(base=0.05)) 
ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
  
ax.scatter(x, y) 
ax.set_ylim(ymin=1.60,ymax=2.10) 
plt.show()  



x = np.array(temp3)
y = np.array(df3["Range"])

fig, ax = plt.subplots() 
  
ax.set_title('P3 Ranges') 
  
ax.set_ylabel('RANGES') 
ax.set_xlabel('READINGS') 
  
 
ax.yaxis.set_major_locator(MultipleLocator(base=0.05)) 
ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
  
ax.scatter(x, y) 
plt.show()  

