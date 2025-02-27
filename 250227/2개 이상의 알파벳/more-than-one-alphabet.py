A = input()

def transform(A):
    Aarray=list(A)
    for i in range(0,len(Aarray)-1):
        if (Aarray[i]!=Aarray[i+1]):
            return False

if (transform(A)==False):
    print("Yes")
else:
    print("No")

# Please write your code here.