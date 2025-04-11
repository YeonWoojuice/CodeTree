n = int(input())
arr=[tuple(input().split())for i in range(n)]

class data:
    def __init__(self, d, dy,w):
        self.d=d
        self.dy=dy
        self.w=w

data_pron=[data(date, day, weather) for date, day, weather in arr]

for j in range(n):
    if data_pron[j].w == "Rain":
        print(f"{data_pron[j].d}",end=" ")
        print(f"{data_pron[j].dy}",end=" ")
        print(f"{data_pron[j].w}")
        break;