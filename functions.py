# Built-In Functions/Standard-Library

y = max(45, 89, 75, 56,39, 12)
print("The maximum value is", y)

x = min(67, 85, 76, 54, 95, 42)
print("The minimum value is", x)

# User-defined functions
def school():
    print("eMobilis")

school()

def add():
    num1 = 5
    num2 = 3
    print(num1 +num2)

add()

# Parameter/Variable and Argument/Value
def multiply(a , b):
    print(a * b)

multiply(6,9)
multiply(22,9)


def employee(name, age, gender, salary, position):
    print(name, age, gender, salary, position)

employee("Yoh",54, "Male", 510000,"CEO")
employee("Hoy",45, "Female", 410000, "Managing Director")
employee("Ohy",44, "Male", 440000, "Project Manager")

#A program to display details of 5 patients
# Using a user-defined function implement parameter and argument
# fullname, gender, age, disease

def patient(fullname, gender, age, disease):
    print(fullname, gender, age, disease)

patient("Rann Re","Male",36,"Pneumonia")
patient("Dan Phil","Male",36,"Malaria")
patient("Hank Le","Male",36,"Malaria")
patient("Rose Tig","Female",36,"Cancer")
patient("Shan Heer","Female",36,"Cholera")