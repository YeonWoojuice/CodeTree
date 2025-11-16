import sys
n=int(sys.stdin.readline())
arr=[[0 for _ in range(n)]for _ in range(n)]
add=1
for i in range(n-1,-1,-1):
    if ((n-1-i)%2==0):
        for j in range(n-1,-1,-1):
            arr[j][i]=add
            add+=1
    else:
        for j in range(0,n):
            arr[j][i]=add
            add+=1

print("\n".join(" ".join(map(str, row)) for row in arr))

