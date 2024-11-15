import numpy as np
from pylab import *
import pandas as pd

errorsLS = []
errorsDWM = []
errorsLSv2 = []


for i in range(1,12):
  if(i==7):
      continue
  if(i==3):
      df = pd.read_csv("pc"+str(i)+"LS.csv",sep=';')
      for k in range(0,len(df["ERRO LS"])):
           
           errorsLS.append(df["ERRO LS"][k])
           errorsDWM.append(df["ERRO_DWM"][k])
  else:
      #print(i)
      df = pd.read_csv("pc"+str(i)+"LS.csv",sep=';')
      for k in range(0,len(df["ERRO LS"])):
           
           errorsLS.append(df["ERRO LS"][k])
           errorsDWM.append(df["ERRO_DWM"][k])
           errorsLSv2.append(df["ERRO LS"][k])

df = pd.read_csv("pc3specificLS.csv",sep=';')
for k in range(0,len(df["ERRO LS"])):
  errorsLSv2.append(df["ERRO LS"][k])


#print(errorsLS)

# Calculate the cumulative proportion of the data that falls below each value
cumulative = np.linspace(0, 100, len(errorsLS))

# Sort the data in ascending order
sorted_data = np.sort(errorsLS)

# Calculate the cumulative proportion of the sorted data
cumulative_data = np.cumsum(sorted_data) / np.sum(sorted_data)

plt.plot(sorted_data, cumulative_data*100, color='r', label='LS')

# Add labels and title
plt.xlabel("Error Value")
plt.ylabel("CDF (%)")
plt.xlim(0,6)
plt.title("Cumulative Distribution Function of Error Values")
#plt.show()



# Calculate the cumulative proportion of the data that falls below each value
cumulative1 = np.linspace(0, 1, len(errorsDWM))

# Sort the data in ascending order
sorted_data1 = np.sort(errorsDWM)

# Calculate the cumulative proportion of the sorted data
cumulative_data1 = np.cumsum(sorted_data1) / np.sum(sorted_data1)

plt.plot(sorted_data1, cumulative_data1*100,color='g', label='DWM')

# Add labels and title
plt.xlabel("Error Value")
plt.ylabel("CDF (%)")
plt.xlim(0,6)
#plt.title("Cumulative Distribution Function (CDF) of error values DWM")
#plt.show()


# Calculate the cumulative proportion of the data that falls below each value
cumulative2 = np.linspace(0, 1, len(errorsLSv2))

# Sort the data in ascending order
sorted_data2 = np.sort(errorsLSv2)

# Calculate the cumulative proportion of the sorted data
cumulative_data2 = np.cumsum(sorted_data2) / np.sum(sorted_data2)

plt.plot(sorted_data2, cumulative_data2*100,color='b', label='LS modified')

# Add labels and title
plt.xlabel("Error Value")
plt.ylabel("CDF (%)")
plt.xlim(0,6)
#plt.title("Cumulative Distribution Function (CDF) of error values LS")
plt.legend()
plt.show()



