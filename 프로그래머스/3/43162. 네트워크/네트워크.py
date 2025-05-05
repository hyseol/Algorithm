def solution(n, computers):
    
    def dfs(com):
        visited[com] = True
        for other_com in range(n):
            if computers[com][other_com] == 1 and not visited[other_com]:
            # 현재 노드와 연결 + 방문 X -> dfs 실행 = 연결된 다른 컴퓨터 탐색
                dfs(other_com)
    
    visited = [False] * n
    count = 0

    for i in range(n):
        if not visited[i]:
        # 방문하지 않은 노드 탐색
            dfs(i)
            count += 1
    
    return count