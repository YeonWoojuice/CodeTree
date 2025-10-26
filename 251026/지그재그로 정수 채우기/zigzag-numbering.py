import sys
input = sys.stdin.readline

n, m = map(int,input().strip().split())

add = 0
arr = [[0 for _ in range(m)] for _ in range(n)]

for i in range(m):
    for j in range(n):
        if i%2==0:
            arr[j][i] = add
            add += 1
        else:
            arr[n-j-1][i] = add
            add += 1

for a in arr:
    print(*a)
