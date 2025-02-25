# Count total set bits in all numbers from 1 to n
# Given a positive integer n, count the total number of set bits in binary representation of all numbers from 1 to n.
# Examples:
# Input: n = 3
# Output:  4
# Binary representations are 1, 2 and 3
# 1, 10 and 11 respectively. Total set
# bits are 1 + 1 + 2 = 4.
# Input: n = 6
# Output: 9
# Input: n = 7
# Output: 12
# Input: n = 8
# Output: 13
# Write a function which first converts number into binary using bin(num) function and
# returns count of set bits in it.

# Function to Count total set bits in all numbers
# from 1 to n
# user defined function
def countSetBit(num):
 
	# convert decimal value into binary and
	# count all 1's in it
	binary = bin(num)
 
	return len([ch for ch in binary if ch=='1'])
 
# function which count set bits in each number
def countSetBitAll(input):
	# map count function on each number
	print (sum(map(countSetBit,input)))
 
n = 8
input=[]
for i in range(1,n+1):
    input.append(i)
    countSetBitAll(input)

