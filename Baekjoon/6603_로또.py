import sys

def comb(idx, start):
    if idx == 6:
        print(*sel)
    else:
        for i in range(start, N):
            if visit[i] == 0:
                sel[idx] = numbers[i]
                visit[i] = 1
                comb(idx + 1, i + 1)
                visit[i] = 0

while True:
    numbers = list(map(int, sys.stdin.readline().split()))
    if numbers == [0]:
        break
    N = numbers[0]
    numbers = numbers[1:]
    sel = [0] * 6
    visit = [0] * N
    tmp = []
    comb(0, 0)
    print('')