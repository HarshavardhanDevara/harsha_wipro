class CustomError(Exception):

    pass
 
def validate_age(age):

    if age < 18:

        raise CustomError("Age must be 18 or above!")

    return "Valid age"
 
try:

    print(validate_age(16))

except CustomError as e:

    print(f"Validation Error: {e}")

 
