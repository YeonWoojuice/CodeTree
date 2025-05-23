N=int(input())
cnt=0
for i in range(N):
    if i % 2 == 0 or i % 5 == 0 or i % 3 == 0 :
        cnt+=1

print(N-cnt)
