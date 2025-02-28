a, b = map(int, input().split())

def compare(a,b):
    if (a>b):
        a*=2
        b+=10
        return a,b
    else:
        a+=10
        b*=2
        return a,b

print(*(compare(a,b)))
        