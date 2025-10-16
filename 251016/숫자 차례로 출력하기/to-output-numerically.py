N=int(input())

def func2(N):
    if N==0:
        return 
    func2(N-1)
    print(N,end=" ")

def func(N):
    if N==0:
        return N
    print(N,end=" ")
    func(N-1)

func2(N)
print()
func(N)