number_of_students = int(input("Enter the number of students: "))
students_grades = []

for student in range(number_of_students):
    student_grade = float(input(f"Enter the grade for student {student + 1}: "))
    students_grades.append(student_grade)

sum_of_grades = sum(students_grades)
average_grade = sum_of_grades / len(students_grades)

print("Average grade:", average_grade)
