import sys
input = sys.stdin.readline
n=int(input())
arr=sorted(map(int, input().split()))
print(max(x+y for x,y in zip(arr[:n],reversed(arr[n:]))))
