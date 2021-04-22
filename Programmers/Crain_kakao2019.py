# 2019 카카오개발자 겨울 인턴십
# https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    stack = []
    result = 0
    for move in moves:
        for doll in board: 
            if doll[move-1] != 0:
                stack.append(doll[move-1])
                doll[move-1] = 0
                break
        if len(stack) >= 2:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                result += 2
    return result