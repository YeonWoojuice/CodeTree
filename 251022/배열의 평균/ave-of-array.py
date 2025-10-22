import sys
arr=[list(map(float,sys.stdin.readline().split()))for i in range(2)]
for i in range(2):
    print(sum(arr[i])/4,end=" ")
print()
for j in range(4):
    print(sum(list(arr[i][j] for i in range(2)))/2,end=" ")
print()
print(sum(arr[0]+arr[1])/8)




