A,B = map(int, input().split())
add=0
for i in range(A,B+1):
    if i%2==0:
        add+=i

print(add)
