def bubble_sort(sequence):
    n = len(sequence)
    for i in range(n-1):
        for j in range(n-i-1):
            if(sequence[j] > sequence[j+1]):
                sequence[j], sequence[j+1] = sequence[j+1], sequence[j]
 
seq=[2,1,4,56,78 ,0 ,-5]
bubble_sort(seq)
print(seq)