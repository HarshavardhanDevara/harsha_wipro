import pandas as pd
 
data = [
    ["hari", 25, "hyderabad" , 50000],
    ["bindu", 22, "chennai",45000],
    ["manasa", 30, "bangalore" , 35000]
]
 
df = pd.DataFrame(data, columns=["Name", "Age", "City","Salary"])
 
df.to_csv(r"C:\Users\harsh\Desktop\harsha_wipro\python\Day17\emp.csv", index=False)  # Save without index
 