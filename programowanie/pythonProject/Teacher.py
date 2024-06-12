from Person import Person


class Teacher(Person):
    def __init__(self, name, surname, subject):
        super().__init__(name, surname)
        self.subject = subject

    def get_teacher_info(self):
        return f"Teacher: {self.get_full_name()}, Subject: {self.subject}"
