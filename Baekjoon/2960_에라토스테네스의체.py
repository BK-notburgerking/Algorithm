# n = 1000
# sieve = [False, False] + ([True] * (n - 1))
# primes = []
#
# for i in range(2, n + 1):
#     if sieve[i]:
#         primes.append(i)
#     for j in range(i * 2, n + 1, i):
#         sieve[j] = False
#
# print(primes)


N, K = map(int, input().split())
tmp = 0
sieve = [True] * (N + 1)
for i in range(2, N + 1):
    for j in range(i, N + 1, i):
        if sieve[j] != False:
            sieve[j] = False
            tmp += 1
            if tmp == K:
                print(j)