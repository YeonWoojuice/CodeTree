a, b, c = map(int, input().split())
res=a*b*c
def f(res):
    if res<10:
        return res
    else:
        return f(res//10)+res%10

print(f(res))