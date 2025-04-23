str, n = input().strip().split(' ')
n = int(n)
if 1 <= len(str) <= 10 and 1 <= n <= 5:
    print(str*n)
