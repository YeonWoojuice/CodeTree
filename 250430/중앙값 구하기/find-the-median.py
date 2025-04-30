A,B,C=map(int,input().split(" "))
if (A>B and A>C):
    if (B>C):
        print(B)
    else:
        print(C)
elif (B>A and B>C):
    if (A>C):
        print(A)
    else:
        print(C)
elif(C>A and C>B):
    if (A>B):
        print(A)
    else:
        print(B)