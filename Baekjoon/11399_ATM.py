#ATM
#https://www.acmicpc.net/problem/11399

# N = int(input())
# time = list(map(int, input().split(' ')))
# person = {}
# before = 0
# answer = 0
#
# for idx, val in enumerate(time):
#     person[idx+1] = val
#
# person = sorted(person.items(), key=lambda x: x[1])
#
# for i in range(len(person)):
#     before += person[i][1]
#     answer += before
#
# print(answer)


N = int(input())
time = sorted(list(map(int, input().split())))
tmp = 0
answer = 0

for t in time:
    tmp += t
    answer += tmp

print(answer)