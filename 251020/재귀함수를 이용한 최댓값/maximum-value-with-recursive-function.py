n=int(input())
arr=list(map(int, input().split()))

def f(n,arr):
    if n==1:
        return arr[0]
    elif n==2:
        if arr[n-1]>arr[n-2]:
            arr[n-2]=arr[n-1]
            return arr[n-2]
        else:
            return arr[n-2]
    else:
        if arr[n-1]>arr[n-2]:
            arr[n-2]=arr[n-1]
        return f(n-1,arr)

print(f(n,arr))
