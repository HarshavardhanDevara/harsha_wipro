marks=[12,45,56,78,9]
pmarks=filter(lambda a: a>=50 , marks)
fmarks=filter(lambda a: a<50  , marks)
print(list(pmarks))
print(list(fmarks))