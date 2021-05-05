def solution(rows, columns, queries):
    arr = [([0] * columns) for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = (j + 1) + columns * i

    def move(sr, sc, er, ec):
        xr, xc = sr, sc  # 이전좌표
        ex_num = arr[xr][xc]  # 이전 값
        min_num = ex_num  # 최소 값
        for _ in range(ec - sc):  # 우
            nr, nc = xr, xc + 1  # 이동할 좌표
            tmp = arr[nr][nc]  # 다음 움직일 숫자
            if tmp < min_num:
                min_num = tmp
            arr[nr][nc] = ex_num  # 이동할 좌표에 이전 값 할당
            xr, xc = nr, nc  # 이전좌표 변경
            ex_num = tmp  # 이전좌표의 값 변경

        for _ in range(er - sr):  # 하
            nr, nc = xr + 1, xc
            tmp = arr[nr][nc]
            if tmp < min_num:
                min_num = tmp
            arr[nr][nc] = ex_num
            xr, xc = nr, nc
            ex_num = tmp

        for _ in range(ec - sc):  # 좌
            nr, nc = xr, xc - 1
            tmp = arr[nr][nc]
            if tmp < min_num:
                min_num = tmp
            arr[nr][nc] = ex_num
            xr, xc = nr, nc
            ex_num = tmp

        for _ in range(er - sr):  # 상
            nr, nc = xr - 1, xc
            tmp = arr[nr][nc]
            if tmp < min_num:
                min_num = tmp
            arr[nr][nc] = ex_num
            xr, xc = nr, nc
            ex_num = tmp

        return min_num

    ans = []
    for query in queries:
        sr, sc, er, ec = query
        ans.append(move(sr - 1, sc - 1, er - 1, ec - 1))

    return ans