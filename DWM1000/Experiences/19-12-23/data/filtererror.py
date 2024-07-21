import pandas as pd
import sys
import math
import csv


with open('errors.csv', 'w', newline='') as file:
 
 
 
 writer = csv.writer(file,delimiter=';')
 writer.writerow(["ID","Exp1 Avg. Error","Exp2 Avg. Error","Exp3 Avg. Error","Exp4 Avg. Error"])
 for i in range(1,4):
     erroexp = []
     for j in range(1,5):
      
         
 
           df = pd.read_csv("exp"+str(j)+"p"+str(i)+'.csv',sep=';')
           erroexp.append(df['Erro'].mean())
           
 
        
     
     writer.writerow(["Pub"+str(i),str(erroexp[0].round(2)),str(erroexp[1].round(2)) ,str(erroexp[2].round(2)),str(erroexp[3].round(2))]) 

file.close()
