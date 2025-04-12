n = int(input())
arr=[tuple(input().split())for i in range(n)]

class data:
    def __init__(self, d, dy,w):
        self.d=d
        self.dy=dy
        self.w=w

data_pron=[data(date, day, weather) for date, day, weather in arr]
results=[x for x in data_pron if x.w == "Rain"]
results=sorted(results, key=lambda x:x.d)

print(f"{results[0].d}",end=" ")
print(f"{results[0].dy}",end=" ")
print(f"{results[0].w}")
        