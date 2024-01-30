import serial
import time
from queue import Queue
from threading import Thread
import paho.mqtt.client as mqtt
import DWM1000_parser
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
      
      
#Input the serial port ID
s = input("ttyACM: ")
       
ser = serial.Serial(
        #Serial Port to read the data from
        port='/dev/ttyACM'+ s,
        #Rate at which the information is shared to the communication channel
        baudrate = 115200,
        #Applying Parity Checking (none in this case)
        parity=serial.PARITY_NONE,
        # Pattern of Bits to be read
        stopbits=serial.STOPBITS_ONE,
        # Total number of bits to be read
        bytesize=serial.EIGHTBITS,
        # Number of serial commands to accept before timing out
        timeout=1
)


ser.readline()
client = mqtt.Client(client_id=sys.argv[2])
client.on_connect=on_connect
client.on_disconnect=on_disconnect
client.on_log=publog         
print("Connecting to broker ", sys.argv[1])
client.connect(sys.argv[1],1886)
client.loop_start()
   


while(True):
     s = DWM1000_parser.parse(ser.readline().decode().strip())
     if(s=="invalid"):
         print("no message")
     else:
         #print(s)
         #mobileid,range,t =  s.split(",")
         mobileid,range =  s.split(",")
         t = time.time()
         print(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],mobileid,range,t)
         client.publish("test/distances", '{},{},{},{},{},{},{}'.format(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],mobileid,range,t))
  
        




