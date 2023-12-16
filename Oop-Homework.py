# 1.Create a Person class with the following attributes: name(string) and age(integer)
# 2.Add a method to the Person class called describe that prints a description of the person.

class Person:
    def __init__(self, name, age):
        self.name = str(name)
        self.age = int(age)

    def describe(self):
        print(f'Their name is {self.name} and is {self.age} years old')

# 3.Create a Student class that inherits from Person and has an additional attribute: student_id(integer)
# 4.Add a method to the Student class called describe that overrides the describe method of the Person class . The new describe method should print the name, age, gender, and student ID of the student.


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = int(student_id)

    def describe(self):
        print(f'The student name is {self.name}, is {self.age} years old and their student ID is {self.student_id}')

# 5.Create a Course class with the following attributes: name(string), teacher(string) and students(list)
# 6.Add a method to the Course class called add_student that takes a Student object as a parameter and adds the student to the course's list of students.
# 7.Add a method to the Course class called list_students that prints the names of all the students in the course.


class Course():
    def __init__(self, name, teacher):
        self.name = str(name)
        self.teacher = str(teacher)
        self.students = []

    def add_student(self, student):
        self.students.append(student.name)

    def list_students(self):
        print(f"The students of this course are: {self.students}")


# 8.Create instances of the Student class and add them to an instance of the Course class using the add_student method.

student1 = Student('Ana', 21, 1)
student2 = Student('Pedro', 20, 2)
student3 = Student('Lucrecia', 22, 3)

course = Course('History', 'Profesor Jirafales')
course.add_student(student1)
course.add_student(student2)
course.add_student(student3)

# 9.Call the list_students method on the instance of the Course class to verify that the students were added successfully.

course.list_students()
