N = int(input())

def f(N):
    if (N%2==0):
        if (N==2):
            return N 
        return N+f(N-2)

    else: 
        if (N==1):
            return N
        return N+f(N-2)

print(f(N))
