def solution(stones, k):
    start = 0
    end = max(stones)
    
    while start <= end:
        mid = (start + end) // 2
        skip = 0
        for s in stones:
            if s - mid < 0:
                skip += 1
                if skip >= k:
                    break
            else:
                skip = 0

        if skip >= k:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1

    return answer