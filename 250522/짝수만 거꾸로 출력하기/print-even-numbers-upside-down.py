N = int(input())
arr = list(map(int, input().split()))

for i in range(0,N):
    if (arr[N-i-1]%2==0):
        print(arr[N-i-1],end=" ")
