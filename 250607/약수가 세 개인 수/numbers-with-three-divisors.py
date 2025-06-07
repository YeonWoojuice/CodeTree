start, end = map(int, input().split())

add=0
cnt=0
for i in range(start, end+1):
    for j in range(1,i+1):
        if i%j==0:
            add+=1
    if add==3:
        cnt+=1
    add=0
print(cnt)