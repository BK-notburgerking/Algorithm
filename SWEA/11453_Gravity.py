import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    box = list(map(int, input().split()))
    fall = []
    maximum = 0

    for i in range(len(box)):
        drop = len(box) - i
        for j in range(i,len(box)):
            if box[i] <= box[j]:
                drop -= 1
        fall.append(drop)

    for falling in fall:
        if maximum < falling:
            maximum = falling

    print(f'#{tc} ' + str(maximum))
