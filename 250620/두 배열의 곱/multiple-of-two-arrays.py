arr1=[
    list(map(int, input().split()))
    for i in range(3)
]
arr2=[
    list(map(int, input().split()))
    for j in range(3)
]

for k in range(0,3):
    for l in range(0,3):
        print(arr1[k][l]*arr2[k][l])
    print()