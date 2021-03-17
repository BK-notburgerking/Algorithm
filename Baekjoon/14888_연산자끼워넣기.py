import itertools
import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
opr_num = list(map(int, sys.stdin.readline().split()))
opr = []
# 1 == +, 2 == -, 3 == *, 4 == /
for i in range(4):
    while opr_num[i] != 0:
        opr.append(i + 1)
        opr_num[i] -= 1

perm = list(set(itertools.permutations(opr, N - 1))) #중복제거해주니까 통과했음 기존에 list론 통과안댐
rest = num[1:]
min = 1000000000
max = -1000000000
for i in range(len(perm)):
    ans = num[0]
    tmp = list(zip(perm[i], rest))
    for j in range(N - 1):
        if tmp[j][0] == 1:
            ans += tmp[j][1]
        if tmp[j][0] == 2:
            ans -= tmp[j][1]
        if tmp[j][0] == 3:
            ans *= tmp[j][1]
        if tmp[j][0] == 4:
            ans = int(ans / tmp[j][1])
    if ans > max:
        max = ans
    if ans < min:
        min = ans

print(max, min, sep='\n')