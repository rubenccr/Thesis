import serial
import time
from queue import Queue
from threading import Thread
import paho.mqtt.client as mqtt
import sys


def publog(client, userdata, level, buff):
           print("Log: "+buff)
           
def on_connect(client, userdate, flags, rc):
           if rc==0:
              print("connected OK")
           else:
              print("Bad connection return code=", rc)
              
def on_disconnect(client, userdata, flags, rc=0):
            print("Disconnected result code "+str(rc))
      
      

client = mqtt.Client(client_id=sys.argv[2])
client.on_connect=on_connect
client.on_disconnect=on_disconnect
client.on_log=publog         
print("Connecting to broker ", sys.argv[1])
client.connect(sys.argv[1],1886)
client.loop_start()
   


while(True):
     t = time.time_ns()
     
     print(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],id,range,t)
     client.publish("test/distances", '{},{},{},{},{},{},{}'.format(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],"dummytagid",5,t))
  
        




