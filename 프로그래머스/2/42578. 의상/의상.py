def solution(clothes):
    hash_table = {}
    for name, category in clothes:
        hash_table[category] = hash_table.get(category, 1) + 1

    answer = 1
    for count in hash_table.values():
        answer *= count

    return answer - 1