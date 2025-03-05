n, m = map(int, input().split())
A = list(map(int, input().split()))
cnt=0

def addmin(cnt,m,A):

    while (m>0):
        if (m%2==0):
            m=//2
            cnt+=A[m]

        else:
            m-=1
            cnt+=A[m]

    print(cnt)

addmin(cnt,m,A)



