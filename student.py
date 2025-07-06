class Student:
    def __init__(self, name, course, year):
        self.name = name
        self.course = course
        self.year = year

    def introduction(self):
        return f"{self.name}, Welcome to {self.course} "
        
student1 = Student("Elvis", "Web Dev", 1)

print(student1.introduction())