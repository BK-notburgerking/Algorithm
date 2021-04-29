import sys; input = sys.stdin.readline
from heapq import heappush, heappop

def dijkstra(start, end):
    dis = [10000000] * (N + 1)
    visit = [0] * (N + 1)
    dis[start] = 0
    q = [[0, start]]
    while q:
        k, u = heappop(q)
        if visit[u] or k > dis[u]: continue
        visit[u] = 1
        for w, v in G[u]:
            if dis[v] > w + dis[u] and not visit[v]:
                dis[v] = w + dis[u]
                heappush(q, [dis[v], v])

    return dis[end]

N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    G[u].append([w, v])
    G[v].append([w, u])

for _ in range(M):
    start, end = map(int, input().split())
    print(dijkstra(start ,end))