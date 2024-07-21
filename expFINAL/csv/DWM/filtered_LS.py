import sys
import time
import queue
import scipy
import csv
from math import sqrt
from scipy.optimize import least_squares

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




def test_ls():
  global ANCHORS  
  ANCHORS_TEST = {}
  ANCHORS_TEST[0] = {
    "pub1": {
        "id": 0, 
        "x": 5.0,
        "y": 0.0,
        "z": 0.0,
        "range": 0
    }, 
    "pub2": {
        "id": 0,
        "x": 0.0,
        "y": 5.0,
        "z": 0.0,
        "range": 7

    },
    "pub3": {
        "id": 0,
        "x": 0.0,
        "y": 0.0,
        "z": 0.0,
        "range": 5
    },
    "pub4": {
        "id": 0,
        "x": 5.0,
        "y": 5.0,
        "z": 0.0,
        "range": 5
    },
    "pub5": {
        "id": 0,
        "x": 5.0,
        "y": 6.0,
        "z": 0.0,
        "range": 6
    }
  }
  iguess = (0.0,0.0,0.0)
  ANCHORS = ANCHORS_TEST
  results = least_squares(equations_v2, iguess,args=(0,ANCHORS))
  print(results.x)

#test_ls()

#sys.exit(0) 

def parser(element):
  #print(element)
  aux = element.split('[')
  #print(aux)
  px = aux[0]
        
  aux2 = aux[1].split(',')
  #print(aux2)
  x = aux2[0]
  y = aux2[1]
  z = aux2[2].split(']')[0]
  r = aux2[2].split('=')[1] 
  #print(x)
  #print(y)
  #print(z)
  #print(r)  
  return [px,float(x),float(y),float(z),float(r)]  
  
  
  
     
         
       
         
flag = False  
var = input("Input the name of the file you want to parse: ")
var2 = input("Input ground truth values:  ")
gtx = var2.split(",")[0]
gty = var2.split(",")[1]
with open(var+".csv", 'r', newline='') as f:
  
  with open(var+'LS.csv', 'w', newline='') as file:
    
    writer = csv.writer(file,delimiter=';')
    writer.writerow(["Anchor/Range","Anchor/Range","Anchor/Range", "Anchor/Range","LS_Estimated","DWM_Estimated","Timestamp","X_DWM","Y_DWM","X_LS","Y_LS","GROUND_X","GROUND_Y","ERRO_X_LS","ERRO_Y_LS","ERRO_X_DWM","ERRO_Y_DWM","ERRO LS","ERRO_DWM"])
    lines = csv.reader(f, delimiter=';', quotechar='|')
    iguess = (0.0,0.0,0.0) 
    
    for l in lines:
     
      ANCHORS[id] = {}
      if(flag==True):
      
        for element in l:
           
           #print("this is element: %s "%element)
           if(element=="null"):
              continue
           elif(element[0]=="["):
              break 
           else:
              #print(element)
              #print(parser(element))
              (aid, ax, ay, az, arange) =  parser(element)   
              #print(aid)
              #print(ax)
              #print(ay)
              #print(az)
              #print(arange)
          
              
              ANCHORS[id][aid] = {
              "x": ax, 
              "y": ay, 
              "z": az,
              "range": arange
              }
              #print(ANCHORS)

             
        results = least_squares(equations_v2, iguess, args=(id,ANCHORS))
       
        rlist = [results.x[0].round(2),results.x[1].round(2),results.x[2].round(2)]
        dwm = l[4].split(",")
        erroxls = float(gtx) - float(results.x[0].round(2))
        erroyls = float(gty) - float(results.x[1].round(2))
        erroxdwm = float(gtx) - float(dwm[0].split("[")[1])
        erroydwm = float(gty) - float(dwm[1])
        errols = sqrt((erroxls*erroxls)+(erroyls*erroyls))
        errodwm = sqrt((erroxdwm*erroxdwm)+(erroydwm*erroydwm))
        writer.writerow([l[0],l[1],l[2],l[3],rlist,l[4],l[5],dwm[0].split("[")[1],dwm[1],results.x[0].round(2),results.x[1].round(2),gtx,gty,round(erroxls,2),round(erroyls,2),round(erroxdwm,2),round(erroydwm,2),round(errols,2),round(errodwm,2)])
      flag=True
  file.close()
f.close()


        


