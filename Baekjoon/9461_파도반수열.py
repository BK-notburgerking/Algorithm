def dp(n):
    if n < 3:
        return 1
    if n >= 3 and memo[n] == 0:
        memo[n] = dp(n - 3) + dp(n - 2)
    return memo[n]

for _ in range(int(input())):

    N = int(input())
    memo = [0] * 100
    for i in range(3):
        memo[i] = 1
    dp(N - 1)
    print(memo[N - 1])