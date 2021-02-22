import sys
ans = []
N = int(input())
road = list(map(int, sys.stdin.readline().split()))
hill = 0
tmp = []

for i in range(N - 1):
    if road[i] < road[i + 1]:
        hill += (road[i + 1] - road[i])
    if road[i] >= road[i + 1]:
        tmp.append(hill)
        hill = 0
tmp.append(hill)

print(max(tmp))