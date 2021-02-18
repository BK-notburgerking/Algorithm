n = int(input())
for tc in range(1, n+1):

    lst = []
    c = int(input())
    numbers = input()
    for i in range(len(numbers)):
        lst.append(int(numbers[i]))

    tmp = [0] * 10 #갯수담을 리스트 초기화
    max = 0
    num = 0

    for j in range(c):
        tmp[lst[j]] += 1 #갯수담을 리스트에 카드를 인덱스로 해서 갯수 카운트

    for k in range(10): #
        if tmp[k] >= max: # 가장 큰 갯수와 카드를 탐색 '='를 사용해서 가장 큰숫자를 저장함 
            max = tmp[k]
            num = k
    
    print(f'#{tc} {num} {max}')