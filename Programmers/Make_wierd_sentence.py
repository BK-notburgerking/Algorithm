# https://programmers.co.kr/learn/courses/30/lessons/12930
# 이상한 문자 만들기

def solution(s):
    lst = s.split(' ')
    strange = ''
    for word in lst:
        for i in range(len(word)):
            if word[i].isalpha() == True:
                if i % 2 == 0:
                    strange += word[i].upper()
                else:
                    strange += word[i].lower()
            else:
                strange += word[i]
        strange += ' '
    return strange[:-1]

# 9번줄의 .isalpha()에서 ()를 빼먹고 왜 안돌아 가는지 2일이나 쳐다봤다.. 다음부턴 꼭 주의하고 코드는 처음 쓸때 주의해서 쓰자 제발!!!!