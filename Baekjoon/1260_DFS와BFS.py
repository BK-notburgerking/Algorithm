from collections import deque

def dfs(s):
    visit = [0] * (N + 1)
    search = []
    stack = []
    stack.append(s)
    visit[s] = 1
    while stack:
        v = stack.pop()
        for w in g[v]:
            if visit[w] == 0:
                stack.append(w)
        visit[v] = 1
        if v not in search: #마지막요소가 2개씩 들어가는 일이 발생해서 이를 막아줌
            search.append(v)
    return search

def bfs(s):
    visit = [0] * (N + 1)
    search = [V]
    q = deque()
    q.append(s)
    visit[s] = 1
    while q:
        v = q.popleft()
        for w in g[v]:
            if visit[w] == 0:
                visit[w] = 1
                q.append(w)
                search.append(w)
    return search

#정점 간선 시작점
N, M, V = map(int, input().split())

g = [[] for _ in range(10001)]

for _ in range(M):
    v, w = map(int, input().split())
    g[v].append(w)
    g[w].append(v)

for i in range(M + 1): #dfs는 스택을 사용하므로 reverse 해줘야 작은것부터 꺼내서 탐색함
    g[i].sort(reverse= True)

print(' '.join(map(str, dfs(V))))

for i in range(M + 1): #정점 번호가 작은 것을 먼저 방문하기 위해 연결리스트를 정렬시킴
    g[i].sort()

print(' '.join(map(str, bfs(V))))
