import pandas as pd
import sys
import math
import csv

var = sys.argv[1]
#print(s[1])

   
 

    


   
 
#rdistance = math.sqrt((float(gtx)-float(nodex))**2 + (float(gty)-float(nodey))**2)

#print("avgerrorLSX: " +str(avgerrorLSX.round(2)))
#print("avgerrorLSY: " +str(avgerrorLSY.round(2)))
#print("avgerrordwmx: "+str(avgerrordwmx.round(2)))
#print("avgerrordwmy: "+str(avgerrordwmy.round(2)))

with open('results.csv', 'w', newline='') as file:
 writer = csv.writer(file,delimiter=';')
 writer.writerow(["Control Point","Avg. Error LS","STD. LS","Variance LS","Avg. Error DWM","STD. DWM","Variance DWM"])
 for i in range(1,int(var)+1):
   
     if(i==7):
        writer.writerow(["pc"+str(i),"no data","no data"])
     
     else:
       df = pd.read_csv("pc"+str(i)+"LS.csv",sep=';')
       avgerrorLS = df['ERRO LS'].mean()
       avgerrordwm = df['ERRO_DWM'].mean()
       desvioLS = df['ERRO LS'].std()
       desvioDWM = df['ERRO_DWM'].std() 
       varLS = df['ERRO LS'].var()
       varDWM = df['ERRO_DWM'].var()
       writer.writerow(["pc"+str(i),str(avgerrorLS.round(2)),str(desvioLS.round(2)),str(varLS.round(2)),str(avgerrordwm.round(2)),str(desvioDWM.round(2)),str(varDWM.round(2))])
     



file.close()
