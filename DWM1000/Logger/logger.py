import sys
import time
import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import queue
import datetime



def on_connect(client, userdata, flags, rc):
           if rc==0:
              print("Logger Connected")
              global connected
              connected=True

           else:
              print("Client is not connected")
              
def on_range(client, userdata, message):
            (ex,ey,ez) = message.payload.decode("utf-8").split(",")
            global message_queue 
            message_queue.put((ex,ey,ez))
            
            
            
def on_range2(client, userdata, message):
          (aid,ax,ay,az,id,range,timestamp) = message.payload.decode("utf-8").split(",")
          global message_queue2 
          message_queue2.put((aid,ax,ay,az,id,range,timestamp),block=False)
            
            
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
current_date = datetime.date.today()

         
f = open("logLS_"+str(current_date)+"_"+str(current_time)+".csv", "a")
f2 = open("logPub_"+str(current_date)+"_"+str(current_time)+".csv", "a")

f.write("{};{};{}\n".format("X","Y","Z")) 
f2.write("{};{};{};{};{};{};{}\n".format("NodeId","X","Y","Z","TagId","Range","TimeStamp"))

            
global message_queue
global message_queue2
 
 
message_queue = queue.Queue()
client = mqtt.Client("Logger")
client.on_connect=on_connect
client.on_message=on_range
client.connect(sys.argv[1],1886)
client.subscribe("test/lsquares")
client.loop_start()

message_queue2 = queue.Queue()
client2 = mqtt.Client("Logger2")
client2.on_connect=on_connect
client2.on_message=on_range2
client2.connect(sys.argv[1],1886)
client2.subscribe("test/distances")
client2.loop_start()


while True:
    try:
         (ex,ey,ez) = message_queue.get()
         ts=time.time()
         f.write("{};{};{};{}\n".format(ex,ey,ez,ts))
         (aid,ax,ay,az,id,range,timestamp) = message_queue2.get()
         f2.write("{};{};{};{};{};{};{}\n".format(aid,ax,ay,az,id,range,timestamp))
    except KeyboardInterrupt:
         break 

f.close()
f2.close()
    
    
    
    
    
    
    
    
