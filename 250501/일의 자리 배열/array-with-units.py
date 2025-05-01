list1 = list(map(int, input().split()))
for i in range(8):
    list1.append((list1[i]+list1[i+1])%10)

print(*list1)
