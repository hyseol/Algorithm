def solution(m, n, puddles):
    dp = [0] * m
    dp[0] = 1  # 시작점

    puddles_set = set((x-1, y-1) for x, y in puddles)
    
    for y in range(n):
        for x in range(m):
            if (x, y) in puddles_set:
                dp[x] = 0
                continue
            if x > 0:
                dp[x] = (dp[x] + dp[x-1]) % 1000000007
        if y != 0:
            dp[0] = dp[0]
    
    return dp[m-1]