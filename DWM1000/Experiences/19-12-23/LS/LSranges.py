from math import sqrt
from scipy.optimize import least_squares
import pandas as pd
import csv
global ANCHORS 
ANCHORS = {}


def equations_v2 ( guess, id,ANCHORS ):
    x, y , z = guess
   
    return [
          (x - a["x"]) ** 2 
        + (y - a["y"]) ** 2 
        + (z - a["z"]) ** 2 
        - (a["range"]) ** 2 for a in ANCHORS[id].values()
    ]

j=1
iguess = (0.0,0.0,0.0)
ANCHORS[id] = {} 

expl = [(2,4),(1,1),(3,6),(3,1)]

for i in range(1,5):
   
   j=1
   df = pd.read_csv("exp"+str(i)+"p"+str(j)+'.csv',sep=';')
   j+=1
   df2 = pd.read_csv("exp"+str(i)+"p"+str(j)+'.csv',sep=';')
   j+=1
   df3 = pd.read_csv("exp"+str(i)+"p"+str(j)+'.csv',sep=';')
   minsize = min(df['Range'].size,df['Range'].size, df2['Range'].size, df3['Range'].size)
  
   with open("exp"+str(i)+"LS.csv", 'w', newline='') as f:
     writer = csv.writer(f,delimiter=';')
     writer.writerow(["LS_X","LS_Y","LS_Z","ERRO_LS"])
     for k in range(minsize):

        aid =[df['ID'][0],df2['ID'][0],df3['ID'][0]]
        ax = [float(df['X'][0]),float(df2['X'][0]),float(df3['X'][0])]
        ay = [float(df['Y'][0]),float(df2['Y'][0]),float(df3['Y'][0])]
        arange = [float(df['Range'][k]),float(df2['Range'][k]),float(df3['Range'][k])]
        ANCHORS[id] = {}
        for n in range(0,3):       
          
          ANCHORS[id][aid[n]] = {
          "x": ax[n], 
          "y": ay[n], 
          "z": 0.0,
          "range": arange[n]
          }
          #print(ANCHORS)
        
        results = least_squares(equations_v2, iguess, args=(id,ANCHORS))
        erroxls = float(expl[i-1][0]) - float(results.x[0])
        erroyls = float(expl[i-1][1]) - float(results.x[1]) 
        errols = sqrt((erroxls*erroxls)+(erroyls*erroyls))
        writer.writerow([results.x[0].round(2),results.x[1].round(2),results.x[2].round(2),round(errols,2)])
     
   f.close()    

