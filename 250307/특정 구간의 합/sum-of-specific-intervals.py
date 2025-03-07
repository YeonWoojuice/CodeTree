n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for i in range(m)]

def add(n,m,queries):
    add=0
    global arr
    for x,y in queries:
        for j in range(x-1,y):
            add+=arr[j]    
        print(add)
        add=0

add(n,m,queries)



