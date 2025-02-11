# A shop keeper gives discount based on the  amount purchased and rule is given below 
# Amount          Disc
# <1000           5%
# 1000-5000       7%
# >5000           10%
# we have to print amount , discount and netamount
amt=int(input("Enter amount value     "))
if amt < 1000:
   disc= 0.05*amt

if amt>=1000 and amt <=5000 :
   disc=0.07 * amt

if amt >5000:
   disc=0.1*amt
netamt=amt-disc
print("Amount         =" ,amt)
print("Discount       =" ,disc)
print("Net amount     = ",netamt)