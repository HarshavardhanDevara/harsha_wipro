# Writing Bytes to a File
data = b'Hello, Binary World!'         # A bytes object
#with open('binary_file.bin', 'wb') as file:
#    file.write(data)
f=open('binary_file.bin', 'wb')
f.write(data)

print("Binary file written successfully.")

# The b'...' notation represents bytes.
# The file is opened in wb mode to write in binary format.
# The write() method writes the bytes to the file.