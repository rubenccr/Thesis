import csv
import pandas as pd



df = pd.read_csv("pc3specificLS.csv",sep=';')

df1 = pd.DataFrame(columns=["Avg.Error LS","STD. LS"])
print(round(df["ERRO LS"].mean(),2))
print(round(df["ERRO LS"].std(),2))
#df1["Avg.Error LS"] = [round(df["ERRO LS"].mean(),2)]
#df1["STD. LS"] = [round(df["ERRO LS"].std(),2)]

#df1.to_csv('pc3errortable.csv', sep=';',index=False)
