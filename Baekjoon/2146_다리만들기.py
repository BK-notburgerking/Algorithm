from collections import deque

def bfs1(r, c, land):
    q = deque()
    q.append((r, c))
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if visited[nr][nc] == 0 and arr[nr][nc] == 1: #방문안했고 땅이면
                    visited[nr][nc] = land
                    q.append((nr, nc))
                elif visited[nr][nc] == 0 and arr[nr][nc] == 0: #방문안했고 땅 옆에 붙어있는 바다면


                    end.append((r, c)) #땅의 끝

def bfs2(end):
    cnt = 0 #반복횟수
    ans = 987654321
    while end:
        cnt += 1
        for _ in range(len(end)):
            r, c = end.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < N:
                    if visited[nr][nc] == 0 or visited[nr][nc] == 1: #바다거나 땅옆에 있는 바다
                        visited[nr][nc] = visited[r][c] #땅 확장
                        end.append((nr, nc))
                    elif visited[nr][nc] != visited[r][c]: #우리땅 아님
                        if visited[nr][nc] < visited[r][c]:
                            ans = min(((cnt - 1) * 2), ans)
                        if visited[nr][nc] > visited[r][c]:
                            ans = min(((cnt * 2) - 1), ans)
    return ans

N = int(input())
arr = [] #지도
end = deque() #육지의 끝에 붙어있는 바다 (다리의 시작점)
land = -1 #육지 분리해서 표시하기 위함
visited = [([0] * N) for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for _ in range(N):
    arr.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = land
            bfs1(i, j, land)
            land -= 1

print(bfs2(end))