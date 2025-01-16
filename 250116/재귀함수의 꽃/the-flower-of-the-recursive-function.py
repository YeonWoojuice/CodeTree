N = int(input())

def func(N): #3 
    if N <= 0:
        return
    print(N, end=' ') #3 #2 #1
    func(N-1)
    print(N, end=' ') 
# Write your code here!

func(N)