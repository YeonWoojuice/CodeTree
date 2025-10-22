import sys
input=sys.stdin.readline
str1=sorted(str(input()))
str2=sorted(str(input()))

print("Yes" if str1==str2 else "No")