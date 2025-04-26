def solution(priorities, location):
    from collections import deque
    
    queue = deque([(i, p) for i, p in enumerate(priorities)])
    order = 0

    while queue:
        idx, priority = queue.popleft()
        if any(priority < p for _, p in queue):
            queue.append((idx, priority))
        else:
            order += 1
            if idx == location:
                return order