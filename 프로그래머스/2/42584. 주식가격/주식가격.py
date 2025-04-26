def solution(prices):
    from collections import deque
    queue = deque(prices)
    answer = []
    while queue:
        current = queue.popleft()
        time = 0
        for p in queue:
            time += 1
            if p < current:
                break
        answer.append(time)
    return answer