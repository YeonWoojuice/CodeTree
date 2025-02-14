a, b = map(int, input().split())

def square(a,b):
    mul=1
    i=1
    for i in range(1,b+1):
        mul*=a
    print(mul)

square(a,b)
# Write your code here!