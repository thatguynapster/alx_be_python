class Student:
    """docstring for Student."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_student_details(self):
        print('\nStudent Details:')
        student = f"Name: {self.name}\nAge: {self.age} years"
        return student
