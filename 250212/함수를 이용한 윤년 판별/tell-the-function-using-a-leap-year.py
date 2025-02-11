y = int(input())

def leap_year(y):
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        return True
    else: 
        return False
if leap_year(y)==True:
    print("true")
else:
    print("false")