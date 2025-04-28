def solution(participant, completion):
    hash_table = {}
    for p in participant:
        hash_table[p] = hash_table.get(p, 0) + 1 # {참여 : 1}
    for c in completion:
        hash_table[c] -= 1 # 복합할당연산 {완주 : 0}
    for p in hash_table:
        if hash_table[p] > 0: # 완주 안 한 사람 = 1
            return p