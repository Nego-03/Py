class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

def info(self):
    print(self.position, "is earning" ,self.salary)

employee1 = Employee("John","CEO", 345000)
print(employee1.name,employee1.position,employee1.salary)
employee1.info()

employee2 = Employee("Jane","Mangaing Director", 300000)

employee3 = Employee("Jane","Mangaing Director", 285000)
employee4 = Employee("Jane","Mangaing Director", 245000)