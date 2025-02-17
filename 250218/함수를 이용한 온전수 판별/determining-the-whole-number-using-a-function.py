a, b = map(int, input().split())
add=0 

def func(i):
    if (i%2==0):
        return False
    elif (i%10==5):
        return False
    elif (i%3==0):
        if (i%9==0):
            return True
        else:
            return False
    else:
        return True


for i in range(a,b+1):
    if (func(i)==True):
        add+=1
    
print(add)

# Write your code here!