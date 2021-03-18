from collections import deque

def rotate(gear, rot):
    if rot == 1:
        mag[gear].appendleft(mag[gear].pop())
    if rot == -1:
        mag[gear].append(mag[gear].popleft())

for tc in range(1, int(input()) + 1):
    K = int(input())
    mag = [[-1] * 8]
    for _ in range(4):
        mag.append(deque(map(int, input().split())))
    mag.append([-1] * 8)

    for _ in range(K):
        gear, rot = map(int, input().split())
        rotate_list = [gear]
        left = mag[gear][6]
        right = mag[gear][2]
        i = 1
        j = 1
        while left != mag[gear - i][2] and mag[gear - i][2] != -1:
            left = mag[gear - i][6]
            rotate_list.append(gear - i)
            i += 1
        while right != mag[gear + j][6] and mag[gear + j][6] != -1:
            right = mag[gear + j][2]
            rotate_list.append(gear + j)
            j += 1

        for rotating_gear in rotate_list:
            if abs(gear - rotating_gear) == 0:
                rotate(rotating_gear, rot)
            if abs(gear - rotating_gear) == 1:
                a = rot * -1
                rotate(rotating_gear, a)
            if abs(gear - rotating_gear) == 2:
                rotate(rotating_gear, rot)
            if abs(gear - rotating_gear) == 3:
                a = rot * -1
                rotate(rotating_gear, a)

    score = 0
    for i in range(1, 5):
        score += (mag[i][0] * (2 ** (i - 1)))

    print('#{} {}'.format(tc, score))