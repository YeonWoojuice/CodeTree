import sys
n, m = map(int,sys.stdin.readline().split())
arr=[[0 for _ in range(m)]for _ in range(n)]

cnt=1

for i in range(m):
    curr_col = i
    curr_row = 0
    while curr_col >= 0 and curr_row < n:
        arr[curr_row][curr_col]=cnt
        curr_col-=1
        curr_row+=1
        cnt+=1

for i in range(1, n):
    curr_col = m-1
    curr_row = i
    while curr_row < n and curr_col >= 0:
        arr[curr_row][curr_col] = cnt
        curr_col-=1
        curr_row+=1
        cnt+=1



for row in range(n):
    for col in range(m):
        print(arr[row][col],end=' ')
    print()

