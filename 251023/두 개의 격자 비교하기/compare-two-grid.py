import sys
input=sys.stdin.readline
n,m=map(int, input().split())
arr=[list(map(int, input().strip().split()))for _ in range(m)]
input()
arr2=[list(map(int, input().strip().split()))for _ in range(m)]
for i in range(n):
    for j in range(m):
        if arr[i][j]==arr2[i][j]:
            print(0,end=" ")
        else:
            print(1,end=" ")
    print()