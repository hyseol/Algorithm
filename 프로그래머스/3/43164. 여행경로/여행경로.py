def solution(tickets):
    route = {}
    for start, end in tickets:
        if start not in route:
            route[start] = [end]
        else:
            route[start].append(end)
    
    for key in route:
        route[key].sort()
        
    total_len = len(tickets) + 1
    answer = []
    
    def dfs(path):
        if len(path) == total_len:  # 모든 공항을 거치는 경로를 찾은 경우
            answer.extend(path)
            return True
    
        current = path[-1]
        if current not in route:
            return False  # 재귀 종료 조건(마지막 공항까지 탐색)

        for i in range(len(route[current])):
            next = route[current][i]
            route[current].pop(i)
            path.append(next)

            if dfs(path):
                return True  # 재귀 종료 조건(정답 경로 찾은 경우)

            # 백트래킹
            path.pop()
            route[current].insert(i, next)
        
        return False
        
    dfs(["ICN"])
    return answer