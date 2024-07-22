import csv
import pandas as pd



df = pd.read_csv("pc3specificLS.csv",sep=';')


p5 = []
p6 = []
p7 = []
p9 = []

for k in range(0,len(df["Simple Range"])):

  aux = df["Simple Range"][k].split("'")
  
  if(len(aux)==7):
  
    if(aux[1].split(" ")[0]=="P6"):
      p6.append(aux[1].split(" ")[1])
    elif(aux[1].split(" ")[0]=="P5"):
      p5.append(aux[1].split(" ")[1])
    elif(aux[1].split(" ")[0]=="P7"):
      p7.append(aux[1].split(" ")[1])
    elif(aux[1].split(" ")[0]=="P9"):
      p9.append(aux[1].split(" ")[1])
      
    if(aux[3].split(" ")[0]=="P6"):
      p6.append(aux[3].split(" ")[1])
    elif(aux[3].split(" ")[0]=="P5"):
      p5.append(aux[3].split(" ")[1])
    elif(aux[3].split(" ")[0]=="P7"):
      p7.append(aux[3].split(" ")[1])
    elif(aux[3].split(" ")[0]=="P9"):
      p9.append(aux[3].split(" ")[1])
    
    if(aux[5].split(" ")[0]=="P6"):
      p6.append(aux[5].split(" ")[1])
    elif(aux[5].split(" ")[0]=="P5"):
      p5.append(aux[5].split(" ")[1])
    elif(aux[5].split(" ")[0]=="P7"):
      p7.append(aux[5].split(" ")[1])
    elif(aux[5].split(" ")[0]=="P9"):
      p9.append(aux[5].split(" ")[1])  
          
  else:
    
    if(aux[1].split(" ")[0]=="P6"):
      p6.append(aux[1].split(" ")[1])
    elif(aux[1].split(" ")[0]=="P5"):
      p5.append(aux[1].split(" ")[1])
    elif(aux[1].split(" ")[0]=="P7"):
      p7.append(aux[1].split(" ")[1])
    elif(aux[1].split(" ")[0]=="P9"):
      p9.append(aux[1].split(" ")[1])
      
    if(aux[3].split(" ")[0]=="P6"):
      p6.append(aux[3].split(" ")[1])
    elif(aux[3].split(" ")[0]=="P5"):
      p5.append(aux[3].split(" ")[1])
    elif(aux[3].split(" ")[0]=="P7"):
      p7.append(aux[3].split(" ")[1])
    elif(aux[3].split(" ")[0]=="P9"):
      p9.append(aux[3].split(" ")[1])
    
    if(aux[5].split(" ")[0]=="P6"):
      p6.append(aux[5].split(" ")[1])
    elif(aux[5].split(" ")[0]=="P5"):
      p5.append(aux[5].split(" ")[1])
    elif(aux[5].split(" ")[0]=="P7"):
      p7.append(aux[5].split(" ")[1])
    elif(aux[5].split(" ")[0]=="P9"):
      p9.append(aux[5].split(" ")[1])
      
      
    if(aux[7].split(" ")[0]=="P6"):
      p6.append(aux[7].split(" ")[1])
    elif(aux[7].split(" ")[0]=="P5"):
      p5.append(aux[7].split(" ")[1])
    elif(aux[7].split(" ")[0]=="P7"):
      p7.append(aux[7].split(" ")[1])
    elif(aux[7].split(" ")[0]=="P9"):
      p9.append(aux[7].split(" ")[1])  
     
  
df1 = pd.DataFrame(p5, columns=["P5"])
df2 = pd.DataFrame(p6, columns=["P6"])
df3 = pd.DataFrame(p7, columns=["P7"])
df4 = pd.DataFrame(p9, columns=["P9"]) 

df1.to_csv('p5.csv', index=False)
df2.to_csv('p6.csv', index=False)
df3.to_csv('p7.csv', index=False)
df4.to_csv('p9.csv', index=False)
  
                    
