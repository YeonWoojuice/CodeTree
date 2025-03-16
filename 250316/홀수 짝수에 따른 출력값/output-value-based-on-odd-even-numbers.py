N = int(input())

def f(N):
    if (N==1):
        return res
    elif (N==2):
        return res
    
    if (N%2==1): # 홀수
        res+=f(N-2)
    else: # 짝수
        res+=f(N-2)

print(f(N))
