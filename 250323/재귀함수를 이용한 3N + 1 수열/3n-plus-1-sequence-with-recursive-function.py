n = int(input())
add=0

def f(n,add):
    if n==1:
        print(add)
    else:
        if n%2==0:
            f(n//2,add+1)
        else:
            f(n*3+1,add+1)

f(n,add)