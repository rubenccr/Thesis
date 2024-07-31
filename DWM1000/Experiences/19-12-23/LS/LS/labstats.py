import pandas as pd
import sys
import math
import csv

#insert number of files
var = sys.argv[1]
#print(s[1])



with open('labdata.csv', 'w', newline='') as file:
 writer = csv.writer(file,delimiter=';')
 writer.writerow(["Experience","Avg. Error LS","STD. LS"])
 for i in range(1,int(var)+1):
   
 
       df = pd.read_csv("exp"+str(i)+"LS.csv",sep=';')
       avgerrorLS = df['ERRO_LS'].mean()
       desvioLS = df['ERRO_LS'].std()
       
       writer.writerow([str(i),str(avgerrorLS.round(2)),str(desvioLS.round(2))])
     



file.close()
