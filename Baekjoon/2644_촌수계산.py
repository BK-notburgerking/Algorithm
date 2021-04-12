import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, end):
    q = deque()
    q.append(start)
    while q:
        vs = q.popleft()
        for v in link[vs]:
            if visit[v] == -1:
                visit[v] = visit[vs] + 1
                if v == end:
                    return visit[v]
                q.append(v)
    return -1

n = int(input())
start, end = map(int, input().split())
m = int(input())
link = [[] for _ in range(n + 1)]
visit = [-1] * (n + 1)

for i in range(m):
    p, c = map(int, input().split())
    link[p].append(c)
    link[c].append(p)

visit[start] = 0
print(bfs(start, end))