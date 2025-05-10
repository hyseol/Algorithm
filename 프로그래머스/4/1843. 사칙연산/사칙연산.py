def solution(arr):
    arrs = ''.join(arr).split('-')  # -를 기준으로 나눔
    val0 = sum(list(map(int, arrs[0].split('+'))))  # 맨 앞의 값 = 무조건 포함
    if len(arrs) == 1:  # -가 없는 경우
        return val0
    
    min_val = 0
    max_val = 0
    for arr in arrs[:0:-1]:  # 뒤에서부터 앞으로 순회
        x = list(map(int, arr.split('+')))
        x_min = -(sum(x))  # -로 묶어서 최소값 계산
        x_max = sum(x[1:]) - x[0]  # x[0]만 빼고 나머지는 다 더함 = 최댓값
        min_val, max_val = min(x_min + min_val, x_min - max_val), max(x_max + max_val, x_min - min_val)

    return val0 + max_val