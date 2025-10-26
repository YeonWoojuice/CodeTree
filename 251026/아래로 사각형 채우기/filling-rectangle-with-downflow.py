import sys
n=int(input())
arr=[[0for i in range(n)]for i in range(n)]
add=1
for i in range(n):
    for j in range(n):
        arr[j][i]=add
        add+=1

for raw in arr:
    print(*raw)