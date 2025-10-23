import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(3)]
input()
arr2 = [list(map(int, input().split())) for _ in range(3)]

for i in range(3):
    for j in range(3):
        print(arr[i][j] * arr2[i][j], end=" ")
    print()
