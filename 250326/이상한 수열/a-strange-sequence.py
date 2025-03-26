N = int(input())

def f(N):
    if N==1:
        return 1
    if N==2:
        return 2
    return f(N-1)+f(N//3)

print(f(N))
    