# 최상위 부모 = 루트 찾기
def find(parent, x):
    if parent[x] != x:  # 자신과 같지 않다 = 루트를 찾지 못함
        parent[x] = find(parent, parent[x])  # 경로 압축 = 재귀
    return parent[x]

# a,b 2개의 노드를 같은 집합으로 연결
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:  # 루트가 더 작은 쪽을 기준으로 집합을 합침
        parent[b] = a
    else:
        parent[a] = b

def solution(n, costs):  # n : 섬 개수 / costs : 연결 가능한 간선 목록
    costs.sort(key=lambda x: x[2])  # 비용이 낮은 순서로 정렬
    parent = [i for i in range(n)]  # 각 섬의 부모를 자기 자신으로 초기화
    
    total_cost = 0
    for a, b, cost in costs:
        if find(parent, a) != find(parent, b):  # 서로 다른 집합 = 연결되지 않음
            union(parent, a, b)  # 같은 집합으로 연결 
            total_cost += cost  # 비용 추가
    
    return total_cost
