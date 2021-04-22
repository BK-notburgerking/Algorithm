#예상 대진표 2017 팁스타운
#https://programmers.co.kr/learn/courses/30/lessons/12985

def solution(n,a,b):
    cnt = 0 # 경기 횟수
    while True:
        a = (a + 1) // 2 # 3일경우 2가 4일경우도 2가 되므로 +1해서 몫만 가져옴
        b = (b + 1) // 2
        cnt += 1 
        if a == b: #만나게 되면 스탑
            break
    return cnt