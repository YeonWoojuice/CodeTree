n, m = map(int, input().split())
A = list(map(int, input().split()))
cnt=0

def addmin(cnt,m,A):

    while (m>0):
        mid=m+1
        if (mid%2==0):
            mid//=2
            cnt+=A[m]

        else:
            mid-=1
            cnt+=A[m]

    print(cnt)

addmin(cnt,m,A)




