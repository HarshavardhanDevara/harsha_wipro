# 4. List rows in the ascending order of calories

import pandas as pd
df = pd.read_csv(r"C:\Users\harsh\Desktop\harsha_wipro\python\Day17\data.csv")

rows_ascending_calories = df.sort_values(by='Calories')
print("Rows in ascending order of calories:")
print(rows_ascending_calories, "\n")