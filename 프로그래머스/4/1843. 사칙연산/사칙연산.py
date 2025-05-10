def solution(arr):
    n = (len(arr) // 2) + 1  # 숫자의 개수

    # max, min 함수 사용을 위해 inf 값을 초기값으로 사용
    dp_max = [[float('-inf')] * n for _ in range(n)]
    dp_min = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        dp_max[i][i] = dp_min[i][i] = int(arr[2*i])  # 대각선 위치 = 길이 1 구간

    for length in range(2, n+1):  # 구간 길이
        for i in range(n - length + 1):  # i = 시작 인덱스 / n - length + 1 = 시작 인덱스가 될 수 있는 마지막 인덱스
            j = i + length -1  # j = 끝 인덱스
            for k in range(i, j):  # k를 기준으로 왼쪽, 오른쪽 나눔
                # print(i,j)
                op = arr[2 * k + 1]  # 연산자 
                for a in (dp_min[i][k], dp_max[i][k]):
                    for b in (dp_min[k+1][j], dp_max[k+1][j]):
                        # print(a, b, k)
                        if op == '+':
                            val = a + b
                        elif op == '-':
                            val = a - b
                        elif op == '*':
                            val = a * b 
                        dp_max[i][j] = max(dp_max[i][j], val)
                        dp_min[i][j] = min(dp_min[i][j], val)
                        # print(dp_max)
                        # print(dp_min)

    return dp_max[0][n-1]