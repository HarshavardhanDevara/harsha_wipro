# write python script to validate indian mobile phone nos
import re
def validate_mobile(number):
    pattern = r"^[6789]\d{9}$"  # Starts with 6, 7, 8, or 9 and has exactly 10 digits
    if re.fullmatch(pattern, number):
        return True
    else:
        return False
mobile_number = input("Enter an Indian mobile number: ")

if validate_mobile(mobile_number):
    print("Valid Indian mobile number.")
else:
    print("Invalid Indian mobile number.")
