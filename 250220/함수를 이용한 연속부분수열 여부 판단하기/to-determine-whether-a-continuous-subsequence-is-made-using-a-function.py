n1, n2 = map(int, input().split()) #수열 a의 원소 개수
a = list(map(int, input().split())) # 수열 b의 원소 개수
b = list(map(int, input().split()))



def continue_section(n1, n2):
    for i in range(0,n1-n2):
        if (a[i:i+n2:1]==b):
            return True



    
if (continue_section(n1,n2)==True):
    print("Yes")
else:
    print("No")
