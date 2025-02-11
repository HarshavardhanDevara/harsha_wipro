#  Calculate the sum and average of the digits present in a string
# Given a string s1, write a program to return the sum and average of the digits that appear in the string, 
# ignoring all other characters.
# Given:
# str1 = "PYnative29@#8496"
# Expected Outcome:
# Sum is: 38 Average is  6.333333333333333

input_str = "PYnative29@#8496"
total = 0
cnt = 0
for char in input_str:
    if char.isdigit():
        total += int(char)
        cnt += 1

# average = sum / count of digits
avg = total / cnt
print("Sum is:", total, "Average is ", avg)