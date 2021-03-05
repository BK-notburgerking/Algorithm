def perm(idx, j):
    if idx == M:
        print(' '.join(map(str, select)))
    else:
        for i in range(j, N):
            if visit[i] == 0:
                visit[i] = 1
                select[idx] = arr[i]
                perm(idx + 1, i + 1)
                visit[i] = 0


N, M = map(int, input().split())
arr = [i for i in range(1, N + 1)]
select = [0] * M
visit = [0] * N

perm(0, 0)