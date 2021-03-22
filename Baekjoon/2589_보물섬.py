from collections import deque
from copy import deepcopy

def bfs(i, j):
    max = 0
    q = deque()
    q.append((i, j))
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < H and 0 <= nc < W:
                if t_map[nr][nc] == 'L' and dis[nr][nc] == -1:
                    dis[nr][nc] = dis[r][c] + 1
                    q.append((nr, nc))
                    if dis[nr][nc] > max:
                        max = dis[nr][nc]
    return max


H, W = map(int, input().split())
t_map = [input() for _ in range(H)]
original = [([-1] * W) for _ in range(H)]
dis = deepcopy(original)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
ans = 0

for i in range(H):
    for j in range(W):
        if t_map[i][j] == 'L':
            dis[i][j] = 0
            tmp = bfs(i, j)
            if tmp > ans:
                ans = tmp
            dis = deepcopy(original)

print(ans)