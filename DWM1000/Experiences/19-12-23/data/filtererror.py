import pandas as pd
import sys
import math
import csv


with open('errors.csv', 'w', newline='') as file:
 
 
 
 writer = csv.writer(file,delimiter=';')
 writer.writerow(["ID","E1 Error","E1 STD.","E2 Error","E2 STD.","E3 Error","E3 STD.","E4 Error","E4 STD."])
 for i in range(1,4):
     erroexp = []
     errostd = []
     for j in range(1,5):
      
         
 
           df = pd.read_csv("exp"+str(j)+"p"+str(i)+'.csv',sep=';')
           erroexp.append(df['Erro'].mean())
           errostd.append(df['Erro'].std())
 
     writer.writerow(["Pub"+str(i),str(erroexp[0].round(2)),str(errostd[0].round(2)),str(erroexp[1].round(2)),str(errostd[1].round(2)),str(erroexp[2].round(2)),str(errostd[2].round(2)),str(erroexp[3].round(2)),str(errostd[3].round(2))]) 
 
file.close()
