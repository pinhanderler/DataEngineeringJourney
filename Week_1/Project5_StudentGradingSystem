# Project 5: Student Grading System 

students = {}

for i in range(3):
    name = input(f"Enter student {i+1} name: ")
    grades = []
    for j in range(3):
        grade = int(input(f"Enter grade {j+1} for {name}: "))
        grades.append(grade)
    students[name] = grades

print("\nStudent averages:")
highest_avg = 0
top_student = ""

for name, grades in students.items():
    avg = sum(grades) / len(grades)
    print(f"{name}: {avg}")
    if avg > highest_avg:
        highest_avg = avg
        top_student = name

print("\n Highest average:", top_student, "-", highest_avg)
