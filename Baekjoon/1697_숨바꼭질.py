from collections import deque

def bfs(q):
    while q:
        v = q.popleft()
        if v == K:
            return dis[K]
        for next in (v + 1, v - 1, v * 2):
            if 0 <= next < 100001 and dis[next] == 0:
                dis[next] = dis[v] + 1
                q.append(next)

N, K = map(int, input().split())
dis = [0] * 100001

q = deque([N])
print(bfs(q))