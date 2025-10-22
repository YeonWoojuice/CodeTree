import sys
n=int(sys.stdin.readline())
arr1=list(map(int,sys.stdin.readline().split()))
arr2=list(map(int,sys.stdin.readline().split()))
arr1.sort()
arr2.sort()

if arr1==arr2:
    print("Yes")
else:
    print("No")

        