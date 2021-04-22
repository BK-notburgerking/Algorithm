# 모의고사
# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    pattern_1 = [1, 2, 3, 4, 5]
    pattern_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 패턴3개 정의
    cnt = [0, 0, 0] # 맞은갯수 담을 리스트
    answer = [] # 정답 리턴할 리스트
    
    for i in range(len(answers)): #answers 갯수만큼 반복
        if answers[i] == pattern_1[i % len(pattern_1)]: #pattern_1[i % len(pattern_1)] 을 통해서 리스트를 반복되는 사이클로 만들수있음
            cnt[0] += 1
        if answers[i] == pattern_2[i % len(pattern_2)]:
            cnt[1] += 1
        if answers[i] == pattern_3[i % len(pattern_3)]:
            cnt[2] += 1
    
    for idx, score in enumerate(cnt): #enumerate활용해 인덱스와 함께 가져옴 이경우 인덱스+1 이 리턴해야할 학생이 됨
        if score == max(cnt): #맞은점수가 max랑 같으면
            answer.append(idx + 1) #해당 인덱스+1 (학생) 을 정답 리스트에 저장
    return answer