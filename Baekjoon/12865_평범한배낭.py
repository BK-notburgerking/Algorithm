import sys; input = sys.stdin.readline

def dp(bag):
    for item in range(1, N + 1): # 물건하나씩 꺼내서 가방에 넣어봄
        weight, value = bag.pop()
        for bag_size in range(1, K + 1): # 배낭의 크기를 최대까지 키워가며 담으며 가치를 적음
            # 물건을 담을만큼 가방이 커지면
            if bag_size >= weight:
                                         # 물건을 안담았을 때 가치와, 담았을 때의 가치 중 큰것을 취함
                memo[item][bag_size] = max(memo[item-1][bag_size], memo[item-1][bag_size - weight] + value)
            else: # 물건의 무게가 배낭의 크기보다 작을 경우
                memo[item][bag_size] = memo[item - 1][bag_size] # 물건 못담음 즉, 가치추가 X

N, K = map(int, input().split())
# 선택0, 무게0의 경우를 만들기 위해 각각 +1씩
memo = [([0] * (K + 1)) for _ in range(N + 1)]
bag = []
for _ in range(N):
    w, v = map(int, input().split())
    bag.append([w, v])
dp(bag)

print(memo[N][K])