import time

def parse(s):
  #print(s)
  if(len(s)<22):
      return "invalid"
  aux = s.split("[")
  mobileid=aux[0]
  aux2 = s.split("=")
  range = aux2[1]
  parsedstr = mobileid +","+ range #+","+ str(time.time_ns())
  
  return parsedstr

