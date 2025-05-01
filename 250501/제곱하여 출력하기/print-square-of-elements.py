N=int(input())
arr=list(map(int, input().split()))
for i in range(N):
    arr[i]*=arr[i]
print(*arr)