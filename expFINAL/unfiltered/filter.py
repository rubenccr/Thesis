import csv
import json

def parse(s):
  
  parsedstr = ["","","","","",""]
  splitedline = s.split(" ")
  i=0
  
  #print(len(splitedline))
  if(len(splitedline)==7):
     
     if(splitedline[5][0]=='P'):
          return "null"
     
     parsedstr[5] = splitedline[1].split("]")[0]
    
     for element in splitedline:
         
        
         
         if(i==3):
           
           parsedstr[i] ="null"
           i+=1
         
         if(element[0]=='P'):
            
            
            parsedstr[i] = element
            i+=1
            
         if(element[0]=='e'):
            aux3 = element.split('t')
            aux4 = aux3[1]
            aux5 = aux4.split(',')
            parsedstr[i]=aux5[0]+','+aux5[1]+','+aux5[2]+']'
            i+=1
            
         
         
  elif(len(splitedline)==8):
      
      
      parsedstr[5] = splitedline[1].split("]")[0]   
      for element in splitedline:             
         
         if(element[0]=='P'):
            
            
            parsedstr[i] = element
            #print(i)
            i+=1
            
         if(element[0]=='e'):
            aux3 = element.split('t')
            aux4 = aux3[1]
            aux5 = aux4.split(',')
            parsedstr[i]=aux5[0]+','+aux5[1]+','+aux5[2]+']'
            i+=1
         
         
            
  else:
               
        return "null"
            
  #print(parsedstr)
  return parsedstr




var = input("Input the name of the file you want to parse: ")

with open(var+".txt",'r') as f:
  
  with open(var+'.csv', 'w', newline='') as file:
    
    writer = csv.writer(file,delimiter=";")
    writer.writerow(["Anchor/Range","Anchor/Range","Anchor/Range", "Anchor/Range","Estimated","Timestamp"])
    lines = f.readline()
   
    while lines != "":
      
      lines = f.readline()
      #print(lines)            
      parsed = parse(lines)
      
      if(parsed=="null"):
         #print("discard line")
         continue
         
      else:
          #print("writing line")
          writer.writerow([parsed[0], parsed[1], parsed[2],parsed[3],parsed[4],parsed[5]])

  file.close()

f.close()



