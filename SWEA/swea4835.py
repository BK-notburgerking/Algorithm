n = int(input())
for tc in range(1, n+1):

    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    tmp = []
    i = 0

    while i < (N - M + 1):
        total = 0
        for j in range(M):
            total += lst[i + j]
        tmp.append(total)
        i += 1

    min = tmp[0]
    max = tmp[0]

    for k in range(len(tmp)):
        if tmp[k] < min:
            min = tmp[k]
        if tmp[k] > max:
            max = tmp[k]
    
    answer = max - min

    print(f'#{tc} {answer}')