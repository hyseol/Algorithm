def possible(mid, distance, rocks, n):
    removed = 0
    prev = 0
    for r in rocks:
        if (r - prev) < mid:
            removed += 1
        else:
            prev = r

    if (distance - prev) < mid:
        removed += 1

    return removed <= n
    
def solution(distance, rocks, n):        
    rocks.sort()
    start = 0
    end = distance
    
    while start <= end:
        mid = (start + end) // 2
        if possible(mid, distance, rocks, n):
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
    
    return answer