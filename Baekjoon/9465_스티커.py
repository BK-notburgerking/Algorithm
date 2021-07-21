for _ in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]
    memo = [arr[0][0], arr[0][1]]

    for c in range(1, n):
        for r in range(2):
            print(arr[r][c])