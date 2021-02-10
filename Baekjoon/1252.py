#이진수 덧셈
#https://www.acmicpc.net/problem/1252

binary = list(map(int, input().split(' ')))
sum = str(binary[0] + binary[1])

bin = [0]
for n in sum:
    bin.append(int(n))

for i in range(len(bin)-1, 0, -1):
    if bin[i] >= 2:
        bin[i] -= 2
        bin[i-1] += 1

if bin[0] == 0:
    bin = bin[1:]

print(''.join(map(str, bin)))