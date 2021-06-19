import sys; input = sys.stdin.readline
from collections import deque

def bfs(root):
    q = deque()
    q.append(root)
    while q:
        p = q.popleft()
        for c in adj[p]:
            if not visit[c]:
                visit[c] = 1
                ans[c] = p
                q.append(c)

N = int(input())
adj = [[] for _ in range(N + 1)]
ans = [[] for _ in range(N + 1)]
visit = [0] * (N + 1)
for _ in range(N - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

visit[1] = 1
bfs(1)
print('\n'.join(map(str, ans[2:])))