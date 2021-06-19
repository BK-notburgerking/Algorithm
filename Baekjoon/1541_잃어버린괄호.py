calc = input().split('-')
arr = []

for c in calc:
    if '+' in c:
        tmp = map(int, c.split('+'))
        arr.append(sum(tmp))
    else:
        c = int(c)
        arr.append(c)

ans = arr[0]
if len(arr) > 1:
    for i in range(1, len(arr)):
        ans -= arr[i]

print(ans)