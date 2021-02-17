# import sys
#
# ages = []
# names = []
# ans = []
# n = int(input())
# for _ in range(n):
#     age, name = sys.stdin.readline().split()
#     ages.append(int(age))
#     names.append(name)
#
# for i in range(n-1):
#     for j in range(n-2, -1 + i, -1):
#         if ages[j] > ages[j+1]:
#             ages[j], ages[j+1] = ages[j+1], ages[j]
#             names[j], names[j+1] = names[j+1], names[j]
#
# for k in range(n):
#     ans.append(str(ages[k]) + ' ' + names[k])
#
# print('\n'.join(ans))

###

# import sys
#
# dic = {}
# n = int(input())
# for _ in range(n):
#     age, name = sys.stdin.readline().split()
#     dic[name] = age
#
# sortdic = sorted(dic.items(), key = lambda x : x[1])
#
# print(sortdic)
#
# for i in range(n):
#     print(sortdic[i][1] + ' ' +sortdic[i][0])

###

import sys

ans = []
n = int(input())
for _ in range(n):
    age, name = sys.stdin.readline().split()
    ans.append([age, name])
ans.sort(key = lambda x : int(x[0]))

for i in range(n):
    print(ans[i][0], ans[i][1])