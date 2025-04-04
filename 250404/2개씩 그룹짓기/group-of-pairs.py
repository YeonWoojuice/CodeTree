n = int(input())
nums = list(map(int, input().split()))
adds1=[]
adds2=[]


for i in range(n):
    adds1.append(nums[2*i]+nums[2*i+1]) # 10 8 8
    adds1.sort(reverse=True) # 10 8 8
        
for j in range(n-1):
    adds2.append(nums[1+2*j]+nums[(2+2*j)%(n*2-1)]) # 2+7 
    adds2.sort(reverse=True) # 10 5
        
if (adds1[0]<adds2[0]):
    print(adds1[0])
else:
    print(adds2[0])




