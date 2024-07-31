import pandas as pd
import csv
from math import sqrt

with open("expstats.csv", 'w', newline='') as f:
   writer = csv.writer(f,delimiter=';')
   writer.writerow(["Avg.Error LS","STD. LS"])
   df = pd.read_csv('logLS_2024-01-31_12:15:10.csv',sep=';')
   gtX = 1
   gtY = 1
   LS = []
   #print(len(df["X"]))
   df1 = pd.DataFrame()
   for i in range(0,len(df["X"])):
   
     erroxls = float(gtX) - float(df["X"][i])  
     erroyls = float(gtY) - float(df["Y"][i]) 
     errols = sqrt((erroxls*erroxls)+(erroyls*erroyls))
     LS.append(round(errols,2))
    
     
   df1["ls"] = LS
   als = df1["ls"].mean()
   std = df1["ls"].std()
   writer.writerow([round(als,2),round(std,2)])  

f.close()   
