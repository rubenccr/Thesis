import csv
import pandas as pd



p5p6p7 = pd.read_csv("p5p6p7.csv",sep=';')
p5p6p9 = pd.read_csv("p5p6p9.csv",sep=';')
p6p7p9 = pd.read_csv("p6p7p9.csv",sep=';')
p5p7p9 = pd.read_csv("p5p7p9.csv",sep=';')

df1 = pd.DataFrame(columns=["Using","Avg.Error LS","STD. LS"])
df1["Using"] = ["P5/P6/P7","P5/P6/P9","P6/P7/P9","P5/P7/P9"]

error = []
std = []
#print(round(p5p6p7["LS"].mean(),2))
#print(round(p5p6p7["LS"].std(),2))
#print(round(p5p6p9["LS"].mean(),2))
#print(round(p5p6p9["LS"].std(),2))
#print(round(p6p7p9["LS"].mean(),2))
#print(round(p6p7p9["LS"].std(),2))
#print(round(p5p7p9["LS"].mean(),2))
#print(round(p5p7p9["LS"].std(),2))
error.append(round(p5p6p7["LS"].mean(),2))
error.append(round(p5p6p9["LS"].mean(),2))
error.append(round(p6p7p9["LS"].mean(),2))
error.append(round(p5p7p9["LS"].mean(),2))

std.append(round(p5p6p7["LS"].std(),2))
std.append(round(p5p6p9["LS"].std(),2))
std.append(round(p6p7p9["LS"].std(),2))
std.append(round(p5p7p9["LS"].std(),2))

print(error)
print(std)
df1["Avg.Error LS"] = error
df1["STD. LS"] = std

df1.to_csv('4combsLS.csv', sep=';',index=False)
