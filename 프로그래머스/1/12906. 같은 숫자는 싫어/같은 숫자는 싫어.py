def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i == 0 or arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer


# stack
def solution(arr):
    stack = []
    for num in arr:
        if not stack or stack[-1] != num:
            stack.append(num)
    return stack
