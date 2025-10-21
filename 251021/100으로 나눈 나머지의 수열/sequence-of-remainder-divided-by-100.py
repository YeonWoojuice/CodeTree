import sys
from functools import lru_cache

n = int(sys.stdin.readline())

@lru_cache(None)
def f(n):
    if n == 1: return 2
    if n == 2: return 4
    return (f(n-1) * f(n-2)) % 100

print(f(n))
