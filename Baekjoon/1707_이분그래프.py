import sys; input = sys.stdin.readline
from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    color[start] = 1
    while q:
        u = q.popleft()
        for v in G[u]:
            if color[v] == 0:
                color[v] = color[u] * -1
                q.append(v)
            elif color[v] == color[u]:
                return True # 이분불가능
    return False

for tc in range(int(input())):

    V, E = map(int, input().split())
    G = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)

    color = [0] * (V + 1)
    ans = False
    for i in range(1, V + 1):
        if color[i] == 0:
            ans = bfs(i)
            if ans: # 이분불가능하면
                break

    if ans:
        print('NO')
    else:
        print('YES')