import sys
input = sys.stdin.readline

n,m=map(int, input().split())
arr=list([0 for j in range(m)]for i in range(n))
add=0
for i in range(n):
    for j in range(m,0,-1):
        if j>-1:
            add+=1
            print(add, end=" ")
            add = arr[i][j]
            print(arr[i][j],end=" ")
    print()
        
            
