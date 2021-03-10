def blackjack(idx, j):
    if idx == 3:
        if sum(sel) <= M:
            maxi.append(sum(sel))
    else:
        for i in range(j, N):
            if visit[i] == 0:
                visit[i] = 1
                sel[idx] = cards[i]
                blackjack(idx + 1, i + 1)
                visit[i] = 0

N, M = map(int, input().split())
cards = list(map(int, input().split()))
visit = [0] * N
sel = [0] * 3
maxi = []

blackjack(0, 0)
print(max(maxi))