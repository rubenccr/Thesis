import serial
import time


def parse(s):
  
  parsedstr = ["","",""]
  aux = s.split(" ")
  parsedstr[2]=aux[2]
  aux2 = aux[1].split("}\\")
  a16 = aux2[0].split("\"a16\":")
  a16 = a16[1].split(",")
  a16 = a16[0].split("\"")
  parsedstr[0] = a16[1]

  d = aux2[0].split("\"D\":")
  d = d[1].split(",")
  d = d[0].split("\'")
  parsedstr[1] = d[0]
 
  return parsedstr



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
        # Total number of bits to be read
        bytesize=serial.EIGHTBITS,
        # Number of serial commands to accept before timing out
        timeout=1
)

ser.readline()
while(True):
 
  print(parse(str(ser.readline())+ " "+str(time.monotonic_ns())))





