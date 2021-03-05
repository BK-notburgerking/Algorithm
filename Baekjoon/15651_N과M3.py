def perm(idx):
    if idx == M:
        print(' '.join(map(str, sel)))
    else:
        for i in range(N):
            sel[idx] = arr[i]
            perm(idx + 1)

N, M = map(int, input().split())
arr = [i for i in range(1, N + 1)]
sel = [0] * M

perm(0)