with open('text.bin', 'rb') as file:
    data = file.read()
    print("Read from binary file:", data.decode('utf-8'))  # Decode back to string