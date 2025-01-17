n = int(input())
arr = list(map(int, input().split()))

def lcm(a,b):
    return (a*b)//gcd(a,b)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def find_lcm(arr, n):
    if n == 1:
        return arr[0]
    return lcm(arr[n-1], find_lcm(arr, n-1))

print(find_lcm(arr,n))

# Write your code here!