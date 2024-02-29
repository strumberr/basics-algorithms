import math


def factorial(n):
    if n == 0:
        return 1
    
    factorialVar = n * factorial(n - 1)

    print(factorialVar)

    return factorialVar


def arithmeticSum(n):
    if n == 0:
        return 0

    return n + arithmeticSum(n - 1)

def GCD(a, b):

    if b == 0:
        return a

    gcdVar = GCD(b, a % b)
    print(gcdVar)
    return gcdVar

# longest common subsequence
def LCS(s1, s2, i, j):

    if i == 0 or j == 0:
        return 0

    if s1[i - 1] == s2[j - 1]:
        z = 1 + LCS(s1, s2, i - 1, j - 1)
        # print(z)
        return z
    else:
        x = max(LCS(s1, s2, i - 1, j), LCS(s1, s2, i, j - 1))
        # print(x) 
        return x
    

def LCS_matrix(s1, s2):

    m, n = len(s1), len(s2)
    matrix = [[0 for _ in range(n+1)] for _ in range(m+1)]
    
    def LCS(s1, s2, i, j, matrix):
        
        if i == 0 or j == 0:
            matrix[i][j] = 0
            return 0

        if matrix[i][j] != 0:
            return matrix[i][j]

        if s1[i - 1] == s2[j - 1]:
            matrix[i][j] = 1 + LCS(s1, s2, i - 1, j - 1, matrix)
        else:
            matrix[i][j] = max(LCS(s1, s2, i - 1, j, matrix), LCS(s1, s2, i, j - 1, matrix))
        return matrix[i][j]

    LCS(s1, s2, m, n, matrix)
    
    return matrix


# print(factorial(5))
# print(arithmeticSum(5))
# print(GCD(20, 12))
# print(LCS("AGGTAB", "GXTXAYB", 6, 7))
# print it in a matrix form by formatting the output
s1 = "AGGTAB"
s2 = "GXTXAYB"

matrix = LCS_matrix(s1, s2)

print("  G X T X A Y B")

s1 = list(s1)
s1.append(" ")

for row in matrix:
    rowValueS1 = s1[matrix.index(row)]
    print(rowValueS1 + " " + " ".join(str(cell) for cell in row))
    