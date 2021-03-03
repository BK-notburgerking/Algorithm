def dfs(r, c):
    global cnt
    visit[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        #범위를 벗어나지 않고 방문한적이 없는 곳에 대해서 탐색하여 cnt수 늘림
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != '0' and visit[nr][nc] == 0:
            visit[nr][nc] = 1
            cnt += 1
            dfs(nr, nc)
    return cnt

N = int(input())
arr = [input() for _ in range(N)]

#12시부터 시계방향
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
visit = [[0] * N for _ in range(N)]
cnt = 1 #단지내 아파트 개수
ans = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == '1' and visit[i][j] == 0: # 집이 있고 방문하지 않은 단지일 경우에만 탐색
            home = dfs(i, j)
            ans.append(home)
            cnt = 1 # 다음 탐색을 위해 cnt 초기화

ans.sort()
print(len(ans))
print('\n'.join(map(str, ans)))