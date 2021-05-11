import sys; input = sys.stdin.readline

def move_dust():
    moving = []
    for i in range(R):
        for j in range(C):
            if room[i][j] > 0:
                r, c = i, j
                minus_dust = 0
                dif = room[r][c] // 5
                if 0 <= r - 1 < R and 0 <= c < C and room[r - 1][c] >= 0:
                    minus_dust += dif
                    moving.append((r - 1, c, dif))
                if 0 <= r < R and 0 <= c + 1 < C and room[r][c + 1] >= 0:
                    minus_dust += dif
                    moving.append((r, c + 1, dif))
                if 0 <= r + 1 < R and 0 <= c < C and room[r + 1][c] >= 0:
                    minus_dust += dif
                    moving.append((r + 1, c, dif))
                if 0 <= r < R and 0 <= c - 1 < C and room[r][c - 1] >= 0:
                    minus_dust += dif
                    moving.append((r, c - 1, dif))
                room[r][c] -= minus_dust

    while moving:
        r, c, plus_dust = moving.pop()
        room[r][c] += plus_dust

def start_clean(cleaner):
    for i in range(2):
        if i == 0:
            clean = cleaner[0][0]
            room[clean - 1][0] = 0
            for r in range(clean - 2, -1, -1):
                room[r + 1][0] = room[r][0]
                room[r][0] = 0
            for c in range(1, C):
                room[0][c - 1] = room[0][c]
                room[0][c] = 0
            for r in range(1, clean + 1):
                room[r - 1][C - 1] = room[r][C - 1]
                room[r][C - 1] = 0
            for c in range(C - 2, 0, -1):
                room[clean][c + 1] = room[clean][c]
                room[clean][c] = 0
        if i == 1:
            clean = cleaner[1][0]
            room[clean + 1][0] = 0
            for r in range(clean + 2, R):
                room[r - 1][0] = room[r][0]
                room[r][0] = 0
            for c in range(1, C):
                room[R - 1][c - 1] = room[R - 1][c]
                room[R - 1][c] = 0
            for r in range(R - 2, clean - 1, -1):
                room[r + 1][C - 1] = room[r][C - 1]
                room[r][C - 1] = 0
            for c in range(C - 2, 0, -1):
                room[clean][c + 1] = room[clean][c]
                room[clean][c] = 0

def count_dust():
    total = 0
    for i in range(R):
        for j in range(C):
            if room[i][j] > 0:
                total += room[i][j]
    return total

R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]
cleaner = []

for i in range(2, R - 1):
    if room[i][0] == -1:
        cleaner.append([i, 0])

for t in range(T):
    move_dust()
    start_clean(cleaner)

print(count_dust())