import sys
input=sys.stdin.readline
n,k,T=input().split()
n,k=int(n),int(k)
arr=sorted([input().strip() for i in range(n)])
filtered=[s for s in arr if s.startswith(T)]
print(filtered[k-1])