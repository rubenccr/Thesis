import csv
import json

def parse(s):
  
  parsedstr = ["","",""]
  aux = s.split(" ")
  parsedstr[2]=aux[2]
  aux2 = aux[1].split("}\\")
  a16 = aux2[0].split("\"a16\":")
  a16 = a16[1].split(",")
  a16 = a16[0].split("\"")
  parsedstr[0] = a16[1]

  d = aux2[0].split("\"D\":")
  d = d[1].split(",")
  d = d[0].split("\'")
  parsedstr[1] = d[0]
 
  return parsedstr




var = input("Input the name of the file you want to parse: ")

with open(var+".txt",'r') as f:
  
  with open(var+'.csv', 'w', newline='') as file:
    
    writer = csv.writer(file)
    writer.writerow(["TagID", "Distance", "Timestamp"])
    lines = f.readline()
   
    while lines != "":
      
      lines = f.readline()
      if lines == "":
            break
      parsed = parse(lines)
      writer.writerow([parsed[0], parsed[1], parsed[2]])

  file.close()

f.close()



