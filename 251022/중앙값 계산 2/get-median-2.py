import sys
input = sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))
sort1=[]

for i in range(n):
    sort1.append(arr[i])
    sort1.sort()
    if i%2==0:
        print(sort1[i//2],end=" ")

        