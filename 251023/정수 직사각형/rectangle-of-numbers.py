import sys
n,m = map(int,sys.stdin.readline().split())
add=1
for i in range(n):
    for j in range(m):
        print(add,end=" ")
        add+=1
    print()