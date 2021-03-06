# 2063. 중간값 찾기

# 중간값은 통계 집단의 수치를 크기 순으로 배열 했을 때 전체의 중앙에 위치하는 수치를 뜻한다.
# 입력으로 N 개의 점수가 주어졌을 때, 중간값을 출력하라.

# [제약 사항]
# 1. N은 항상 홀수로 주어진다.
# 2. N은 9이상 199 이하의 정수이다. (9 ≤ N ≤ 199)

# [입력]
# 입력은 첫 줄에 N 이 주어진다.
# 둘째 줄에 N 개의 점수가 주어진다.

# [출력]
# N 개의 점수들 중, 중간값에 해당하는 점수를 정답으로 출력한다.

N = int(input())
lst = list(map(int, input().split()))
tmp = 0

for i in range(N):
    for j in range(N-1):
        tmp = lst[j]
        lst[j] = lst[j+1]
        lst[j+1] = tmp
print(lst[N//2])


#이런방법도 있음
#N = int(input())
#lst = list(map(int, input().split()))
#lst.sort()
#print(lst[N//2])


#어려웠던 점 : sort()를 쓰기 싫어서 어려워졌음.. 왠지 쓰면 치트쓰는거 같아서 싫었음 전부다 돌면서 소팅했는데 더 좋은방법이 분명 있을듯.. 알고리즘 공부가 필요하다.
#             list()를 input()받는 방법을 몰라서 찾아봤음 map()함수와 split()함수에 대해 추가로 알게 됐음
#             split() - 문자열을 분리하기 위해 사용함 괄호안에 '내용' 을 넣어서 해당 내용을 기준으로 분리할 수 있음
#             map() - map(변환 함수, 순회 가능 데이터) - 여러개의 데이터를 한 번에 다른 형태로 변환함