def perm(idx, j, total):
    global ans

    if total > 100:
        return

    if idx == 7:
        if total == 100:
            ans = sorted(sel)

    else:
        for i in range(j, 9):
            if visit[i] == 0:
                visit[i] = 1
                sel[idx] = dwarves[i]
                perm(idx + 1, j + 1, total + dwarves[i])
                visit[i] = 0


dwarves = [int(input()) for _ in range(9)]
visit = [0] * 9
sel = [0] * 7
ans = []
perm(0, 0, 0)
print('\n'.join(map(str, ans)))