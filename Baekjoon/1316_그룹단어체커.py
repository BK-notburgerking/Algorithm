N = int(input())
cnt = 0
for _ in range(N):
    txt = input()
    check = [0]
    for i in range(len(txt)):
        if txt[i] != check[-1]:
            if txt[i] in check:
                break
            else:
                check += txt[i]
    else:
        cnt += 1
print(cnt)
