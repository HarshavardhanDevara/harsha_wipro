import pandas as pd

url_dict = { "$ref": "https://jsonplaceholder.typicode.com/todos/1" }
url = url_dict["$ref"]

df = pd.read_json(url)

print(df.head())