import math

def solution(numer1, denom1, numer2, denom2):
    n, d = (numer1 * denom2) + (numer2 * denom1), denom1 * denom2
    
    gcd = math.gcd(n, d)  # 최대공약수 구하기
    
    return [n // gcd, d // gcd]