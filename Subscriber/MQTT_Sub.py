import paho.mqtt.client as mqtt
        
def on_connect(client, userdata, flags, rc):
           if rc==0:
              print("Client Connected")
              global connected
              connected=True
           else:
              print("Client is not connected")
              
def on_message(client, userdata, message):
            (id,range,timestamp) = message.payload.decode("utf-8").split(",")
            print(id,range,timestamp)
            
            

 
            
            

def startsub(addr):

    broker=addr #change 
    client = mqtt.Client("Sub")
    client.on_message=on_message
    client.on_connect=on_connect
    client.connect(broker,1886)
    client.loop_start()
    return client

def subscribe(client):

    client.subscribe("test/distances")
  
