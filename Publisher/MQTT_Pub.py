import paho.mqtt.client as mqtt
import time

def publog(client, userdata, level, buff):
           print("Log: "+buff)
           
def on_connect(client, userdate, flags, rc):
           if rc==0:
              print("connected OK")
           else:
              print("Bad connection return code=", rc)
              
def on_disconnect(client, userdata, flags, rc=0):
            print("Disconnected result code "+str(rc))
            

def startpub(addr, pubid):

    client = mqtt.Client(client_id="LeastSquares")
    client.on_connect=on_connect
    client.on_disconnect=on_disconnect
    client.on_log=publog           
    print("Connecting to broker ", addr)
    client.connect(addr,1886)
    client.loop_start()
    return client


    
def publishLS(client,msg):

    client.publish("test/lsquares",msg)    
    
    

        
def on_connectsub(client, userdata, flags, rc):
           if rc==0:
              print("Client Connected")
              global connected
              connected=True
           else:
              print("Client is not connected")
              
def on_messagesub(client, userdata, message):
            (id,range,timestamp) = message.payload.decode("utf-8").split(",")
            print(id,range,timestamp)
            
            

 
            
            

def starts(addr):

    
    client = mqtt.Client("LS")
    client.on_message=on_message
    client.on_connect=on_connect
    client.connect(addr,1886)
    client.loop_start()
    return client

def subscribe(client):

    client.subscribe("test/lsquares")   
