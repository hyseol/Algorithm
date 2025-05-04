import heapq

def solution(operations):
    queue = []
    heapq.heapify(queue)
    
    for oper in operations:
        if oper.startswith("I"):
            heapq.heappush(queue, int(oper[2:]))
                           
        elif queue and (oper == "D 1"):   
            queue.remove(max(queue))
            heapq.heapify(queue)
                           
        elif queue and (oper == "D -1"):
            heapq.heappop(queue)
    
    if len(queue) == 0:
       return [0,0]
    else:
       return [max(queue), min(queue)]