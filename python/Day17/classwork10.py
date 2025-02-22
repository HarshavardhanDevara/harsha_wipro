import pandas as pd
 
data = [
    ["Alice", 25, "New York"],
    ["Bob", 30, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]
 
df = pd.DataFrame(data, columns=["Name", "Age", "City"])
print(df)