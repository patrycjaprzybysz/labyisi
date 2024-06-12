from Person import Person


class Student(Person):
    def __init__(self, name, surname, student_id):
        super().__init__(name, surname)
        self.student_id = student_id

    def get_student_info(self):
        return f"Student: {self.get_full_name()}, ID: {self.student_id}"
