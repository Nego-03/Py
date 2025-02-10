class Student:
    def __init__(self, name, gender,age):
        self.name = name
        self.gender = gender
        self.age = age

    def study(self):
        print(self.name, "is studying")

student1 = Student("Innocent", "male", 34)
print(student1.name, student1.gender, student1.age)
student1.study()
student2 = Student("Abigail", "Female", 22)