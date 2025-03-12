N = int(input())
cnt=0

def func(N,cnt):
    
    if N==1:
        print(cnt)
        
    elif N%2==0:
        cnt+=1
        func(N//2,cnt)
        
    else:
        cnt+=1
        func(N//3,cnt)

func(N,cnt)