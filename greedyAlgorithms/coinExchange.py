
coins = [1, 5, 20]
x = 67

dp = [float('inf')] * (x + 1)

dp[0] = 0

for i in range(1, x + 1):
    for coin in coins:
        if i - coin >= 0:
            dp[i] = min(dp[i], dp[i - coin] + 1)


result = dp[x] if dp[x] != float('inf') else -1

print(result)
