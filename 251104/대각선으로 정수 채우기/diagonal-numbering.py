import sys
n, m = map(int,sys.stdin.readline().split())
arr=[[0 for i in range(n)]for i in range(m)]

cnt=1

for i in range(n):
    curr_col = i
    curr_row = 0
    while curr_col >= 0 and curr_col < n:
        arr[curr_row][curr_col]=cnt
        curr_col-=1
        curr_row+=1
        cnt+=1


for i in range(0,m):
    curr_col = n-1
    curr_row = i+1
    while curr_col >= 0 and curr_row < m:
        arr[curr_row][curr_col] = cnt
        curr_col-=1
        curr_row+=1
        cnt+=1

for row in arr:
    print(*row)

