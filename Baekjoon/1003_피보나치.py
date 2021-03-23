def fib(n):
    if n == 0 or n == 1:
        memo[n] = n
        return n
    elif memo[n] == 0:
        memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]

for _ in range(int(input())):

    memo = [0] * 41
    n = int(input())
    if n == 0:
        print('1 0')
    else:
        fib(n)
        print(memo[n-1], memo[n])