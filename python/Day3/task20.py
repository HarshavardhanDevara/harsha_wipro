# Writing a List of Integers as Binary Data

import struct

numbers = [10, 20, 30, 40]  # List of integers

with open('numbers.bin', 'wb') as file:
    for num in numbers:
        file.write(struct.pack('i', num))  # Convert each integer to 4-byte binary format

print("Binary numbers written successfully.")