def solution(tickets):
    adj = {}
    for dep, arr in tickets:
        if adj.get(dep) == None:
            adj[dep] = [arr]
        else:
            adj[dep] += [arr]

    for dep in adj.keys():
        adj[dep].sort(reverse=True)

    s = ["ICN"]
    ans = []
    while s:
        depart = s.pop()
        if depart in adj and len(adj[depart]) > 0:
            s.append(depart)
            s.append(adj[depart].pop())
        else:
            ans.append(depart)

    return ans[::-1]