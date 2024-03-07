inputPart = list(map(int, input().split()))
n = inputPart[0]
x = inputPart[1]
priceEachBook = list(map(int, input().split()))
nPagesEachBook = list(map(int, input().split()))

dp = [0]*(x+1)

for i in range(n):
    for j in range(x, priceEachBook[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - priceEachBook[i]] + nPagesEachBook[i])
        
print(dp[x])

# time complexity: O(n*x)
