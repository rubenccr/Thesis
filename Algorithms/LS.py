import sys
import time
import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import queue
import scipy
from scipy.optimize import least_squares

global ANCHORS 
ANCHORS = {}


def equations_v2 ( guess ):
    x, y , z = guess
   
    return [
          (x - a["x"]) ** 2 
        + (y - a["y"]) ** 2 
        + (z - a["z"]) ** 2 
        - (a["range"]) ** 2 for a in ANCHORS.values()
    ]

def test_ls():
  global ANCHORS  
  ANCHORS_TEST = {
    "pub1": { 
        "x": 5,
        "y": 0,
        "z": 0.0,
        "range": 0
    }, 
    "pub2": {
        "x": 0,
        "y": 5,
        "z": 0.0,
        "range": 7

    },
    "pub3": {
        "x": 0,
        "y": 0,
        "z": 0,
        "range": 5
    },
    "pub4": {
        "x": 5,
        "y": 5,
        "z": 0,
        "range": 5
    },
    "pub5": {
        "x": 5,
        "y": 6,
        "z": 0,
        "range": 6
    }
  }
  iguess = (0,0,0)
  ANCHORS = ANCHORS_TEST
  results = least_squares(equations_v2, iguess)
  print(results.x)

#test_ls()

#sys.exit(0) 

global message_queue 
message_queue = queue.Queue()

def on_connect(client, userdata, flags, rc):
           if rc==0:
              print("Client Connected")
              global connected
              connected=True

           else:
              print("Client is not connected")
              
def on_range(client, userdata, message):
            (aid,ax,ay,az,id,range,timestamp) = message.payload.decode("utf-8").split(",")
            # print("callack", id,range,timestamp)
            #global message_queue 
            message_queue.put((aid,int(ax),int(ay),int(az),id,int(range),timestamp),block=False)
            

client = mqtt.Client("LeastSquares")
client.on_connect=on_connect
client.on_message=on_range
client.connect(sys.argv[1],1886)
client.subscribe("test/distances")
client.loop_start()

while True:
    try:
        (aid, ax, ay, az, id,range,timestamp) = \
            message_queue.get(block=True,timeout=1)
        ANCHORS[aid] = {  
            "x": ax, 
            "y": ay, 
            "z": az,
            "range": range,
            "timestamp": timestamp
        }
        #print(ANCHORS)
        if len(ANCHORS) >= 3:
            iguess = (0,0,0)
            results = least_squares(equations_v2, iguess)
            #print(results.x)
            client.publish("test/lsquares",str(results.x[0])+","+str(results.x[1])+","+str(results.x[2]))

         
    except queue.Empty:
        print("queue is empty")


