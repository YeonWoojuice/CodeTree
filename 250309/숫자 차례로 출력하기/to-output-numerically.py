n = int(input())

def print_number1(n):
    if n==0:
        return 
    print_number1(n-1)
    print(n,end=" ")

def print_number2(n):
    if n==0:
        return
    print(n,end=" ")
    print_number2(n-1)

print_number1(n)
print()
print_number2(n)

'''
고민했던 부분: print함수 호출 사이에 print-number()을 호출 하면
무조건 붙어서 출력되는 어떻게 두 줄로 출력 되도록 할수 있을까? 
'''