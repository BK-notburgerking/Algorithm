import sys; input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]
bacon = 0xfffffff
ans = 101
for i in range(M):
    u, v = map(int, input().split())
    adj[u].append([u, v])
    adj[v].append([v, u])

for i in range(1, N + 1):
    dis = [-1] * (N + 1)
    dis[0], dis[i] = 0, 0
    q = deque()
    q.extend(adj[i])
    while q:
        s, e = q.popleft()
        if dis[e] == -1:
            dis[e] = dis[s] + 1
            q.extend(adj[e])

    if sum(dis) < bacon:
        bacon = sum(dis)
        ans = i

print(ans)