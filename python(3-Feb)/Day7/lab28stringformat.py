#%modulo string formatting
name = "Harsha"
age = 25
print("my name is %s and i am %d years old" %(name,age))
# Using the format() Method
# The format() method is like the cooler, younger sibling of the modulo operator. 
# It's more flexible and easier to read.
print("My name is {} and I am {} years old.".format(name, age))
#index format
print("The {0} in the {1} weighs {2} pounds.".format("cat", "hat", 5))
print("The {1} in the {0} weighs {2} pounds.".format("hat", "cat", 5))
#f string format
print(f"My name is {name} and I am {age} years old.")
print("my name is {} and i am {} years old".format("harsha",25))
print("my name is {0} and i am {1} years old".format("harsha",25))
print("my name is {1} and i am {0} years old".format(25,"harsha"))
pi = 3.14159
print(f"Pi to two decimal places: {pi:.2f}")

 
 