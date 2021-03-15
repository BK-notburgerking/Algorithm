import sys
sys.setrecursionlimit(100000)

def dfs(r, c, color, status):
    if status == 'nomal':
        nomal_visit[r][c] = 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if nomal_visit[nr][nc] == 0 and rgb[nr][nc] == color:
                    dfs(nr, nc, color, 'nomal')

    if status == 'abnomal':
        abnomal_visit[r][c] = 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if color == 'R' or color == 'G':
                    if abnomal_visit[nr][nc] == 0 and (rgb[nr][nc] == 'R' or rgb[nr][nc] == 'G'):
                        dfs(nr, nc, color, 'abnomal')
                else:
                    if abnomal_visit[nr][nc] == 0 and rgb[nr][nc] == color:
                        dfs(nr, nc, color, 'abnomal')

N = int(input())
rgb = [input() for _ in range(N)]

nomal_visit = [([0] * N) for _ in range(N)]
abnomal_visit = [([0] * N) for _ in range(N)]
nomal_cnt = abnomal_cnt = 0

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for i in range(N):
    for j in range(N):
        if nomal_visit[i][j] == 0:
            dfs(i, j, rgb[i][j], 'nomal')
            nomal_cnt += 1
        if abnomal_visit[i][j] == 0:
            dfs(i, j, rgb[i][j], 'abnomal')
            abnomal_cnt += 1

print(nomal_cnt, abnomal_cnt)