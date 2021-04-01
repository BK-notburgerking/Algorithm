from collections import deque
import sys

def bfs(start, fire):

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    while start:
        for _ in range(len(fire)):
            fire_r, fire_c = fire.popleft()
            for j in range(4):
                fr = fire_r + dr[j]
                fc = fire_c + dc[j]
                if 0 <= fr < h and 0 <= fc < w: #범위체크
                    if building[fr][fc] == '.': #길이면 불이 번짐
                        building[fr][fc] = '*'
                        fire.append((fr, fc))

        for _ in range(len(start)):
            person_r, person_c = start.popleft()
            for i in range(4):
                nr = person_r + dr[i]
                nc = person_c + dc[i]
                if 0 <= nr < h and 0 <= nc < w: #범위안에 있을 때
                    if (nr == 0 or nr == h-1 or nc == 0 or nc == w-1) and building[nr][nc] == '.': #상근이가 끝에있고 그 끝이 갈수있으면
                        return building[person_r][person_c] + 1
                    if building[nr][nc] == '.':
                        building[nr][nc] = building[person_r][person_c] + 1 #상근이 이동
                        start.append((nr, nc))

    return 'IMPOSSIBLE'


for tc in range(int(sys.stdin.readline())):

    w, h = map(int, sys.stdin.readline().split())
    building = []
    start = deque()
    fire = deque()

    for i in range(h):
        tmp = list(sys.stdin.readline())
        building.append(tmp[:w]) #개행문자제거
        for j in range(w):
            if tmp[j] == '*':
                fire.append((i, j))
            if tmp[j] == '@':
                start.append((i, j))
                building[i][j] = 1 #초기값

    if start[0][0] == 0 or start[0][0] == h-1 or start[0][1] == 0 or start[0][1] == w-1:
        print(1)
    else:
        print(bfs(start, fire))