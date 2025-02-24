a, b = map(int, input().split())
tmp=0

def func(a,b):
    if (a<b):
        a*=2
        b+=25
    elif(a>b):
        a+=25
        b*=2
    return a,b


print(*(func(a,b)))
 
# Write your code here!