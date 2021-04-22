def solution(tickets):
    adj = {} #인접리스트
    for dep, arr in tickets:
        if adj.get(dep) == None:
            adj[dep] = [arr]
        else:
            adj[dep] += [arr]

    for dep in adj.keys():
        adj[dep].sort(reverse=True) #가장 위부터 꺼내서 쓸거라 오름차순
        #가장 위에 사전순 제일 빠른게 올라옴

    s = ["ICN"] # 인천에서 시작
    ans = []
    while s:
        depart = s.pop() #스택에서 꺼냄 -> 출발지
        # 만약 출발지가 실제로 출발가능하고 (인접리스트에 키로 존재)
        # 아직 사용안한 티켓이 있으면 (밸류의 길이가 양수)
        if depart in adj and len(adj[depart]) > 0:
            s.append(depart) #다시 스택에 넣어주고
            s.append(adj[depart].pop()) #가장 위에있는 티켓을 스택에 넣어줌
        else: # 해당 출발지에서 출발하는 티켓이 없는 경우
            # 바로 정답에 넣어줌
            # 왜냐하면 더이상 갈곳이 없기때문에 굳이 스택에 넣어서 탐색할 필요가 없음
            ans.append(depart)

    return ans[::-1]