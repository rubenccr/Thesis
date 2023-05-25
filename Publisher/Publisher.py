import serial
import time
from queue import Queue
from threading import Thread
import MQTT_Pub
import UWB_Parser

#Input the serial port ID
s = input("ttyACM: ")
       
ser = serial.Serial(
        #Serial Port to read the data from
        port='/dev/ttyACM'+ s,
        #Rate at which the information is shared to the communication channel
        baudrate = 9600,
        #Applying Parity Checking (none in this case)
        parity=serial.PARITY_NONE,
        # Pattern of Bits to be read
        stopbits=serial.STOPBITS_ONE,
        # Total number of bits to be172.17.71.195 read
        bytesize=serial.EIGHTBITS,
        # Number of serial commands to accept before timing out
        timeout=1
)

ser.readline()
#q = Queue(maxsize = 20)
ip = input("IP: ")
brokerid = input("Name your publisher: ")
c=MQTT_Pub.startbroker(ip,brokerid)


while(True):
     t = time.time_ns()
     print(t)
     id,range = UWB_Parser.parse(str(ser.readline()))
     print(id,range,t)
     MQTT_Pub.publish(c, '{},{},{}'.format(id,range,t))
  
        




