import pandas as pd
import numpy  as np
import matplotlib.pyplot as mtp
# read_csv() method to read csv and convert into data frame
# dataframe is a kind of data set like RDBMS table having rows and columns
df=pd.read_csv(r'C:\Users\harsh\Desktop\harsha_wipro\python\Day8\sl.csv')
#by giving path where ever it is it will be readable here r string as raw string to read path 
print(df.head())  # head() method returns the first 5 rows
