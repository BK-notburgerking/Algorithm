# 1206 view
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV134DPqAA8CFAYh&categoryId=AV134DPqAA8CFAYh&categoryType=CODE&problemTitle=1206&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

for test in range(10):
    n = int(input())
    apt = list(map(int, input().split()))
    answer = 0

    for i in range(2, n-2):
        tmp = apt[i-2:i+3]
        mini = min(tmp[2]-tmp[0], tmp[2]-tmp[1], tmp[2]-tmp[3], tmp[2]-tmp[4])
        if mini > 0:
            answer += mini
    test += 1

    print('#%s ' % test +str(answer))