a, b = map(int, input().split())
# Write your code here!
cnt=0
is_prime = True

for i in range (a,b+1):
    for j in range(2,i):
        if (i%j==0 or i==1):
            is_prime=False
        
    if is_prime:
        cnt+=i
    is_prime = True

print(cnt)