arr1=[
    list(map(int, input().split()))
    for _ in range(4)
]
sum=0
for i in range(4):
    for j in range(4):
        sum+=arr1[i][j]
    print(sum)
    sum=0