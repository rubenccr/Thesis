import sys
import re


s = sys.argv[1]
s1 = s.split(".")
f2 = open(s1[0]+".csv", "a")
f = open(s, 'r')
text = f.readlines()
f2.write("ID,Range,Timestamp\n")
count = 0
count2 = 0
for line in text:
    
    l = line.split("||")
    #print(l)
    aux1=l[1].split("=")
    if(len(aux1)>1):
       aux2=aux1[1].split(" ")
       count += 1
       #print(aux2)
       if(count>1):
         #print(aux2[0])
         distance=aux2[0]
         timestamp=l[0]
         f2.write("D62A" + "," + distance+ "," + timestamp +'\n')

f.close()
f2.close()
