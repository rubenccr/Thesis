import serial
import time

#Input the serial port ID
s = input("ttyACM: ")
t = input("Log for how many mins?: ")
aux = time.localtime()
st=""
aux2="_"

for k in range(6):
      
      st += aux2+str(aux[k])
      if k>2:
        aux2=":"
       
        
         
with open("log"+st+"("+t+"mins).txt", 'w') as f:
    
 
 ser = serial.Serial(
        #Serial Port to read the data from
        port='/dev/ttyACM'+ s,
        #Rate at which the information is shared to the communication channel
        baudrate = 9600,
        #Applying Parity Checking (none in this case)
        parity=serial.PARITY_NONE,
        # Pattern of Bits to be read
        stopbits=serial.STOPBITS_ONE,
        # Total number of bits to be read
        bytesize=serial.EIGHTBITS,
        # Number of serial commands to accept before timing out
        timeout=1
)

 
 print("Logging for "+ t + " mins")
 #5 mins
 x=int(t)*60
 y=time.monotonic()
 z=x+y
 starttime=time.monotonic_ns()
 while time.monotonic()<=z:
       
       f.write(str(ser.readline())+ " "+str(time.monotonic_ns()-starttime)+"\n") 
        
        
f.close()
print("Logging done.") 
      



