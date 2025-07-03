class Student:
    def __init__(self,height,weight,count):
        self.height=height
        self.weight=weight
        self.count=count

n = int(input())

students=[]
for i in range(n):
    height, weight, count = tuple(input().split()) + (i+1,)
    students.append(Student(int(height), int(weight), int(count)))

students.sort(key = lambda x: (-x.height, -x.weight, x.count))

for student in students:
    print(student.height, student.weight, student.count)


