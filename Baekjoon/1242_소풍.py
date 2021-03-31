# #사람, 움직이는수, 동호
# N, K, M = map(int, input().split())
# kill = K % N #만약 K가 N보다 클경우 다시 1부터 반복하게 만들어야 하므로 나머지 계산
# if kill == 0: #만약 K가 N의 배수일 경우 마지막값을 죽이는데 값은 0이 나오므로 보정필요함
#     kill = N
# #지워진 숫자 다음을 1로 했을 때 동호의 위치를 계산, 반복
# for i in range(1, N + 1):
#     if M == kill or N == 1: #동호의자리가 지워질 자리와 같거나, 동호만 남았을 때
#         print(i)
#         break
#     elif M > kill:
#         M -= kill #지워진 사람 다음을 1로 했을 때 동호의 위치
#         N -= 1 #사람이 한명 줄어듦
#     elif M < kill:
#         M = N + M - kill #이경우 M - K는 음수값, 뒤로 몇번째에 있다고 계산하면 됨
#         while M <= 0:
#             M = M + N
#         N -= 1
#         아니왜안돼 ㅡㅡ

N, K, M = map(int, input().split())
M -= 1 #동호의 인덱스
start = 0
for i in range(1, N + 1):
    removed = (start + K - 1) % N
    if removed == M:
        print(i)
        break
    if removed < M:
        M -= 1
    if removed > M:
        pass
    start = removed
    N -= 1
