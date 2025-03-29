n = int(input())
arr = list(map(int, input().split()))

def lcm(a,b):
    for i in range(max(a,b),a*b+1):
        if i%a==0 and i%b==0:
            return i

def func(n,arr):
    if n==1:
         return print(lcm(arr[n],arr[n-1]))
        
    arr[n-1]=lcm(arr[n],arr[n-1])
    func(n-1,arr)

n-=1
func(n,arr)