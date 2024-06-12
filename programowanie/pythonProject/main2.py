from Student import Student
from Teacher import Teacher

# Przykład użycia:
student = Student("Jan", "Kowalski", "s12345")
teacher = Teacher("Anna", "Nowak", "Mathematics")

print(student.get_student_info())  # Output: Student: Jan Kowalski, ID: s12345
print(teacher.get_teacher_info())  # Output: Teacher: Anna Nowak, Subject: Mathematics
