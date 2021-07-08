import sys; input = sys.stdin.readline
from collections import deque

def bfs(r, c):
    global mini, maxi
    q = deque()
    q.append((r, c))
    union_list = [(r, c)]
    population_total = population[r][c]
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if (0 <= nr < N and 0 <= nc < N) and not visit[nr][nc]:
                if mini <= abs(population[r][c] - population[nr][nc]) <= maxi:
                    visit[nr][nc] = 1
                    q.append((nr, nc))
                    union_list.append((nr, nc))
                    population_total += population[nr][nc]

    if len(union_list) > 1:
        for r, c in union_list:
            population[r][c] = population_total // len(union_list)
            next_q.append((r, c))
        return True
    return False

N, mini, maxi = map(int, input().split())
population = [list(map(int, input().split())) for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

next_q = deque()
for i in range(N):
    for j in range(N):
        next_q.append((i, j))

ans = 0
while True:
    moved = False
    visit = [([0] * N) for _ in range(N)]
    for _ in range(len(next_q)):
        i, j = next_q.popleft()
        if not visit[i][j]:
            visit[i][j] = 1
            if bfs(i, j):
                moved = True

    if not moved:
        break

    ans += 1

print(ans)