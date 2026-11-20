class Student:
    school = "Berklee College of Music"
    students = []

    __slots__ = ("first_name", "last_name", "subjects", "__neptun_code")

    def __init__(self, first_name, last_name, subjects, neptun_code):
        self.first_name = first_name
        self.last_name = last_name
        self.subjects = subjects
        self.__neptun_code = neptun_code
        Student.students.append(self)

    def average(self):
        avg = round(sum(s["grade"] for s in self.subjects) / len(self.subjects), 2)
        print(f"{self.first_name} {self.last_name} ({self.__neptun_code}) average: {avg}")

    def credits(self):
        return sum(s["credit"] for s in self.subjects if s["grade"] > 1)

    def __bio(self):
        print("Top secret info")

    def _protected():
        pass


student = Student(
    "John",
    "Doe",
    [
        {"subject": "Math", "credit": 7, "grade": 1},
        {"subject": "Physics", "credit": 4, "grade": 3},
        {"subject": "Algo", "credit": 6, "grade": 2},
    ],
    "ABC123",
)
print(student, type(student))
print(student.first_name)
print(student.last_name)
student.first_name = "Jane"
# print(getattr(student, "first_name"))
# setattr(student, "first_name", "Jane")
print(student.first_name)
# student.hobbies = ["reading", "swimming"]
# print(student.hobbies)
student.average()
print(student.credits())
print(student.school)
print(Student.school)

student_2 = Student(
    "Jane",
    "Smith",
    [
        {"subject": "Math", "credit": 7, "grade": 4},
        {"subject": "Physics", "credit": 4, "grade": 4},
        {"subject": "Algo", "credit": 6, "grade": 3},
    ],
    "XYZ789",
)


print(Student.students)
# AttributeError: 'Student' object has no attribute '__neptun_code'
# print(student.__neptun_code)

# AttributeError: 'Student' object has no attribute '__bio'
# student.__bio()

# print(student._Student__neptun_code)
# student._Student__bio()
