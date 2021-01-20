# https://programmers.co.kr/learn/courses/30/lessons/12930

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

# 8번라인에 .isalpha()에서 ()를 빼먹고 왜안되지 하면서 2일을 봤음 제발 다음부터 이런실수 절대 하지 말자.. 코드를 처음쓸때 꼼꼼히 쓰자 제발