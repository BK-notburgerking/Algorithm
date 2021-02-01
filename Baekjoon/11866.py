# https://www.acmicpc.net/problem/11866
# 요세푸스 문제 0

josephus = list(map(int, input().split()))
pick = josephus[1] - 1
circle = []
answer = []

for person in range(1, josephus[0]+1):
    circle.append(person)

while len(circle) != 1:
    for i in range(pick):
        circle.append(circle.pop(0))
    answer.append(circle.pop(0))
answer.append(circle.pop(0))


print('<' + ', '.join(map(str, answer)) + '>')