N=int(input())

def f(N):
    if N<=2:
        return 1
    else:
        return f(N-1)+f(N-2)

print(f(N))