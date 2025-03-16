N = int(input())

def f(N):
    if (N==1):
        return N
    elif (N==2):
        return N
    
    if (N%2==1): # 홀수
        f(N)+f(N-2)
    else: # 짝수
        f(N)+f(N-2)