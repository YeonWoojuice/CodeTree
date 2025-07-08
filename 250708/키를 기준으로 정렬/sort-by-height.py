class Student:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

n = int(input())

students = []

for _ in range(n):
    n_i, h_i, w_i = input().split()
    student = Student(n_i, int(h_i), int(w_i))
    students.append(student)


students.sort(key=lambda x: x.height)


for student in students:
    print(student.name, student.height, student.weight)