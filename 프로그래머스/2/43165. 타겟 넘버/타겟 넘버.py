def solution(numbers, target):
    count = 0

    def dfs(index, current_sum):
        nonlocal count
        if index == len(numbers):
            if current_sum == target:
                count += 1
            return  # 재귀 종료 
        
        # 재귀 호출 - 다음 숫자 더하거나 빼는 두 가지 경우 탐색
        dfs(index + 1, current_sum + numbers[index])
        dfs(index + 1, current_sum - numbers[index])

    # 함수 실행
    dfs(0, 0)  # 초기 인덱스 = 0, 초기 누적합 = 0
    return count
