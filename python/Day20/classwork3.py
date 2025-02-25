def countTotalBits(num):
	# bit_length function return 
	# total bits in number 
	B_len = num.bit_length()
	print("Total bits in binary are : ", B_len)
 
num = int(input("enter value for num:"))
 
countTotalBits(num)