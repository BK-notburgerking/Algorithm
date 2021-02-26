N = int(input())
box = [[0] * 101 for _ in range(101)]

color = 1
for i in range(N):
    c, r, w, h = map(int, input().split())
    r = 100 - r
    for j in range(h):
        for k in range(w):
            box[r - j][c + k] = color # 입력은 0이지만 인덱스상에서 100부터 올라가므로 r - j가 맞음
    color += 1

ans = [0] * N
for i in range(101):
    for j in range(101):
        for k in range(1, N + 1):
            if box[i][j] == k:
                ans[k - 1] += 1

print('\n'.join(map(str, ans)))