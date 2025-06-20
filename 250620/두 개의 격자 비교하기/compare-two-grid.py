N,M=map(int, input().split())
arr1=[
    list(map(int, input().split()))
    for _ in range(N)
]

input()

arr2=[
    list(map(int, input().split()))
    for _ in range(M)
]

for i in range(N):
    for j in range(M):
        if (arr1[i][j]==arr[i][j]):
            print(0,end=" ")
        else:
            print(1,end=" ")
    print()