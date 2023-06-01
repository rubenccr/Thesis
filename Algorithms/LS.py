import sys
import time
import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import queue
import scipy
from scipy.optimize import least_squares




def equations(guess):
   x,y,z = guess
   
   return ((x - x1)**2 + (y - y1)**2 + (z - z1)**2 - (d1)**2,
           (x - x2)**2 + (y - y2)**2 + (z - z2)**2 - (d2)**2,
           (x - x3)**2 + (y - y3)**2 + (z - z3)**2 - (d3)**2
   )


def on_connect(client, userdata, flags, rc):
           if rc==0:
              print("Client Connected")
              global connected
              connected=True

           else:
              print("Client is not connected")
              
def on_range(client, userdata, message):
            (id,range,timestamp) = message.payload.decode("utf-8").split(",")
            # print("callack", id,range,timestamp)
            #global message_queue 
            message_queue.put((id,range,timestamp))
            
            
            

global message_queue 
global x1
global x2
global x3
global y1
global y2
global y3
global z1
global z2
global z3
global d1
global d2
global d3

message_queue = queue.Queue()
iguess = (30,10,0)

x1=19
x2=100
x3=42
y1=7
y2=12
y3=23
z1=0
z2=0
z3=0
d1=0
d2=0
d3=0

id1="default"
id2="default"
id3="default"            

client = mqtt.Client("LeastSquaresSub")
client.on_connect=on_connect
client.on_message=on_range
client.connect(sys.argv[1],1886)
client.subscribe("test/distances")
client.loop_start()




while(id1!=id2 or id1!=id3 or id2!=id3):
   
   if(message_queue.empty() or id1=="default" or id2=="default" or id3=="default"):
   
       time.sleep(3)
   
   
   else:
       (id,range,timestamp) = message_queue.get()
       id1=id
       (id,range,timestamp) = message_queue.get()
       id2=id
       (id,range,timestamp) = message_queue.get()
       id3=id


count1=0
count2=0
count3=0

while True:
    (id,range,timestamp) = message_queue.get()
    #print("main thread", id,range,timestamp)
    if(id==id1):
        d1=int(range)
        count1=1
    if(id==id2):
        d2=int(range)
        count2=1
    if(id==id3):
        d3=int(range)
        count3=1
        
    if(count1==1 and count2==1 and count3==1):
        ls = least_squares(equations, iguess)
        #tratar conteudo do ls e extrair apenas a info relevante aos Subs normais
        client.publish("test/lsquares",ls)
        count1=0
        count2=0
        count3=0
      
    


        




