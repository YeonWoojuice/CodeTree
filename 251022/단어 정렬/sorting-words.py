import sys 
n=int(sys.stdin.readline())
arr=list(sys.stdin.readline().strip()for i in range(n))
arr.sort()
for x in arr:
    print(x)
