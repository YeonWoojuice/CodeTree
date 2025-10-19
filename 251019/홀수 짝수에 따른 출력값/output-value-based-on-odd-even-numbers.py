N=int(input())

def f(N):
    if N<=2:
        return N
    else:
        if N%2==0:
            return f(N-2)+N
        elif N%2==1:
            return f(N-2)+N

print(f(N))
    