a, b = map(int, input().split())

add=0

def func(i):
    count=0
    for j in range(2,i):
        if (i%j==0):
            count+=1
    if count>0:
        return False
    else:
        return True
            

def addEven(i):
    rest=0
    rest2=0
    result=0

    if i<10:
        rest=i%10
        result=rest
    else:
        rest2=i//10
        rest=i%10
        result=rest+rest2

    if result%2==0:
        return True
    else:
        return False

for i in range(a,b+1):
    if (func(i)==True):
        if (addEven(i)==True):
            add+=1

print(add)

        