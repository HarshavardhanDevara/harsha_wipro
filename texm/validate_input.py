class IllegalArgumentException(Exception):
    pass

class NumberFormatException(Exception):
    pass

class NoSuchElementException(Exception):
    pass

def validate_register_number(register_number):
    if len(register_number) != 9 or not (register_number[:2].isdigit() and register_number[2:5].isalpha() and register_number[5:].isdigit()):
        raise IllegalArgumentException("Register Number must be in the format 2 digits, 3 letters, 4 digits.")
    if not register_number.isalnum():
        raise NoSuchElementException("Register Number contains invalid characters.")

def validate_mobile_number(mobile_number):
    if len(mobile_number) != 10:
        raise IllegalArgumentException("Mobile Number must contain exactly 10 characters.")
    if not mobile_number.isdigit():
        raise NumberFormatException("Mobile Number must contain only digits.")

def main():
    try:
        register_number = input().strip()
        mobile_number = input().strip()
        
        validate_register_number(register_number)
        validate_mobile_number(mobile_number)
        
        print("Valid")
    except (IllegalArgumentException, NumberFormatException, NoSuchElementException) as e:
        print(f"Invalid with exception message: {str(e)}")

if __name__ == "__main__":
    main()
