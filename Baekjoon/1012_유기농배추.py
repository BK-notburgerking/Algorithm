import sys; input = sys.stdin.readline
from collections import deque

def bfs(r, c):
    q = deque()
    q.append([r, c])
    while q:
        r, c = q.popleft()
        arr[r][c] = 2
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < H and 0 <= nc < W:
                if arr[nr][nc] == 1:
                    arr[nr][nc] = 2
                    q.append([nr, nc])

for tc in range(int(input())):

    W, H, K = map(int, input().split())
    start = []
    arr = [([0] * W) for _ in range(H)]
    ans = 0
    for _ in range(K):
        C, R = map(int, input().split())
        start.append((R, C))
        arr[R][C] = 1

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    for cabbage in start:
        r, c = cabbage
        if arr[r][c] == 1:
            bfs(r, c)
            ans += 1

    print(ans)