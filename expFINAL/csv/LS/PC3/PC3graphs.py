from math import sqrt
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
temp4 = []

df1 = pd.read_csv("p5.csv",sep=';')
df2 = pd.read_csv("p6.csv",sep=';')
df3 = pd.read_csv("p7.csv",sep=';')
df4 = pd.read_csv("p9.csv",sep=';')



plt.hist(df1["P5"],bins=20, color='skyblue', edgecolor='black')
plt.xlabel("Distance")
plt.ylabel("Number of Values")
plt.title("Distance to tag from Anchor P5")
plt.show()

plt.hist(df2["P6"],bins=20, color='skyblue', edgecolor='black')
plt.xlabel("Distance")
plt.ylabel("Number of Values")
plt.title("Distance to tag from Anchor P6")
plt.show() 

plt.hist(df3["P7"],bins=20, color='skyblue', edgecolor='black')
plt.xlabel("Distance")
plt.ylabel("Number of Values")
plt.title("Distance to tag from Anchor P7")
plt.show() 

plt.hist(df4["P9"],bins=20, color='skyblue', edgecolor='black')
plt.xlabel("Distance")
plt.ylabel("Number of Values")
plt.title("Distance to tag from Anchor P9")
plt.show() 
