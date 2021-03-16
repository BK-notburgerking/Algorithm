def fac(n):
    ini = 1
    for i in range(1, n + 1):
        ini *= i
    return ini

def score_count(idx, j):
    global cnt, min_score

    if idx == (N // 2):
        if cnt < comb_num:
            cnt += 1
            start = sel
            link = list(set(person) - set(start))
            start_score = 0
            link_score = 0
            for i in range(N // 2):
                for j in range(N // 2):
                    start_score += arr[start[i]][start[j]]
                    link_score += arr[link[i]][link[j]]
            dif = abs(start_score - link_score)
            if dif < min_score:
                min_score = dif

    else:
        for i in range(j, N):
            if visit[i] == 0:
                visit[i] = 1
                sel[idx] = person[i]
                score_count(idx + 1, i + 1)
                visit[i] = 0

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

person = [i for i in range(N)]
visit = [0] * N
sel = [0] * (N // 2)
cnt = 0 #조합 완성 갯수
min_score = 999999999
comb_num = (fac(N) / (fac(N // 2) * 2) // 2) #nCr

score_count(0, 0)
print(min_score)