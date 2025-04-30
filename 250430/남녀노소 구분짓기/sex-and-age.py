Sex=int(input())
Age=int(input())

if (Age>18):
    if(Sex==0):
        print("MAN")
    else:
        print("WOMAN")
else:
    if (Sex==0):
        print("BOY")
    else:
        print("GIRL")
