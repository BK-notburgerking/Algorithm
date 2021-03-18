def check(r, c):
    for row in range(r):
        if c == board[row]:
            return False
        if r - c == row - board[row]:
            return False
        if r + c == row + board[row]:
            return False
    return True

def bt(idx):
    global ans

    if idx == N:
        ans += 1

    else:
        for i in range(N):
            if check(idx, i):
                board[idx] = i
                bt(idx + 1)
                board[idx] = 0


N = int(input())
board = [0] * N
ans = 0

bt(0)
print(ans)