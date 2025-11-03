import sys
input=sys.stdin.readline
arr=[list(map(int,input().strip().split()))for _ in range(2)]
def aver(arr):
    return sum(arr)/len(arr)
add=0
for row in arr: print(f'{aver(row):.1f}',end=" ") print()
for col in zip(*arr): print(f'{aver(col):.1f}',end=" ") print()
print(f'{aver([x for row in arr for x in row]):.1f}')
