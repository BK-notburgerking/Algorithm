import sys; input = sys.stdin.readline

def order(p):
    pre_in_post_order[0] += p
    if adj[p][0] != '.':
        order(adj[p][0])
    pre_in_post_order[1] += p
    if adj[p][1] != '.':
        order(adj[p][1])
    pre_in_post_order[2] += p

N = int(input())
adj = {}
pre_in_post_order = ['', '', '']
for _ in range(N):
    p, lc, rc = input().split()
    adj[p] = [lc, rc]

order('A')

print('\n'.join(pre_in_post_order))