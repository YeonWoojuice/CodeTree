import sys
arr=[list(map(int, sys.stdin.readline().split()))for i in range(4)]
add=0
for i in range(4):
    for j in range(4):
        if (i>=j):
            add+=arr[i][j]
print(add)
