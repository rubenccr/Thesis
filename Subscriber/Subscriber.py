import sys
import time
import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import queue
import scipy
from scipy.optimize import least_squares




def equations(guess):
   x,y,z,r = guess
   
   return ((x - x1)**2 + (y - y1)**2 + (z - z1)**2 - (d1 - r )**2,
           (x - x2)**2 + (y - y2)**2 + (z - z2)**2 - (d2 - r )**2,
           (x - x3)**2 + (y - y3)**2 + (z - z3)**2 - (d3 - r )**2
   )



global message_queue 
message_queue = queue.Queue()
iguess = (30,10,0,0)

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
            global message_queue 
            message_queue.put((id,range,timestamp))
            
            
            

 
            

client = mqtt.Client("Sub")
client.on_connect=on_connect
client.on_message=on_range
client.connect(sys.argv[1],1886)
client.subscribe("test/distances")
client.loop_start()

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

(id,range,timestamp) = message_queue.get()
id1=id
(id,range,timestamp) = message_queue.get()
id2=id
(id,range,timestamp) = message_queue.get()
id3=id
count1=0
count2=0
count3=0
se="42"
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
        print(ls)
        count1=0
        count2=0
        count3=0
      
    


        




