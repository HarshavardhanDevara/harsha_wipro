# File1.py
 
print ("File1 __name__ = %s" %__name__)
 
if __name__ == "__main__": 
	print ("File1 is being run directly") 
else: 
	print ("File1 is being imported") 
 
 
# File1.py
 
print("\n")
 
print (__name__)
 
print("\n")
 
if __name__ == "__main__":
 
	print ("File1 is being run directly")
 
else: 
	print ("File1 is being imported")