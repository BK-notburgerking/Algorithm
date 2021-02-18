N = int(input())
for tc in range(1, N+1):
    c = int(input())
    lst = list(map(int, input().split()))

    max = lst[0]
    min = lst[0]
    for i in range(1, c):
        if lst[i] > max:
            max = lst[i]
        if lst[i] < min:
            min = lst[i]
    answer = max - min

    print(f'#{tc} {answer}')
