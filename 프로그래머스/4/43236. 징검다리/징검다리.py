def is_possible(min_dist, distance, rocks, n):
    removed = 0  # 제거된 돌의 수
    prev = 0  # start 지점부터 시작

    for r in rocks:
        if r - prev < min_dist:  # r과 직전 지점 사이의 거리가 최소 길이보다 짧으면 r 제거
            removed += 1
        else:  # 그렇지 않으면 직전 지점 갱신
            prev = r
    
    if distance - prev < min_dist:  # 도착지와 마지막 돌 사이의 거리 확인
        removed += 1

    return removed <= n  # 제거된 돌이 n개인지 확인
      

def solution(distance, rocks, n):
    rocks.sort()
    start = 1
    end = distance

    while start <= end:
        mid = (start + end) // 2  # 확인할 최소 길이 
        if is_possible(mid, distance, rocks, n):
            answer = mid
            start = mid + 1  # 더 큰 거리도 가능한지 확인
        else:
            end = mid - 1  # 더 작은 거리 확인

    return answer