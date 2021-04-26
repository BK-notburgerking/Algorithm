import sys; input = sys.stdin.readline
from heapq import heappush, heappop

def dijkstra(start):
    dis = [3000000] * (V + 1) # 거리 초기화
    visit = [0] * (V + 1) # 방문 초기화
    dis[start] = 0 # 시작노드까지 거리 0으로 초기화
    q = [[0 ,start]] # 시작노드 가중치, 시작 노드

    while q:
        k, u = heappop(q) # 현재정점까지의 거리, 현재 정점
        if visit[u]: continue # 현재 정점 방문 처음이면
        visit[u] = 1 # 방문처리
        for w, v in G[u]: # 현재 정점에서 인점 정점까지 거리 탐색
            # 인접정점 방문 안했고, 인접정점까지의 거리가 (현재정점까지 거리 + 인접정점으로 이동거리)보다 작으면
            if not visit[v] and dis[v] > dis[u] + w:
                dis[v] = dis[u] + w # 인접정점의 거리 = 현재 정점까지의 거리 + 인접 정점으로 이동거리
                heappush(q, [dis[v], v])
    return dis

V, E = map(int, input().split())
K = int(input())
G = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append([w, v]) # 유향그래프

ans = dijkstra(K)
for i in range(1, len(ans)):
    if ans[i] == 3000000:
        print('INF')
    else:
        print(ans[i])