n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for i in range(n)]
sort_str=[]

for j in range(n):
    if t == str[j][0:len(t)]:
        sort_str.append(str[j])
        
sort_str.sort()
print(sort_str[k-1])







