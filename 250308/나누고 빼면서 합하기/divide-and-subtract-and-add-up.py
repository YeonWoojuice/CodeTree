n, m = map(int, input().split())
A = list(map(int, input().split()))
cnt=0

def addmin(cnt,m,A):
    while (m>0):
        if (m%2==0):
            cnt+=A[m-1]
            m//=2
            
        else:
            cnt+=A[m-1]
            m-=1

    print(cnt)

addmin(cnt,m,A)
