N=int(input())
count=0
for i in range(1,N+1):
    for j in range(0,i):
        count+=1
        print(count,end=" ") 
    print()
    
    