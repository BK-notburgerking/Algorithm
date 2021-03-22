import sys
sys.setrecursionlimit(100000)

def dfs(r, c, rain):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N:
            if visit[nr][nc] == 0 and land[nr][nc] > rain:
                visit[nr][nc] = 1
                dfs(nr, nc, rain)


N = int(input())
land = [list(map(int, input().split())) for _ in range(N)]
top = max(map(max, land))
visit = [([0] * N) for _ in range(N)]
maxi = 0
tmp = 0
rain = 0

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for _ in range(top + 1):
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0 and land[i][j] > rain:
                visit[i][j] = 1
                tmp += 1
                dfs(i, j, rain)
    if tmp >= maxi:
        maxi = tmp
    visit = [([0] * N) for _ in range(N)]
    tmp = 0
    rain += 1

print(maxi)