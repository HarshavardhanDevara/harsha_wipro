# Write Custom Exception  if entered age is negative , rais the error saying that
# age can not be negative
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return f"Age is {age}"

try:
    age = int(input("Enter your age: "))
    print(check_age(age))
except ValueError as e:
    print(f"Error: {e}")