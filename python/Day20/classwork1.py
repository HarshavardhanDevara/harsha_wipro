# count no of bits in a given number n
 
def countSetBits( n): 
	# Using bin function in number 
	ans = bin( n ) 
	return ans.count( "1" ) 
# Get value from user 
n=int(input(" Enter value for  n "))
# Function calling 
print( countSetBits(n))