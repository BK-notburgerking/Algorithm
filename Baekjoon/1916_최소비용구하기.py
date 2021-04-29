import sys; input = sys.stdin.readline
from heapq import heappush, heappop

def dijkstra(start, end):
    dis = [100000000] * (N + 1)
    dis[start] = 0
    q = [[0, start]]
    while q:
        k, u = heappop(q)
        if k > dis[u]: continue
        for w, v in G[u]:
            if dis[v] > w + dis[u]:
                dis[v] = w + dis[u]
                heappush(q, [dis[v], v])

    return dis[end]

N = int(input())
M = int(input())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    G[u].append([w, v])
start, end = map(int, input().split())

print(dijkstra(start, end))