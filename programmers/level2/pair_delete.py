# 짝지어 제거하기 2017 팁스타운
# https://programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    word = list(map(str, s))
    lst = [0]
    
    for i in range(len(word)): #word의 리스트 원소만큼 반복하는데
        backword = word.pop() #뒤에서 부터 하나씩 꺼낸 뒤 변수에 저장한다.
        if lst[-1] == backword: #pop한 원소와 가장 최근에 append된 원소와 같으면
            lst.pop() #리스트에서 해당 원소를 꺼낸다.
        else:
            lst.append(backword) #다른원소면 리스트에 넣는다.
    if len(lst) == 1: #초기값이되면
        return 1 #다 짝지어 사라진 것
    return 0



solution('baabaa')
solution('cdcd')