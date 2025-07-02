class Student:
    def __init__(self, name, sc1, sc2, sc3, res):
        self.name=name
        self.sc1=sc1
        self.sc2=sc2
        self.sc3=sc3
        self.res=res

n = int(input())

students=[]
for _ in range(n):
    name, sc1, sc2, sc3= tuple(input().split())
    res=int(sc1)+int(sc2)+int(sc3)
    students.append(Student(name, int(sc1), int(sc2), int(sc3), int(res)))

students.sort(key = lambda x: (x.res))

for student in students:
    print(student.name, student.sc1, student.sc2, student.sc3)


