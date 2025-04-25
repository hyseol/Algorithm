def solution(bridge_length, weight, truck_weights):
    from collections import deque
    on_bridge = deque([0] * bridge_length)
    wating_trucks = deque(truck_weights)

    time = 0
    current_weight = 0

    while on_bridge:
        time += 1

        left = on_bridge.popleft() # 다리에서 트럭 나가기
        current_weight -= left

        if wating_trucks:
            if current_weight + wating_trucks[0] <= weight: # 트럭 올라가기 
                current_truck = wating_trucks.popleft()
                on_bridge.append(current_truck)
                current_weight += current_truck
            else:
                on_bridge.append(0) # 못 올라가고 시간만 +1

    return time