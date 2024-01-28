# Educational Institute Registration Form Management

class RegistrationSystem:
    def __init__(self):
        self.students = {}

    def display_menu(self):
        print("\n--- Registration System Menu ---")
        print("1. Register Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Exit")

    def register_student(self):
        print("\n--- Register Student ---")
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        course = input("Enter course: ")
        self.students[name] = {'Age': age, 'Course': course}
        print(f"\n{name} successfully registered!")

    def view_all_students(self):
        print("\n--- View All Students ---")
        if not self.students:
            print("No students registered yet.")
        else:
            for name, info in self.students.items():
                print(f"Name: {name}, Age: {info['Age']}, Course: {info['Course']}")

    def search_student(self):
        print("\n--- Search Student ---")
        name = input("Enter student name to search: ")
        if name in self.students:
            info = self.students[name]
            print(f"\nStudent found!\nName: {name}, Age: {info['Age']}, Course: {info['Course']}")
        else:
            print(f"\nStudent with name {name} not found.")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                self.register_student()
            elif choice == '2':
                self.view_all_students()
            elif choice == '3':
                self.search_student()
            elif choice == '4':
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    registration_system = RegistrationSystem()
    registration_system.run()
