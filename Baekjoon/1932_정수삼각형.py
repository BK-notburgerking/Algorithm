import sys; input = sys.stdin.readline

N = int(input())
tree = []
memo = []
for _ in range(N):
    tree.append(list(map(int, input().split())))

memo.append(tree[0])
for i in range(1, N):
    tmp = []
    for j in range(1, i + 1):
        if tmp:
            tmp[-1] = max(tmp[-1], memo[i - 1][j - 1] + tree[i][j - 1])
        else:
            tmp.append(memo[i - 1][j - 1] + tree[i][j - 1])
        tmp.append(memo[i - 1][j - 1] + tree[i][j])
    memo.append(tmp)

print(max((memo[-1])))