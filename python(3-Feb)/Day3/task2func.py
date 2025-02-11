def ctof(cel):
    return cel*1.8+32
def ftoc(fah):
    return (fah-32)/1.8
print("temp in fahren",  ctof(40))
print("temp in cel", ftoc(104))