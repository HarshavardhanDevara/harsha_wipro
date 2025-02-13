import pandas as pd

# Dictionary containing the URL to the JSON data
url_dict = { "$ref": "https://jsonplaceholder.typicode.com/todos" }
url = url_dict["$ref"]

# Read the JSON data from the URL into a DataFrame
df = pd.read_json(url)

# Print the DataFrame
print(df.head())
print(df)