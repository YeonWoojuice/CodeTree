n = int(input()) 
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

def f(A,B,n):
    for i in range(0,n):
        if (A[i]!=B[i]):
            return print("No")
    print("Yes")

f(A,B,n)
    
     