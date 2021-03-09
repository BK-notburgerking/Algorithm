import sys
from collections import deque

def bfs(q):
    global maxd
    dr = [-1, 0 , 1 ,0]
    dc = [0, 1, 0, -1]

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and box[nr][nc] == 0:
                box[nr][nc] = 1
                distance[nr][nc] = distance[r][c] + 1
                q.append([nr, nc])

                if distance[nr][nc] > maxd:
                    maxd = distance[nr][nc]

def check(arr):
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                return -1


M, N = map(int, sys.stdin.readline().split())
box = []
q = deque()
distance = [([0] * M) for _ in range(N)]
maxd = 0

for i in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(M):
        if tmp[j] == 1:
            q.append([i, j]) #익은 토마토가 있는 곳을 큐에다가 담아서 큐 채로 bfs에 넘겨줌
    box.append(tmp)

bfs(q)
if check(box) == -1:
    print(-1)
else:
    print(maxd)