# 0 1 1 2 3 5 8 13  21 34
# Write python script using recursion  for the fibo series for 10 terms
# fib(i)=f(i-1)+f(i-2)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
 
for i in range(10):
    print(fibonacci(i), end=" ")
 
# Output: 0 1 1 2 3 5 8 13 21 34