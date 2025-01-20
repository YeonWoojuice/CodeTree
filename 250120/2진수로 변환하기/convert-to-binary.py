n=29
digit=[]

while True:
    if n<2:
        digit.append(n)
        break

    digit.append(n % 2)
    n//=2

for digit in digit[::-1]:
    print(digit, end="")
    

