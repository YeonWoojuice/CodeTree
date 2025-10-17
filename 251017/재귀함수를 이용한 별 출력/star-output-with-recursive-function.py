N=int(input())

def printstar(N):
    if N==0:
        return N
    printstar(N-1)
    print("*"*N)

printstar(N)