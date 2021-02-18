#K = 한번 충전으로 최대한 이동할 수 있는 정류장 수
#N = 종점
#M = 충전기가 설치된 정류장의 수

n = int(input())
for tc in range(1, n + 1):

    K, N, M = map(int, input().split())
    line = list(map(int, input().split()))
    busStop = [0] * (N + 1) #정류장 리스트

    for gas in line: #정류장 리스트에서 충전소가 있는 정류장은 1
        busStop[gas] = 1
    
    i = 0
    answer = 0

    while i < N:
        for j in range(K, -1, -1):
            if j == 0: #탐색하다가 제자리로 돌아왔어,
                i += N #while 깰 조건
                answer = 0 #주유횟수초기화
            if i + j >= N: #정류장 넘어가면
                i += j #while 깰 조건
                break
            if busStop[i + j] == 1:
                i += j #이동거리만큼 확인했는데 주유소 있으면 해당 지점을 시작점으로
                answer += 1 #주유횟수
                break #뒤로 더가면 안되니까 스탑

    print(f'#{tc} {answer}')