from collections import deque
import sys; input = sys.stdin.readline

board = [0] * 101
dis = [101] * 101
l, s = map(int, input().split())
for _ in range(l + s):
    s, e = map(int, input().split())
    board[s] = e

q = deque()
q.append(1)
dis[1] = 0

while q:
    v = q.popleft()
    for i in range(1, 7):
        w = v + i
        if 1 < w < 101 and dis[w] == 101:
            if board[w]:
                w = board[w]
            if dis[w] == 101:
                dis[w] = dis[v] + 1
                q.append(w)

print(dis[-1])