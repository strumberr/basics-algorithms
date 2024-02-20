import math

n = 7

def prime(n):
    if n < 2:
        
        return False

    for i in range(2, math.floor(math.sqrt(n) + 1)):
        if n % i == 0:
            print("Not prime")
            
            return False
        
    return True

print(prime(n))
