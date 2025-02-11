staff=["harsha", 45, 93.33 , True]
print("Name  =" , staff[0])  # index is used to access its elements. Index starts from 0   from left to right
print("Age   =" , staff[1])
print("Score =" , staff[-2])  # we access its elements from right to left. Index starts from -1,-2, etc
staff[1]=43                   # we modify the value . it is possible in the list [ mutable ]
print(staff)
print("\n")
for i in staff:
    print(i)