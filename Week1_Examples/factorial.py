import sys

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n*factorial_recursive(n-1)

def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

#print(factorial_recursive(231))
j = factorial_iterative(231)
k = factorial_recursive(235)

l = j*k

print("Size of l = ",sys.getsizeof(l))
