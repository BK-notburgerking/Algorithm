numbers = list(map(int, input().replace('9', '6')))
max = 0
dic = {}

for number in numbers: 
    if dic.get(number) == None:
        dic[number] = 1
    else:
        dic[number] += 1

if dic.get(6) != None:
    dic[6] = (dic[6]+1) // 2

for key, val in dic.items(): #
    if max < val:
        max = val

print(max)




## 시도 3
# numbers = list(map(int, input()))
# dic = {}
# max = 0

# for number in numbers: 
#     if dic.get(number) == None:
#         dic[number] = 1
#     else:
#         dic[number] += 1

# if dic.get(6) != None:
#     dic[6] = (dic[6]+1) // 2
#     if dic.get(9) != None:
#         dic[6] += (dic[9]+1) // 2
#         dic[9] = 0
# if dic.get(9) != None:
#     dic[9] = (dic[9]+1) // 2

# for key, val in dic.items(): #
#     if max < val:
#         max = val

# print(max)

##시도2
#왜안되지 한참고민했음 도저히 찾을수가 없어서..
#결국 종백님께 헬프를 쳤고
#귀신같이 찾아주심..
#만약 9999인 경우에
#아래에서 3번째줄 if max < ((same + 1)//2): 를 실행하기전에
#이미 바로 그 위의 코드
#     if max < val:
#         max = val
#에서 맥스값이 결정돼버림
#따라서 그 밑에 비교하는 코드가 원하는대로 작동하지 않음
#순서가 틀린거지 순서가..
# numbers = list(map(int, input()))
# dic = {}
# max = 0
# same = 0

# for number in numbers: #딕셔너리로 만들어 숫자가 몇개씩 나오는지 key:val로 만듦 
#     if dic.get(number) == None:
#         dic[number] = 1
#     else:
#         dic[number] += 1

# for key, val in dic.items(): #
#     if key == 6 or key == 9:
#         same += val
#     if max < val:
#         max = val
#         if max < ((same + 1)//2):
#             max = (same + 1)//2
# print(max)


