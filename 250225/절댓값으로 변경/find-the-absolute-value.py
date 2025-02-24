n = int(input())
arr = list(map(int, input().split()))

def absolute(n,arr):
    for i in range(0,n):
        if (arr[i]<0):
            arr[i]*=(-1)
    return arr

print(*(absolute(n,arr)))

# Write your code here!