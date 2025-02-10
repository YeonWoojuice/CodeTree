n = int(input())
cnt=0
# Write your code here!

def return_number(n):
    tens=n//10
    ones=n%10
    result=tens+ones
    return result

if (return_number(n)%5==0 and n%2==0):
    print("Yes")
else:
    print("No")
