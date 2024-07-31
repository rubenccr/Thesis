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

var2 = "8.30,20.40"
gtx = var2.split(",")[0]
gty = var2.split(",")[1]
with open("pc3.csv", 'r', newline='') as f:
  
  with open('3comb.csv', 'w', newline='') as file:
    
    writer = csv.writer(file,delimiter=';')
    writer.writerow(["P5\P6\P9 LS","Using"])
    lines = csv.reader(f, delimiter=';', quotechar='|')
    iguess = (0.0,0.0,0.0) 
    
    for l in lines:
      temp=[]
      
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
             
              if(aid!="P9"):
                temp.append(aid)
                ANCHORS[id][aid] = {
                "x": ax, 
                "y": ay, 
                "z": az,
                "range": arange
                }
              
              
                #print(ANCHORS)

        
        
        if(len(temp)==3):     
        
          results = least_squares(equations_v2, iguess, args=(id,ANCHORS))       
          rlist = [results.x[0].round(2),results.x[1].round(2),results.x[2].round(2)]
          erroxls = float(gtx) - float(results.x[0].round(2))
          erroyls = float(gty) - float(results.x[1].round(2))
          errols = round(sqrt((erroxls*erroxls)+(erroyls*erroyls)),2)
          writer.writerow([errols,temp])
      flag=True
  file.close()
f.close()


#x569,x679,x579
        


