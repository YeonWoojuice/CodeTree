class Student:
    def __init__(self,name,kor,eng,math):
        self.name=name
        self.kor=kor
        self.eng=eng
        self.math=math

n = int(input())

students=[]
for _ in range(n):
    name,kor,eng,math = tuple(input().split())
    students.append(Student(name,int(kor),int(eng),int(math)))
    
students.sort(key=lambda x: (-x.kor,-x.eng,-x.math))

for student in students:
    print(student.name, student.kor, student.eng, student.math) 