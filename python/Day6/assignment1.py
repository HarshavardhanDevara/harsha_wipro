# Convert two lists into a dictionary
harsha = ["bikes", "cars", "mobiles"]
colour = ["red", 'balck', 'grey']
likes=dict(zip(harsha, colour))        #zip function to pair elements 
print(likes)