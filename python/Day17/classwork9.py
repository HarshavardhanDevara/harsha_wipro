#creating df with pandas to csv
import pandas as pd
 
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
 
df = pd.DataFrame(data)
 
df.to_csv(r"C:\Users\harsh\Desktop\harsha_wipro\python\Day17\dfdata.csv", index=False)  # Save without index