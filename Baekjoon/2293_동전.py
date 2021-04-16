import sys; input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [0] * (k + 1) #dp의 1번 인덱스는 합해서 1이되는 경우의 수 2번 인덱스는 합해서 2가되는 경우의 수 ...
dp[0] = 1 #아무것도 선택하지 않는 경우 한가지

for coin in coins:
    for j in range(coin, k + 1):
        dp[j] += dp[j - coin]

print(dp[k])