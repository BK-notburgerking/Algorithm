import sys
from collections import deque

def bfs(q):
    global maxd
    # 위 아래 북 동 남 서
    dh = [-1, 1, 0, 0, 0, 0]
    dr = [0, 0, -1, 0, 1, 0]
    dc = [0, 0, 0, 1, 0, -1]

    while q:
        h, r, c = q.popleft()
        for i in range(6):
            nh = h + dh[i]
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M and box[nh][nr][nc] == 0:
                box[nh][nr][nc] = 1
                distance[nh][nr][nc] = distance[h][r][c] + 1
                q.append([nh, nr, nc])

                if distance[nh][nr][nc] > maxd:
                    maxd = distance[nh][nr][nc]


def check(arr):
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if arr[i][j][k] == 0:
                    return -1

#가로 세로 높이
M, N, H = map(int, sys.stdin.readline().split())
floor = [] #층
box = [] #전체
q = deque() #탐색을 시작할 좌표
distance = [[[0] * M for _ in range(N)] for __ in range(H)] #거리체크
maxd = 0 #최대거리


for h in range(H):
    for r in range(N):
        floor.append(list(map(int, sys.stdin.readline().split())))
        for c in range(M):
            if floor[r][c] == 1:
                q.append([h, r, c])
    box.append(floor)
    floor = []

bfs(q)
if check(box) == -1:
    print(-1)
else:
    print(maxd)
