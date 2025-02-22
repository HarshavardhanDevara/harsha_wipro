import pandas as pd
 
df = pd.read_csv(r"C:\Users\harsh\Desktop\harsha_wipro\python\Day17\dfdata.csv")  # Reads CSV file into a DataFrame
print(df)
print("Columns " , df.columns)
print("Size    " , df.shape)
print(type(df))
