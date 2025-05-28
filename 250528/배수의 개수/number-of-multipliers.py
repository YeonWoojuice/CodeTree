N=[0]*10
for i in range(10):
    N[i]=int(input())
cnt1=0
cnt2=0
for i in range(0,len(N)):
    if N[i]%3==0:
        cnt1+=1
    if N[i]%5==0:
        cnt2+=1
print(cnt1, end=" ")
print(cnt2)

        

