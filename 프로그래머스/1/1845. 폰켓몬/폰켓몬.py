from collections import Counter

def solution(nums):
    species = len(Counter(nums).keys())
    count = len(nums)//2
    return min(species, count)