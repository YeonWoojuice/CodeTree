N = int(input())

def square(N): 
    if N<10:
        return N*N
    return square(N//10)+(N%10)*(N%10) 

print(square(N))
