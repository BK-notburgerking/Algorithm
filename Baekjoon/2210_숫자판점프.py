def bt(r, c, num):
    num += arr[r][c]
    if len(num) == 6:
        ans.add(num)
        return
    else:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < 5 and 0 <= nc < 5:
                bt(nr, nc, num)

arr = [input().split() for _ in range(5)]

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)
ans = set()

for i in range(5):
    for j in range(5):
        bt(i, j, '')

print(len(ans))