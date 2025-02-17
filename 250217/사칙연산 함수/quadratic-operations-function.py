a, o, c = input().split()
a = int(a)
c = int(c)

def add(a,c):
    res=a+c
    print(f'{a} {o} {c} = {res}')

def sub(a,c):
    res=a-c
    print(f'{a} {o} {c} = {res}')

def div(a,c):
    res=int(a/c)
    print(f'{a} {o} {c} = {res}')

def mul(a,c):
    res=a*c
    print(f'{a} {o} {c} = {res}')

if (o=="+"):
    add(a,c)

elif (o=="-"):
    sub(a,c)

elif (o=="/"):
    div(a,c)

elif (o=="*"):
    mul(a,c)

else:
    print(False)