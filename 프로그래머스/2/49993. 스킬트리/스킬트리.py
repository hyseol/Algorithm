def solution(skill, skill_trees):
    count = 0
    for s in skill_trees:
        filtered = ''.join([c for c in s if c in skill])
        if skill.startswith(filtered):
            count += 1
    return count