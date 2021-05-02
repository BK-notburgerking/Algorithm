import sys; input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
rank_arr = sorted(list(set(arr)))
ans_dic = {}

for i in range(len(rank_arr)):
    ans_dic[rank_arr[i]] = i

for i in range(N):
    arr[i] = ans_dic[arr[i]]

print(*arr)