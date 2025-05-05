from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    direcions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 상하좌우 이동
    queue = deque([(0, 0, 1)])  # 시작 위치 (0,0) / 이동 거리 = 1

    while queue:
        x, y, d = queue.popleft()

        if x == n-1 and y == m-1:  # 목표지점에 도달하면 이동 거리 반환
            return d
        
        for dx, dy in direcions:
            nx, ny = x + dx, y + dy  # 이동할 위치의 좌표로 갱신
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
            # 맵 내부에 있는지 확인 + 이동한 위치가 길(1)인지 확인
                maps[nx][ny] = 0  # 방문 지점은 벽(0)으로 바꿔서 다시 돌아가지 않도록 처리
                queue.append((nx, ny, d+1))  # 이동 확정 후 현재 위치 갱신
    
    return -1  # 목표 지점에 도달할 수 없는 경우 = while 문이 끝까지 반복되지 않는 경우