def solution(progresses, speeds):
    from collections import deque
    queue = deque(progresses)
    answer = []
    
    while queue:
        for i in range(len(queue)):
            queue[i] += speeds[i]

        release = 0
        while queue and queue[0] >= 100:
            queue.popleft()
            speeds.pop(0)
            release += 1

        if release > 0:
            answer.append(release)
    
    return answer
