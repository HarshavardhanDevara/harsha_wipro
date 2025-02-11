#Exercise 8: Rename key of a dictionary
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
# Renamed key 'city' to 'location'
sample_dict['location'] = sample_dict.pop('city')
print(sample_dict)