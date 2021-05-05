def solution(lottos, win_nums):
    winning = {}
    for win in win_nums:
        winning[win] = 1

    tmp = 0
    for lotto in lottos:
        if lotto == 0:
            tmp += 1
        else:
            if winning.get(lotto) != None:
                winning[lotto] += 1

    min_match = 0
    for win_num, match in winning.items():
        if match == 2:
            min_match += 1
    max_match = min_match + tmp

    ans = [6, 6]
    for i in range(2, 7):
        if min_match == i:
            ans[1] = 7 - i
        if max_match == i:
            ans[0] = 7 - i

    return ans