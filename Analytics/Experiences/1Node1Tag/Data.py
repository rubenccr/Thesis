import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

var = input("file you want to import: ")
df = pd.read_csv(str(var)+".csv")

print("Mean distances:\n")
print(df.groupby("TagID")["Distance"].mean())
print("\n")


print("STD:\n")
print(df.groupby("TagID")["Distance"].std())
print("\n")

print("Count:\n")
print(df.groupby("TagID")["Distance"].count())
print("\n")

print("Max:\n")
print(df.groupby("TagID")["Distance"].max())
print("\n")

print("Min:\n")
print(df.groupby("TagID")["Distance"].min())
print("\n")

print("Median:\n")
print(df.groupby("TagID")["Distance"].median())
print("\n")



x_data = df['Timestamp'].apply(lambda x: x/(10**9)/60)
y_data = df['Distance'].apply(lambda x: x/100)
plt.scatter(x_data, y_data, color = 'green', marker = '+', label = 'Experience')
plt.axhline(int(var[len(var)-2]), color = 'red', linestyle = '-',label = 'Real Measured Distance')
plt.title('UWB Distance Data Plotted')
plt.xlabel('Time\n(Minutes)')
plt.ylabel('Distance\n(Meters)')
plt.legend()
plt.show()
