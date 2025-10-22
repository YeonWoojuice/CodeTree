import sys
n=4
for i in range(n):
    arr=map(int,sys.stdin.readline().split())
    sum_val=sum(arr)
    print(sum_val)