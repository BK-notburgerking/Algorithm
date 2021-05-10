import sys; input = sys.stdin.readline

N, M = map(int, input().split())
T = set(input().split()[1:])

parties = []
ans = [1] * M # 다 거짓말을 할 수 있음

for _ in range(M):
    parties.append(set(input().split()[1:]))

for _ in range(M):
    for idx, party in enumerate(parties):
        if ans[idx]: # 거짓말 할 수 있는 파티일때만 검증
            if T & party: # 교집합 있으면
                T.update(party) # 진실을 말해야 하는 집합에 추가하고
                ans[idx] = 0 # 해당 번호의 파티를 거짓말 할 수 없음 처리

print(sum(ans))