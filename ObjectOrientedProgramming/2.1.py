# class definition
class Student:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.grade = ""  # New attribute added

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student3 = Student()

    # Assigning values to the first student
    student1.name = "Dominic"
    student1.age = 19
    student1.grade = "A"

    # Assigning values to the second student
    student2.name = "Olivia"
    student2.age = 21
    student2.grade = "B"

    # Assigning values to the third student
    student3.name = "Sophia"
    student3.age = 20
    student3.grade = "A"

    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old, Grade: {student1.grade}')
    print(f'{student2.name}, {student2.age} years old, Grade: {student2.grade}')
    print(f'{student3.name}, {student3.age} years old, Grade: {student3.grade}')

if __name__ == "__main__":
    main()
