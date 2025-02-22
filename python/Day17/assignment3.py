# 3. List columns Maxpulse and Calories

import pandas as pd
df = pd.read_csv(r"C:\Users\harsh\Desktop\harsha_wipro\python\Day17\data.csv")

maxpulse_and_calories = df[['Maxpulse', 'Calories']]
print("Columns Maxpulse and Calories:")
print(maxpulse_and_calories)
