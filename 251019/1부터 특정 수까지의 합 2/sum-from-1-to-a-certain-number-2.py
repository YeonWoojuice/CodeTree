N=int(input())

def f(N):
    if (N==0):
        return N
    return f(N-1)+N

print(f(N))