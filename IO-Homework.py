import json

with open('bootcamp.txt', 'r') as f:
    students = json.load(f)

print(students)

def add_student():
  student = {
      'name': input('Please enter the student name: '),
      'age': input('Please enter the student age: '),
      'email': input('Please enter the student email: ')
  }
  students.append(student)

  with open('bootcamp.txt', 'w') as f:
    json.dump(students, f)
    print('The student has been added to the bootcamp')

def remove_student():
    remove = input('Please enter the student\'s name you want to remove: ')
    removed = list(filter(lambda i: i['name'] != remove, students))

    with open('bootcamp.txt', 'w') as f:
        json.dump(removed, f)
        print('The student has been removed from the bootcamp')

def view_all_students():
    for student in students:
        print('{name} , {age}, {email}'.format(**student))

def search_student():
    search = input('Please enter the student\'s name you want to search: ')
    match = list(filter(lambda i: i['name'] == search, students))
    print('{name} , {age}, {email}'.format(**match[0]))


search_student()
