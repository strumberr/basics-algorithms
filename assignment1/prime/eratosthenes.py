import math

n = 4

total_iterations = 0

def prime(n, total_iterations):

    primeVal = [True] * (n + 1)

    primeVal[0] = primeVal[1] = False

    for i in range(2, math.floor(math.sqrt(n) + 1)):

        if primeVal[i]:
            
            for j in range(i * i, n + 1, i):

                primeVal[j] = False

                total_iterations += 1


        total_iterations += 1

    return primeVal[n], total_iterations

print(prime(n, total_iterations))

