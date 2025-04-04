n = int(input())
nums = list(map(int, input().split()))
adds=[]


for i in range(n):
    adds.append(nums[2*i]+nums[2*i+1]) # 8 7
    adds.sort(reverse=True) # 8 7
        
for j in range(n):
    adds.append(nums[1+2*j]+nums[(1+2*j)%(n-1)])
    adds.sort(reverse=True)
        
if (adds[0]<adds[n]):
    print(adds[0])
else:
    print(adds[n])




