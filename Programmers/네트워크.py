from collections import deque

def solution(n, computers):
    ans = 0
    visit = [0] * (n + 1)
    q = deque()
    for i in range(n):
        if not visit[i]:
            ans += 1
            visit[i] = 1
            q.append(i)
            while q:
                r = q.popleft()
                for c in range(n):
                    if r == c: continue
                    if computers[r][c] == 1 and not visit[c]:
                        visit[c] = 1
                        q.append(c)
    return ans