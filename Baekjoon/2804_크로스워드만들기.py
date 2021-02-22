A, B = input().split()
N, M = len(A), len(B) #열, 행

puzzle = [['.'] * N for _ in range(M)]

for i in range(N):
    flag = False
    for j in range(M):
        if A[i] == B[j]:
            row = j
            col = i
            flag = True
            break
    if flag == True:
        break

for i in range(N):
    puzzle[row][i] = A[i]

for i in range(M):
    puzzle[i][col] = B[i]

for i in range(M):
    print(''.join(puzzle[i]))