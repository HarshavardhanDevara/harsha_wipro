cel=[23,25,27,29,31]
fah= map(lambda cl:cl*1.8+32, cel)
print(list(fah))

fah=[80,85,90,95,100]
cel=map(lambda fh:(fh-32)/1.8, fah)
print(list(cel))