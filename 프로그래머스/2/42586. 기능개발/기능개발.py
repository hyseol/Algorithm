def solution(progresses, speeds):
    from collections import deque
    queue = deque(progresses)
    answer = []
    
    while queue: # 하루 지날때마다 작업 진도 업데이트
        for i in range(len(queue)):
            queue[i] += speeds[i]

        release = 0
        while queue and queue[0] >= 100: 
            queue.popleft()
            speeds.pop(0)
            release += 1 # 100 이상일 경우 배포 +1

        if release > 0:
            answer.append(release) # answer에 release 값 저장
    
    return answer



# zip 활용 / 필요한 작업 일수로 계산 버전

def solution(progresses, speeds):
    from collections import deque
    import math

    days = deque()
    answer = [] 
    for p, s in zip(progresses, speeds): # 필요한 작업 일수 계산
        days.append(math.ceil((100-p)/s)) 

    while days:
        current = days.popleft() # 첫번째 작업 배포
        release = 1

        while days and days[0] <= current: # 첫번째 작업보다 작업일수가 작거나 같으면 배포
            days.popleft()
            release += 1
        
        answer.append(release)
    
    return answer

