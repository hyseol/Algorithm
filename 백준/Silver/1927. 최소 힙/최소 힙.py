import sys
import heapq

input = sys.stdin.readline
N = int(input())
heap = []

for _ in range(N):
    x = int(input())
    if x > 0:
        heapq.heappush(heap, x)  # O(log n)
    elif x == 0:
        if heap:
            print(heapq.heappop(heap))  # O(log n)
        else:
            print(0)

