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


# pairs 활용 버전
def solution(s):
    stack = []
    pair = { "(" : ")"}

    for i in s:
        if i in pair:
            stack.append(i)
        elif len(stack) == 0 or i != pair[stack.pop()]:
            return False
    return len(stack) == 0



