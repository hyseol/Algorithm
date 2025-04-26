def solution(s):
    stack = []
    pair = { "(" : ")"}

    for i in s:
        if i in pair:
            stack.append(i)
        elif len(stack) == 0 or i != pair[stack.pop()]:
            return False
    return len(stack) == 0
