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
