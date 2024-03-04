
inputPart = list(map(int, input().split()))
n = inputPart[0]
x = inputPart[1]
coins = list(map(int, input().split()))

# n = 3
# x = 9
# coins = [2, 3, 5]

mod = 10**9 + 7

dp = [0]*(x+1)
dp[0] = 1

for coin in coins:
    for i in range(coin, x + 1):
        dp[i] = (dp[i] + dp[i - coin]) % mod

print(dp[x])

