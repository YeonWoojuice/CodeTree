n = int(input())
arr = list(map(int, input().split()))

def divide(n,arr):
    for i in range(0,n):
        if (arr[i]%2==0):
            res=arr[i]//2
            print(res,end=" ")
        else:
            res=arr[i]
            print(res,end=" ")

divide(n,arr)
# Write your code here!