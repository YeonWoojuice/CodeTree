N=int(input())

def f(N):
    if N==0:
        return
    print(N,end=" ")
    f(N-1)

def g(N):
    if N==0:
        return
    g(N-1)
    print(N,end=" ")

g(N)
print()
f(N)