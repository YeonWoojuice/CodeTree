n = int(input())
arr = list(map(int, input().split()))

def maximum(n,arr):
    if (arr[n-1]>arr[n-2]): 
        arr[n-2]=arr[n-1] 
    if n==2:
        print(arr[0])


def f(n,arr):
    if (n==1):
        print(arr[0])
    if (n==2):
        return maximum(n,arr)

    maximum(n,arr) 
    f(n-1,arr)
    
f(n,arr)
    
    