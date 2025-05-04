import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while scoville:
        if scoville[0] >= K:
            return count
        
        if len(scoville) < 2:
            return -1
        
        # K보다 작은 값 존재 + 원소가 2개 이상
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, (first + second * 2))
        count += 1
        
    # return count