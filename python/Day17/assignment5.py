# 5. List rows whose pulse is 120 and calories above 400
# 6. Count rows whose pulse is 120 and calories above 400

import pandas as pd
df = pd.read_csv(r"C:\Users\harsh\Desktop\harsha_wipro\python\Day17\data.csv")

# 5. List rows whose pulse is 120 and calories above 400
pulse_120_calories_above_400 = df[(df['Pulse'] == 120) & (df['Calories'] > 400)]
print("Rows with pulse 120 and calories above 400:")
print(pulse_120_calories_above_400, "\n")

# 6. Count rows whose pulse is 120 and calories above 400
count_pulse_120_calories_above_400 = len(pulse_120_calories_above_400)
print("Count of rows with pulse 120 and calories above 400:")
print(count_pulse_120_calories_above_400)