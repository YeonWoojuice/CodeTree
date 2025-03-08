n = int(input())

def print_number(n):

    if (n!=0):
        print(f"{8-n}",end=" ")
        if (n==1):
            print()
        print_number(n-1)
        print(f"{8-n}",end=" ")

print_number(n)