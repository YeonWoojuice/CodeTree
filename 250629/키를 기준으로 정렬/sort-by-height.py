class Student:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

# 학생 수 입력
n = int(input())

# 학생 객체들을 저장할 리스트
students = []

# n명의 학생 정보 입력받기
for _ in range(n):
    n_i, h_i, w_i = input().split()
    # Student 객체 생성하여 리스트에 추가
    student = Student(n_i, int(h_i), int(w_i))
    students.append(student)

# 키(height)를 기준으로 정렬
students.sort(key=lambda x: x.height)

# 정렬된 결과 출력
for student in students:
    print(student.name, student.height, student.weight)