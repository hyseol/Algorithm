import functools

def compare(x, y):
    # x+y와 y+x를 비교해서, 더 큰 조합이 앞으로 오도록 정렬
    if x + y > y + x:
        return -1  # x가 앞에 와야 함
    elif x + y < y + x:
        return 1   # y가 앞에 와야 함
    else:
        return 0   # 순서 상관없음

def solution(numbers):
    # 1. 숫자 리스트를 문자열 리스트로 변환
    str_lst = list(map(str, numbers))
    
    # 2. 문자열들을 '비교 함수(compare)' 기준으로 정렬
    str_lst.sort(key=functools.cmp_to_key(compare))
    
    # 3. 정렬된 문자열들을 하나로 이어붙임
    result = ''.join(str_lst)
    
    # 4. 결과가 '0000...'이면 '0' 반환
    return '0' if result[0] == '0' else result
