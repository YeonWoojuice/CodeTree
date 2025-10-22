import sys
input=sys.stdin.readline
str1=sorted(input().strip())
str2=sorted(input().strip())

print("Yes" if str1==str2 else "No")