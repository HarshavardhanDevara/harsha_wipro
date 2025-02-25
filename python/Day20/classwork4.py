import math
 
def count_bits(num):
	return int(math.log2(num)) + 1
 
num=13
 
print(count_bits(num))