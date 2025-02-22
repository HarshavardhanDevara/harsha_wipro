import pandas as pd
 
df= pd.read_csv(r"C:\Users\harsh\Desktop\harsha_wipro\python\Day17\data.csv")
print(type(df))

print(df.head()) #default it displays top 5 rows

print(df.tail()) #default it displays last 5 rows

print(df.info())

print(df.describe())

print(df.isnull().sum())

print(df.columns)
print(df.shape)