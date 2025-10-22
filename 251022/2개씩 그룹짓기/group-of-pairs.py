import sys
input = sys.stdin.readline
n=int(input())
arr=sorted(map(int, input().split()))
res=[]
for i in range(0,n):
    res.append(arr[i]+arr[2*n-1-i])
print(max(res))
