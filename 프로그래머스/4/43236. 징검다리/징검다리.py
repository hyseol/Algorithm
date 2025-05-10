def solution(distance, rocks, n):
    answer = 0
    sorted_rocks = sorted(rocks)
    sorted_rocks.append(distance)

    start = 0
    end = distance
    while (start <= end):
        mid = (start + end) // 2
        removed = 0
        prev = 0
        for i in range(len(sorted_rocks)):
            if (sorted_rocks[i] - prev < mid):
                removed += 1
            else:
                prev = sorted_rocks[i]
        if removed > n:
            end = mid - 1
        else:
            start = mid + 1
            answer = mid
    return answer