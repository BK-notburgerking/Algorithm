import sys

def div(r, c, N):
    global W, B
    for i in range(r, r+N):
        for j in range(c, c+N):
            if paper[r][c] != paper[i][j]:
                div(r, c, N//2) #1사분면
                div(r, c + N//2, N//2) #2사분면
                div(r + N//2, c + N//2, N//2) #3사분면
                div(r + N//2, c, N//2) #4사분면
                return

    if paper[r][c] == 0:
        W += 1
        return
    else:
        B += 1
        return

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
W = 0
B = 0
div(0, 0, N)
print(W, B, sep=('\n'))