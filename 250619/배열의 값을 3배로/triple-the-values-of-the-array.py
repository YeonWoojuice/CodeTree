arr=[
    list(map(int, input().split()))
    for i in range(3)
]

for j in range(3):
    for k in range(3):
        arr[j][k]*=3

for row in arr:
    for elem in row:
        print(elem,end=" ")
    print()