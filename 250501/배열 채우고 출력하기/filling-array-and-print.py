list1=list(map(str,input().split()))

for i in range(len(list1)):
    print(list1[(len(list1)-1)-i],end="")