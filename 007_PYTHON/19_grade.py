#grade of students according to marks

def grade_student(marks):
    if marks >= 90:
        return 'A+'
    elif marks >= 80:
        return 'A'
    elif marks >= 70:
        return 'B'
    elif marks >= 60:
        return 'C'
    elif marks >= 50:
        return 'D'
    else:
        return 'F'

# List of students and their marks
students_marks = {
    'John': 92,
    'Alice': 85,
    'Bob': 74,
    'Charlie': 65,
    'David': 48
}

# Grading the students
grades = {}
for student, marks in students_marks.items():
    grades[student] = grade_student(marks)

# Displaying the grades
for student, grade in grades.items():
    print(f"{student}: {grade}")
