import sys
sys.setrecursionlimit(3000)
cache = [None] * 2050

def F(n):
    global cache
    if cache[n] is not None:
        return cache[n]
    else:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n > 2:
            cache[n] = n*(n-1) + F(n-1)+F(n-2)
            return cache[n]
print(F(2020))