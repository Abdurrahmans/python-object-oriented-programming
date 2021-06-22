class Person:
    def __init__(self, person_name: str, date_of_birth: int, height: int = None):
        self.name = person_name
        self.date_of_birth = date_of_birth
        self.height = height

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_year_of_birth(self):
        return self.date_of_birth

    def get_summary(self):
        return f"name: {self.name}, DOB: {self.date_of_birth}, height: {self.height if self.height is not None else 'Invalid'}"


a_person = [
    Person('Abdur Rahman', 1997, 75),
    Person('maheen', 1930, 60),
    Person('saddam', 1960),
    Person('jihad', 2020, 80),
    Person('Saba', 1940, ),
    Person('jihad', 1950, 90)]

for person in a_person:
    if person.get_year_of_birth() >= 1950:
        print(person.get_summary())


class Student(Person):

    def __init__(self, person_name: str, date_of_birth: int, email_id: str, student_id: str):
        super(Student, self).__init__(person_name, date_of_birth)
        self.email = email_id
        self.student_id = student_id

    def get_summary(self):
        return f"name: {self.get_name()}, DOB: {self.get_year_of_birth()}, Email: {self.email}"


student = Student('Abdur', 1997, 'abdur@gmail.com', 2001)
print(student.get_summary())
student.set_name('Abdur Rahman')
print(student.get_summary())
