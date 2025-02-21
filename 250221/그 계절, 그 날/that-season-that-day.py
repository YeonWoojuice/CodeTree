Y, M, D = map(int, input().split())

def countYear(Y,M,D):
    if ((Y%4==0 and (Y%100!=0)) or (Y%4==0 and (Y%100!=0) and (Y%400==0))):
        if (0<M<8):
            if (0<M<2):
                if (0<D<31):
                    return "Winter"
            elif (M==2):
                if (0<D<30):
                    return "Winter"
            elif (2<M<6):
                if(M%2==0):
                    if (0<D<31):
                        return "Spring"
                else:
                    if (0<D<32):
                        return "Spring"
            elif (6<M<8):
                if(M%2==0):
                    if (0<D<31):
                        return "Summer"
                else:
                    if (0<D<32):
                        return "Summer"
        elif (7<M<13):
            if (7<M<9):
                if(M%2==0):
                    if (0<D<32):
                        return "Summer"
            elif (8<M<12):
                if (M%2==0):
                    if (0<D<32):
                        return "Fall"
                else:
                    if (0<D<31):
                        return "Fall"
            elif (M==12):
                if (0<D<32):
                    return "Winter"
    else:
        if (0<M<8):
            if (0<M<2):
                if (0<D<31):
                    return "Winter"
            elif (M==2):
                if (0<D<29):
                    return "Winter"
            elif (2<M<6):
                if(M%2==0):
                    if (0<D<31):
                        return "Spring"
                else:
                    if (0<D<32):
                        return "Spring"
            elif (6<M<8):
                if(M%2==0):
                    if (0<D<31):
                        return "Summer"
                else:
                    if (0<D<32):
                        return "Summer"
        elif (7<M<13):
            if (7<M<9):
                if(M%2==0):
                    if (0<D<32):
                        return "Summer"
            elif (8<M<12):
                if (M%2==0):
                    if (0<D<32):
                        return "Fall"
                else:
                    if (0<D<31):
                        return "Fall"
            elif (M==12):
                if (0<D<32):
                    return "Winter"

if (countYear(Y,M,D)=="Spring" or countYear(Y,M,D)=="Summer" or countYear(Y,M,D)=="Fall" or countYear(Y,M,D)=="Winter"):
    print(countYear(Y,M,D))
else:
    print(-1)