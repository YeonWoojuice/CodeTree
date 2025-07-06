class Point:
    def __init__(self,num, x, y):
        self.num, self.x, self.y = num, x, y

    def manh(self):
        return abs(self.x) + abs(self.y)

n = int(input())
points = [Point(int(i), *map(int, input().split())) for i in range(n)]

points.sort(key = lambda p:(p.manh()))

for point in points:
    print(point.num+1)
