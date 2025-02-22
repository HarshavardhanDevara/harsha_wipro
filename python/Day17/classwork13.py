import pandas as pd
 
df = pd.read_csv(r"C:\Users\harsh\Desktop\harsha_wipro\python\Day17\emp.csv")  # Reads CSV file into a DataFrame
print(df, "\n")

print("Columns:\n", df.columns, "\n")
print("Size:\n", df.shape, "\n")  # How many rows and columns

print("Single Column (Name):\n", df["Name"], "\n")  # Access single column
 
print("Multiple Columns (Name, Age):\n", df[["Name", "Age"]], "\n")  # Access multiple columns
 
print("First Row using loc:\n", df.loc[0], "\n")  # Access first row using label-based indexing
 
print("Second Row using iloc:\n", df.iloc[1], "\n")  # Access second row using index-based position
 
print("Rows where Age > 25:\n", df[df["Age"] > 25], "\n")  # Get rows where Age > 25
 
print("Rows where Salary > 40000:\n", df[df["Salary"] > 40000], "\n")

df["Age"] = df["Age"] + 1  # Increment all ages by 1

print("Updated DataFrame (Age Incremented):\n", df, "\n")

df = df.drop(columns=["Salary"])  # Remove column

print("Final DataFrame (Without Salary Column):\n", df, "\n")


print("Summary Statistics:\n", df.describe(), "\n")  # Summary statistics
print("Column-wise Mean:\n", df.mean(numeric_only=True), "\n")  # Column-wise mean
print("Max Age:\n", df["Age"].max(), "\n")  # Max age

df_sorted = df.sort_values(by="Age", ascending=False)  # Sort by Age (Descending)
print("Sorted DataFrame (By Age Descending):\n", df_sorted, "\n")

df_grouped = df.groupby("City")["Age"].mean()  # Group by City and calculate mean Age
print("Grouped Data (Mean Age by City):\n", df_grouped, "\n")
