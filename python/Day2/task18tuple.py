score=()
print(type(score))
marks=(24,45,55)
print(type(marks))
# marks[0]=22
# print(marks) ##cannot modified or added
marks=list(marks)
print(type(marks))
marks[0]=22
print(marks)
marks.insert(1,20)
print(marks)
marks.append(99)
print(marks)
mk=[1,2,3,4]
marks.extend(mk)
print(marks) 
print(type(marks))
marks=tuple(marks)
print(marks)
print(type(marks))