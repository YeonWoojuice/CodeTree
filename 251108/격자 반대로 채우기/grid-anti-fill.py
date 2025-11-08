import sys
n=int(sys.stdin.readline())
arr=list([0 for _ in range(n)]for _ in range(n))
add=1
for i in range(n):
    for j in range(n):
        arr[i][j]==add
        add+=1

for row in zip(arr):
    print(row)
    

        
