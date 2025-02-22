# 2. List rows whose calories are between 400 and 450

import pandas as pd
df = pd.read_csv(r"C:\Users\harsh\Desktop\harsha_wipro\python\Day17\data.csv")
calories_between_400_450 = df[(df['Calories'] >= 400) & (df['Calories'] <= 450)]
print("Rows with calories between 400 and 450:")
print(calories_between_400_450, "\n")