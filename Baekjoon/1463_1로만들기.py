x = int(input())
dp = [i for i in range(x + 1)]

for i in range(1, x + 1):
    if i % 3 == 0 and i % 2 == 0:
        dp[i] = min(dp[i//3] + 1, dp[i//2] + 1)
    elif i % 3 == 0:
        dp[i] = min(dp[i//3] + 1, dp[i-1] + 1)
    elif i % 2 == 0:
        dp[i] = min(dp[i//2] + 1, dp[i-1] + 1)

print(dp[x] - 1)