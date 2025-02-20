M, D = map(int, input().split())

def month_day(M,D):
    if (0<M<7):
        if (M%2==0 and M!=2):
            if (0<D<31):
                return True
        elif (M==2):
            if (0<D<29):
                return True
        else:
            if (0<D<32):
                return True
    elif (M<13):
        if (M%2==0):
            if (0<D<32):
                return True
        else:
            if (0<D<31):
                return True

if (month_day(M,D)==True):
    print("Yes")
else:
    print("No")
    

    
# Write your code here!