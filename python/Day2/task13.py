# Remove empty strings from a list of strings
# Given:str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
# Expected Output:
# Original list of sting
# ['Emma', 'Jon', '', 'Kelly', None, 'Eric', '']
# After removing empty strings
# ['Emma', 'Jon', 'Kelly', 'Eric']

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

res_list = []

for s in str_list:

    # check for non empty string

    if s:

        res_list.append(s)

print(res_list)