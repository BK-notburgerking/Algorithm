import sys

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
dic = {}
ans = []

for card in cards:
    if card in dic:
        dic[card] += 1
    else:
        dic[card] = 1

for number in numbers:
    if number in dic:
        ans.append(dic[number])
    else:
        ans.append(0)

print(' '.join(map(str, ans)))