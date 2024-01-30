import sys
import time
import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import queue
import scipy
from scipy.optimize import least_squares

global ANCHORS 
ANCHORS = {}


def equations_v2 ( guess, id,ANCHORS ):
    x, y , z = guess
   
    return [
          (x - a["x"]) ** 2 
        + (y - a["y"]) ** 2 
        + (z - a["z"]) ** 2 
        - (a["range"]) ** 2 for a in ANCHORS[id].values()
    ]

def test_ls():
  global ANCHORS  
  ANCHORS_TEST = {}
  ANCHORS_TEST[0] = {
    "pub1": {
        "id": 0, 
        "x": 5.0,
        "y": 0.0,
        "z": 0.0,
        "range": 0
    }, 
    "pub2": {
        "id": 0,
        "x": 0.0,
        "y": 5.0,
        "z": 0.0,
        "range": 7

    },
    "pub3": {
        "id": 0,
        "x": 0.0,
        "y": 0.0,
        "z": 0.0,
        "range": 5
    },
    "pub4": {
        "id": 0,
        "x": 5.0,
        "y": 5.0,
        "z": 0.0,
        "range": 5
    },
    "pub5": {
        "id": 0,
        "x": 5.0,
        "y": 6.0,
        "z": 0.0,
        "range": 6
    }
  }
  iguess = (0.0,0.0,0.0)
  ANCHORS = ANCHORS_TEST
  results = least_squares(equations_v2, iguess,args=(0,ANCHORS))
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
            message_queue.put((aid,float(ax),float(ay),float(az),id,float(range),timestamp),block=False)
            

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
        if id not in ANCHORS.keys():
                ANCHORS[id] = {}
        ANCHORS[id][aid] = {  
            "x": ax, 
            "y": ay, 
            "z": az,
            "range": range,
            "timestamp": timestamp
        }
        #print(ANCHORS)
        if len(ANCHORS[id]) >= 3:
            iguess = (0.0,0.0,0.0)
            results = least_squares(equations_v2, iguess, args=(id,ANCHORS))
            print(results.x)
            client.publish("test/lsquares",str(results.x[0])+","+str(results.x[1])+","+str(results.x[2]))

         
    except queue.Empty:
        print("queue is empty")


