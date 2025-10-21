import sys
n = int(sys.stdin.readline())

def f_iter(n):
    if n == 1: return 2
    if n == 2: return 4
    a, b = 2, 4          # f(1), f(2)
    for _ in range(3, n + 1):
        a, b = b, (a * b) % 100
    return b

print(f_iter(n))
