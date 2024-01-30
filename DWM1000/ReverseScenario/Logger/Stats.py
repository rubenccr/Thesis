import pandas as pd
import sys
import math


s = sys.argv[1]
#print(s[1])
if("Pub" in s): 
   
 
   df = pd.read_csv(sys.argv[1],sep=';')
   npub = df['NodeId'].unique()
   gtx = input("Ground truth X?")
   gty = input("Ground truth Y?")
   print("")
   for i in npub:
      means = df[df['NodeId']==i]['Range'].mean()
      stds = df[df['NodeId']==i]['Range'].std()
      nodex = df[df['NodeId']==i]['X'].iloc[0]
      nodey = df[df['NodeId']==i]['Y'].iloc[0]
      rdistance = math.sqrt((float(gtx)-float(nodex))**2 + (float(gty)-float(nodey))**2)
      diffs = means - rdistance
      maxr = df[df['NodeId']==i]['Range'].max()
      minr = df[df['NodeId']==i]['Range'].min()
      print(str(i) + " mean: " +str(means))
      print(str(i) + " std: " +str(stds))
      print(str(i) + " min: " +str(minr))
      print(str(i) + " max: " +str(maxr))
      print(str(i) + " Distance to ground truth range: " +str(diffs))
      print("")
   #print(df)
   
else: 
    gtx = input("Ground truth X?")
    gty = input("Ground truth Y?")
    df = pd.read_csv(sys.argv[1],sep=';')
    meanX = df['X'].mean()
    meanY = df['Y'].mean()
    meanZ = df['Z'].mean()
    stdX = df['X'].std()
    stdY = df['Y'].std()
    stdZ = df['Z'].std()
    diffX = meanX-float(gtx)
    diffY = meanY-float(gty)
    minX = df['X'].min()
    minY = df['Y'].min()
    maxX = df['X'].max()
    maxY = df['Y'].max()
    print("")
    print("X mean: " + str(meanX))
    print("Y mean: " + str(meanY))
    print("Z mean: " + str(meanZ))
    print("")
    print("X std: " + str(stdX))
    print("Y std: " + str(stdY))
    print("Z std: " + str(stdZ))
    print("")
    print("Distance to measured ground truth X: " + str(diffX))
    print("Distance to measured ground truth Y: " + str(diffY))
    print("")
    print("X max value registered: " + str(maxX))
    print("Y max value registered: " + str(maxY))
    print("")
    print("X min value registered: " + str(minX))
    print("Y min value registered: " + str(minY))

