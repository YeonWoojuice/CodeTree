a, b, c = map(int, input().split())

def g(n):
    if n < 10:
        return n

    return g(n // 10) + (n % 10)

def f(a,b,c):
    res=a*b*c
    return g(res)

print(f(a,b,c))
     
