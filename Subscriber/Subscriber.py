import sys
import time
import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import queue
from scipy.optimize import least_squares


#Subscriber recebe distancias ja processadas pelos algoritmos.

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
            
            
            

 
            
global message_queue
message_queue = queue.Queue()
client = mqtt.Client(sys.argv[2])
client.on_connect=on_connect
client.on_message=on_range
client.connect(sys.argv[1],1886)
client.subscribe("test/lsquares")
client.loop_start()

while True:
    (id,range,timestamp) = message_queue.get()
    print("Data received: ", id,range,timestamp)
    
    


        




