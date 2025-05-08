def solution(citations):
    citations.sort(reverse = True)
    for i, c in enumerate(citations):
        if i+1 >= c:
            return i  
        
    return len(citations)  # 모든 원소가 조건을 만족할 경우 전체 논문 개수 = h-index
        