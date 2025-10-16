N=int(input())

def func2(N):
    if N==0:
        return N
    print(7-(N-1),end=" ")
    func2(N-1)

def func(N):
    if N==0:
        return N
    print(N,end=" ")
    func(N-1)

func2(N)
print()
func(N)