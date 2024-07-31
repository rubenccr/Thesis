from math import sqrt
import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.ticker import (MultipleLocator, 
                               FormatStrFormatter, 
                               AutoMinorLocator) 



temp1 = []
temp2 = []
temp3 = []
temp4 = []

df1 = pd.read_csv("p5e.csv",sep=';')
df2 = pd.read_csv("p6e.csv",sep=';')
df3 = pd.read_csv("p7e.csv",sep=';')
df4 = pd.read_csv("p9e.csv",sep=';')







plt.hist(df1["Erro"], bins=90, range=[0,5], color='skyblue', edgecolor='black')
plt.xscale('log')
plt.ylim(0,200)
plt.xlabel("Error relative to ground truth distance.")
plt.ylabel("Number of Values")
plt.title("Error in distance to tag from Anchor P5")
plt.show()

plt.hist(df2["Erro"], bins=75, range=[0,5], color='skyblue', edgecolor='black')
plt.xscale('log')
plt.ylim(0,200)
plt.xlabel("Error relative to ground truth distance.")
plt.ylabel("Number of Values")
plt.title("Error in distance to tag from Anchor P6")
plt.show() 

plt.hist(df3["Erro"], bins=75, range=[0,5], color='skyblue', edgecolor='black')
plt.xscale('log')
plt.ylim(0,200)
plt.xlabel("Error relative to ground truth distance.")
plt.ylabel("Number of Values")
plt.title("Error in distance to tag from Anchor P7")
plt.show() 


plt.hist(df4["Erro"], bins=75, range=[0,5], color='skyblue', edgecolor='black')
plt.xscale('log')
plt.ylim(0,200)
plt.xlabel("Error relative to ground truth distance.")
plt.ylabel("Number of Values")
plt.title("Error in distance to tag from Anchor P9")
plt.show() 
