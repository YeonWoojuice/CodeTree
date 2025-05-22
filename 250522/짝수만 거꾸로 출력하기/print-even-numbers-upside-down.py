N=int(input())
arr=map(int, input().split(" "))

for i in range(N):
    if arr[N-i]%2==0:
        print(arr[N-i],end=" ")
