import sys
for i in range(2):
    arr[i]=list(map(float,sys.stdin.readline().split()))
    print(sum(arr[i])/4,end=" ")
for j in range(4):
    print(sum(list(arr[i][j] for i in range(2)))/2,end=" ")
print(sum(arr))




