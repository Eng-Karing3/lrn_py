class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = int(salary)

    def details(self):
        return f"Employee: {self.name}, Salary {self.salary} "
    
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def details(self):
        return f"Manager: {self.name}, Salary: {self.salary}, Department: {self.department}"
    

employee1 = Manager("John", 2000, "Sales")

print(employee1.details())
        