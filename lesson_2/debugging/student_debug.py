def process_student(student_data):
    name = student_data.get('name')
    grade = student_data.get('grade')
    return (name, grade)

def average_grade(grades):
    total = sum(grades)
    average = total / len(grades)
    return average

students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob'}, 
    {'name': 'Jack', 'grade': 72}, #moved to it's own line to help understand the code
    {'name': 'Jane', 'grade': 75},
]

def collect_grades(students):
    grades = []
    for student in students:
        name, grade = process_student(student)
        if grade is not None:      #catch the problem if one student doesn't have a grade
            grades.append(grade)
    return grades

grades = collect_grades(students)
print(f'{average_grade(grades):.2f}')
# TypeError: unsupported operand type(s) for +: 'int'
# and 'NoneType'