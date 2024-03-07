import math

elements = [1, 2, 3, 5]
x = 9

# ------------- pull approach -------------
def sumToXPull(elements, x):
    dp = {0: 1}
    
    for i in range(1, x + 1):
        dp[i] = 0
        for e in elements:
            if i - e >= 0:
                dp[i] += dp[i - e]
                
    return dp[x]

print(f"sum to x: {sumToXPull(elements, x)}")


# ------------- push approach -------------
def sumToXPush(elements, x):
    dp = [0] * (x + 1)
    dp[0] = 1
    
    for i in range(0, x):
        for e in elements:
            if i + e <= x:
                dp[i + e] += dp[i]
                
    return dp[x]

print(f"sum to x: {sumToXPush(elements, x)}")