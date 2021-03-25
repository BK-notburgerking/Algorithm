def cal(a, b, cnt):
    global ans
    if a > b:
        return
    if a == b:
        ans = cnt + 1
        return
    else:
        cal(a * 2, b, cnt + 1)
        cal((a * 10) + 1, b, cnt + 1)


A, B = map(int, input().split())
ans = -1
cal(A, B, 0)
print(ans)