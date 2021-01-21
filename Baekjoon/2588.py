# 곱셈
# https://www.acmicpc.net/problem/2588

x = int(input())
y = input()[::-1]

print(x * int(y[0]))
print(x * int(y[1]))
print(x * int(y[2]))
print((x * int(y[2]) * 100) + (x * int(y[1]) * 10) + (x * int(y[0])))