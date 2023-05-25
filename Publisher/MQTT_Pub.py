import paho.mqtt.client as mqtt
import time

def on_log(client, userdata, level, buff):
           print("Log: "+buff)
           
def on_connect(client, userdate, flags, rc):
           if rc==0:
              print("connected OK")
           else:
              print("Bad connection return code=", rc)
              
def on_disconnect(client, userdata, flags, rc=0):
            print("Disconnected result code "+str(rc))
            

def startbroker(addr, brokerid):

    broker=addr #change 
    client = mqtt.Client(brokerid)
    client.on_connect=on_connect
    client.on_disconnect=on_disconnect
    client.on_log=on_log           
    print("Connecting to broker ", broker)
    client.connect(broker,1886)
    client.loop_start()
    return client

def publish(client,msg):

    client.publish("test/distances",msg)
    #time.sleep(4)
    #client.loop_stop()
    #client.disconnect()
