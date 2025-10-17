N=int(input())

def func(N):
    if N==0:
        return N
    func(N-1)
    print(N,end=" ")

def func2(N):
    if N==0:
        return N
    print(N,end=" ")
    func2(N-1)    

func(N)
print()
func2(N)