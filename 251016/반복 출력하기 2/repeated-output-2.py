def func(n):
    for i in range(n):
        func2()

def func2():
    print("HelloWorld")

n=int(input())
func(n)
