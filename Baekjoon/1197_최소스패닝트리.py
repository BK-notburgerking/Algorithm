from heapq import heappush, heappop

def prim(start, weight):
    visit = [0] * (V + 1)
    key = [2147483648] * (V + 1)
    key[start] = 0
    q = [[weight, start]]
    ans = 0
    while q:
        k, v = heappop(q)
        if visit[v]: continue
        visit[v] = 1
        ans += k
        for u, w in G[v]:
            if not visit[u] and key[u] > w:
                key[u] = w
                heappush(q, [w, u])
    return ans

V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append([v, w])
    G[v].append([u, w])

print(prim(1, 0))