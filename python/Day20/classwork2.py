def countTotalBits(num):
	# convert number into it's binary and 
	# remove first two characters .
	binary = bin(num)[2:]
	print(len(binary))
num = 13
countTotalBits(num)
#2
def countTotalBits(num):
    binary = bin(num)[2:]
    return len(binary)  # Return the length instead of printing

num = 13
print(countTotalBits(num))  
