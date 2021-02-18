for tc in range(1, 11):

    dump = int(input())
    boxes = list(map(int, input().split()))


    for _ in range(dump):
        max = boxes[0]
        min = boxes[0]
        maxidx = 0
        minidx = 0
        for j in range(1, len(boxes)):
            if boxes[j] > max:
                max = boxes[j]
                maxidx = j
            if boxes[j] < min:
                min = boxes[j]
                minidx = j
        boxes[maxidx] -= 1
        boxes[minidx] += 1

    maxi = boxes[0]
    mini = boxes[0]
    for box in boxes:
        if box > maxi:
            maxi = box
        if box < mini:
            mini = box
    answer = maxi - mini

    print(f'#{tc} {answer}')