import sys
sys.setrecursionlimit(100000) #없으면 recursion error 발생

def dfs(r, c):
    global cnt
    visit[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < M and 0 <= nc < N and visit[nr][nc] == 0:
            cnt += 1
            dfs(nr, nc)

M ,N, K = map(int, input().split())

visit = [[0] * N for _ in range(M)]

for _ in range(K):
    sc, sr, ec, er = map(int, input().split()) #굳이 뒤집지 않음 상하 반전이지만 어차피 모양은 똑같을테니까
    for i in range(sr, er):
        for j in range(sc, ec):
            visit[i][j] = 1

#12시부터 시계방향
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
cnt = 1 #넓이
area = 0 #영역의 갯수
ans = []

for i in range(M):
    for j in range(N):
        if visit[i][j] == 0:
            area += 1
            dfs(i, j)
            ans.append(cnt)
            cnt = 1

ans.sort()
print(area)
print(' '.join(map(str,ans)))