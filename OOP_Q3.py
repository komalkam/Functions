class Student:
    def __init__(self, name, age, roll_number):
        self.name = name
        self.age = age
        self.roll_number = roll_number
        self.grades = {}

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_roll_number(self):
        return self.roll_number

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_roll_number(self, roll_number):
        self.roll_number = roll_number

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def get_grade(self, subject):
        return self.grades.get(subject, None)

    def get_all_grades(self):
        return self.grades

    def calculate_average_grade(self):
        if not self.grades:
            return 0

        total_grades = sum(self.grades.values())
        return total_grades / len(self.grades)

if __name__ == "__main__":
    student1 = Student("Alice", 17, "A001")
    student1.add_grade("Math", 90)
    student1.add_grade("Science", 85)
    student1.add_grade("History", 78)

    student2 = Student("Bob", 16, "A002")
    student2.add_grade("Math", 92)
    student2.add_grade("Science", 88)
    student2.add_grade("History", 95)

    print(f"{student1.get_name()} (Roll Number: {student1.get_roll_number()}, Age: {student1.get_age()})")
    print("Grades:", student1.get_all_grades())
    print("Average Grade:", student1.calculate_average_grade())

    print(f"{student2.get_name()} (Roll Number: {student2.get_roll_number()}, Age: {student2.get_age()})")
    print("Grades:", student2.get_all_grades())
    print("Average Grade:", student2.calculate_average_grade())