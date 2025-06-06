N=int(input())
for j in range(0,N):
    a,b= map(int, input().split())
    add=0
    for i in range(a,b+1):
        if i%2==0:
            add+=i
    print(add)