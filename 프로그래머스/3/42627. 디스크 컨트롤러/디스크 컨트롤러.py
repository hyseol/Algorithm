import heapq

def solution(jobs):
    jobs.sort()
    
    waiting = []
    cur_time = 0
    total_time = []
    count_job = 0  # 완료한 작업의 수
    i = 0  # 인덱스

    while count_job < len(jobs):  # 모든 작업을 완료할 때까지 반복
        while i < len(jobs) and jobs[i][0] <= cur_time:  # 요청 시간이 현재 시간보다 같거나 빠른 경우
            heapq.heappush(waiting, (jobs[i][1], jobs[i][0]))  # 소요시간, 요청시간 순으로 대기 큐에 등록
            i += 1
        
        if waiting:  # 처리 가능한 작업이 있는 경우
            work_time, req_time = heapq.heappop(waiting)
            cur_time += work_time
            total_time.append(cur_time - req_time)
            count_job += 1
        else:  # 처리 가능한 작업이 없는 경우
            cur_time = jobs[i][0]  # 다음 작업 요청 시간까지 스킵
    
    return sum(total_time) // len(jobs)
