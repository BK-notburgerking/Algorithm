import sys; input = sys.stdin.readline
from collections import deque

def bfs(r, c):
    breaking[r][c] = 0
    q = deque()
    q.append((r, c))
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < height and 0 <= nc < width:
                if breaking[nr][nc] == -1:
                    if maze[nr][nc] == '1':
                        breaking[nr][nc] = breaking[r][c] + 1
                        q.append((nr, nc))
                    if maze[nr][nc] == '0':
                        breaking[nr][nc] = breaking[r][c]
                        q.appendleft((nr, nc))

width, height = map(int, input().split())
maze = [input() for _ in range(height)]
breaking = [([-1] * width) for _ in range(height)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

bfs(0, 0)
print(breaking[height - 1][width - 1])