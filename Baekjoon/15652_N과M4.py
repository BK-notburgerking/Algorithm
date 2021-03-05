def perm(idx, j):
    if idx == M:
        print(' '.join(map(str, sel)))
    else:
        for i in range(j, N):
                sel[idx] = arr[i]
                perm(idx + 1, i)

N, M = map(int, input().split())
arr = [i for i in range(1, N + 1)]
sel = [0] * M

perm(0, 0)