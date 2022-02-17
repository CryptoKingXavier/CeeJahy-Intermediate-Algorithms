class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        
    def get_grade(self):
        return self.grade

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)

student = [Student("Blessing", 20, 95),
            Student("Favour", 18, 85),
            Student("Caleb", 16, 80),
            Student("Joshua", 14, 75)]

course = Course("Science", len(student))

def StudentCatalogue():
    name_list, age_list, grade_list = [], [], []
    for i in range(len(student)):
        course.add_student(student[i])
    for i in range(len(student)):
        name_list.append(student[i].get_name())
        age_list.append(student[i].get_age())
        grade_list.append(student[i].get_grade())
    for name, age, grade in zip(name_list, age_list, grade_list):
        print(f"Name: {name},   Age: {age},   Grade: {grade}")
    print(f"The Aggregate Course Average is: {course.get_average_grade():.2f}")

StudentCatalogue()
