A,B=map(str, input().split())
if (len(A)<len(B)):
    print(B)
elif (len(A)==len(B)):
    print("same")
else:
    print(A)