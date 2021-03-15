import sys
sys.setrecursionlimit(100000)

def dfs(r, c, color, status):
    if status == 'normal':
        normal_visit[r][c] = 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if normal_visit[nr][nc] == 0 and rgb[nr][nc] == color:
                    dfs(nr, nc, color, 'normal')

    if status == 'abnormal':
        abnormal_visit[r][c] = 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if color == 'R' or color == 'G':
                    if abnormal_visit[nr][nc] == 0 and (rgb[nr][nc] == 'R' or rgb[nr][nc] == 'G'):
                        dfs(nr, nc, color, 'abnormal')
                else:
                    if abnormal_visit[nr][nc] == 0 and rgb[nr][nc] == color:
                        dfs(nr, nc, color, 'abnormal')

N = int(input())
rgb = [input() for _ in range(N)]

normal_visit = [([0] * N) for _ in range(N)]
abnormal_visit = [([0] * N) for _ in range(N)]
normal_cnt = abnormal_cnt = 0

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for i in range(N):
    for j in range(N):
        if normal_visit[i][j] == 0:
            dfs(i, j, rgb[i][j], 'normal')
            normal_cnt += 1
        if abnormal_visit[i][j] == 0:
            dfs(i, j, rgb[i][j], 'abnormal')
            abnormal_cnt += 1

print(normal_cnt, abnormal_cnt)