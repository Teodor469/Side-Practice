class Students:
    def __init__(self) -> None:
        self.database = {}

    def add_student(self, name, roll_number, age, subjects):
        if roll_number not in self.database:
            self.database[roll_number] = {'name': name, 'roll_number': roll_number, 'age': age, 'subjects': subjects}
        else:
            print("Student already in the system.")

    def roll_number_info(self, roll_number):
        if roll_number in self.database:
            print(self.database[roll_number])
        else:
            print("Student not found.")

    def update_subject(self, roll_number, new_subjects):
        if roll_number in self.database:
            self.database[roll_number]['subjects'] = new_subjects
            print(f"Changed subjects for {self.database[roll_number]['name']} student.")
        else:
            print(f"Student {roll_number} not found.")

    def remove_student(self, roll_number):
        if roll_number in self.database:
            del self.database[roll_number]
            print(f"Student with roll number {roll_number} removed successfully.")
        else:
            print(f"Student with roll number {roll_number} not found.")


student_database = Students()

while True:
    command = input().split(':')
    if command[0] == 'End':
        break

    action, roll_number = command[0], command[1]

    if action == "AddStudent":
        student_database.add_student(command[2], roll_number, command[3], command[4])
    elif action == "DisplayInfo":
        student_database.roll_number_info(roll_number)
    elif action == "Update":
        student_database.update_subject(roll_number, command[2])
    elif action == "Remove":
        student_database.remove_student(roll_number)
