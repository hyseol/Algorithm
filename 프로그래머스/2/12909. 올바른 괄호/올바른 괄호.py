def solution(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")": 
            if not stack or stack[-1] != "(":
                return False
            stack.pop()
    return not stack