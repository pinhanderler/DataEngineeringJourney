class School:
    def __init__(self, name, foundation_year):
        self.name = name
        self.foundation_year = foundation_year
        self.students = []
        self.teachers = {}

    def add_new_student(self, student_name, classroom):
        self.students.append({"name": student_name, "class": classroom})

    def add_new_teacher(self, teacher_name, branch):
        self.teachers[teacher_name] = branch

    def view_student_list(self):
        print("\nStudent List:")
        for student in self.students:
            print(f" - {student['name']} ({student['class']})")

    def view_teacher_list(self):
        print("\nTeacher List:")
        for teacher, branch in self.teachers.items():
            print(f" - {teacher} ({branch})")


if __name__ == "__main__":
    my_school = School("Sunrise High School", 2001)
    my_school.add_new_student("Alice", "10-A")
    my_school.add_new_student("Bob", "11-B")
    my_school.add_new_teacher("Mr. Smith", "Math")
    my_school.add_new_teacher("Mrs. Johnson", "English")
    my_school.view_student_list()
    my_school.view_teacher_list()
