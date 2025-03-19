n = int(input())
arr = list(map(int, input().split()))

def maximum(n,arr): #4 #3 #2
    if (n>=2):
        if (arr[n-1]>arr[n-2]):  # 9>7 #9>5 #9>1
            arr[n-2]=arr[n-1] # 7=9 #5=9 #1=9
        if n==2:
            print(arr[0])
    else:
        print(arr[0])


def f(n,arr):
    if (n==2):
        return maximum(n,arr)

    maximum(n,arr) # 4, 1 5 7 9 # 3,
    f(n-1,arr) # 3,arr #2,arr
    
f(n,arr)
    
    