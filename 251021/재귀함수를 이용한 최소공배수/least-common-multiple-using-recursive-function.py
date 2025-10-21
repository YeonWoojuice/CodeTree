import sys
import math
n=int(sys.stdin.readline())
list1=list(map(int,sys.stdin.readline().split()))

def f(n, list1):
    if n==1: return math.lcm(list1[1],list1[0])
    else:
        f(n-1, list1)
        return list1[n-1]= math.lcm(list1[n],list1[n-1])
print(f(n-1,list1))