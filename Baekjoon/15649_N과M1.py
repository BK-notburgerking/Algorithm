def perm(idx):
    if idx == M:
        print(' '.join(map(str, order)))
    else:
        for i in range(N):
            if visit[i] == 0:
                order[idx] = arr[i]
                visit[i] = 1
                perm(idx + 1)
                visit[i] = 0

N, M = map(int, input().split())
arr = [i for i in range(1, N + 1)]
order = [0] * M # 수열을 넣을 리스트 / 길이가 M인 수열을 구할거임
visit = [0] * N # 해당 요소를 사용했는지 체크

perm(0)