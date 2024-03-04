import math


# O(2^n)
def fib(n):
    
    if n == 0 or n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)

print(f"first fib method: {fib(5)}")



f = {}
# O(n)
def fib2(n):
    
    if n == 0 or n == 1:
        return 1

    if n in f.keys():
        return f[n]
    
    f[n] = fib2(n - 1) + fib2(n - 2)
    
    print(f)
    
    return f[n]

print(f"second fib method: {fib2(5)}")



f = {}
f[0] = 1
f[1] = 1
# O(n)
def fib3(n):
    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]

print(f"third fib method: {fib3(5)}")





def fib4(n):
    
    b_nMinusOne = 1 
    a_n = 1
    
    for i in range(2, n + 1):
        c_nMinusTwo = b_nMinusOne
        b_nMinusOne = a_n
        a_n = c_nMinusTwo + b_nMinusOne
        
    return a_n

print(f"fourth fib method: {fib4(5)}")
