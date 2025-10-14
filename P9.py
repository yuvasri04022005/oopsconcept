class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display(self):
        print(f"Student: {self.name}, Grade: {self.grade}")

class GraduateStudent(Student):
    def __init__(self, name, grade, thesis_topic):
        super().__init__(name, grade)
        self.thesis_topic = thesis_topic

    def display(self):
        super().display()
        print(f"Thesis Topic: {self.thesis_topic}")

stu = GraduateStudent("Yuva", "A+", "AI-based Automation")
stu.display()
