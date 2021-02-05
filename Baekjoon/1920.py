import sys

N = input()
arr_n = list(map(int, sys.stdin.readline().split()))
arr_n.sort()
M = input()
arr_m = list(map(int, sys.stdin.readline().split()))

def bs(arr, number):
    s = 0
    e = len(arr) - 1
    while s <= e:
        mid = (s + e) // 2
        if arr[mid] == number:
            return True
        elif arr[mid] > number:
            e = mid -1
        else:
            s = mid +1
    return False

for m in arr_m:
    if bs(arr_n, m) == False:
        print(0)
    else:
        print(1)
    

## 시간초과
# import sys

# N = input()
# arr_n = list(map(int, sys.stdin.readline().split()))
# M = input()
# arr_m = list(map(int, sys.stdin.readline().split()))

# for i in range(len(arr_m)):
#     if compare[i] in arr_n:
#         print(1)
#     else:
#         print(0)