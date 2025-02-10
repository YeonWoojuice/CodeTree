a, b = map(int, input().split())
cnt=0 

def game(i):
    value_str=f'{i}'
    list_value=list(value_str)

    for j in range(0,len(list_value)):
        if list_value[j]=='3' or list_value[j]=='6' or list_value[j]=='9':
            return 1

for i in range(a,b+1):
    if (game(i)==1 or i%3==0):
        cnt+=1

print(cnt)
 