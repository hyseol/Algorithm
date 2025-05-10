def solution(m, n, puddles):
    pd = [[0] * m for _ in range(n)]
    pd[0][0] = 1  # 시작점
    
    for i, j in puddles:
        pd[j-1][i-1] = -1  # 물웅덩이
    
    for y in range(n):
        for x in range(m):
            if pd[y][x] == -1:  # 물웅덩이 제외
                continue
            if y > 0 and pd[y-1][x] > 0 :  # 아래로 이동하는 경로
                pd[y][x] = (pd[y][x] + pd[y-1][x]) % 1000000007
            if x > 0 and pd[y][x-1] > 0:  # 오른쪽으로 이동하는 경로
                pd[y][x] = (pd[y][x] + pd[y][x-1]) % 1000000007
    
    return pd[n-1][m-1] if pd[n-1][m-1] != -1 else 0
