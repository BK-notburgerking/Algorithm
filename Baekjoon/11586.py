mirror = [] #거울에 비치는 모양을 담을 리스트 초기화

size = int(input()) # 사이즈 입력

for i in range(size):
    mirror += [list(map(str, input()))] #입력을 한줄씩 리스트로 받고, 초기화한 리스트에 2차원 리스트로 담음 

feelings = int(input()) # 1:그대로 / 2:좌우반전 / 3:상하반전

if feelings == 1: #그대로
    for princess in mirror: #리스트 앞에서부터 하나씩 꺼내서
        print(''.join(princess)) # ''.join()을 통해 한줄 씩 str으로 바꾸면서 출력

elif feelings == 2:
    for princess in mirror: 
        princess.reverse() #꺼내서 뒤집음
        print(''.join(princess))

else:
    for princess in mirror[::-1]: #바깥 리스트를 뒤집어서 뒤부터 꺼내오도록 만듬
        print(''.join(princess))
