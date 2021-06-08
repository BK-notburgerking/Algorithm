import sys; input = sys.stdin.readline

def check(r, c):
    global ans
    tmp1, tmp2 = 0, 0
    for i in range(8):
        for j in range(8):
            nr, nc = r + i, c + j
            if board[nr][nc] != sol1[i][j]:
                tmp1 += 1
            if board[nr][nc] != sol2[i][j]:
                tmp2 += 1
            if tmp1 >= ans and tmp2 >= ans:
                return
    ans = min(ans, tmp1, tmp2)

N, M = map(int, input().split())
board = [input() for _ in range(N)]
sol1 = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']
sol2 = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']
ans = 65

end_r = N - 8
end_c = M - 8

for i in range(end_r + 1):
    for j in range(end_c + 1):
        check(i, j)

print(ans)