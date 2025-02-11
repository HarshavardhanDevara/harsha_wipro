staff={"name":"harsha", "age":25, "loc":"tirupati"}
print(staff)
print(staff.keys())
print(staff.values())
print(type(staff))
# for i in staff():
#     print(i)
for i in staff.keys():
    print(i)
for i in staff.values():
    print(i)
for i in staff.items():
    print(i)
for i,j in staff.items():
    print(i,"--->",j)
staff["loc"]="ap"
print(staff)