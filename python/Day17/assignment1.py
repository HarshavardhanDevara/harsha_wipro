# Assignment
# 1. List rows  whose calories above 400

import pandas as pd
df = pd.read_csv(r"C:\Users\harsh\Desktop\harsha_wipro\python\Day17\data.csv")

calories_above_400 = df[df['Calories'] > 400]
print("Rows with calories above 400:")
print(calories_above_400, "\n")








 