class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)

    def introduction(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old"
    
class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school

    def school_intro(self):
        return f"I study at {self.school}"
    
student1 = Student ("Elvis", 20, "Nyeri Tech")

print(student1.introduction())
print(student1.school_intro())

        

        