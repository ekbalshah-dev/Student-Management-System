students = {}
def add_student():
    roll_no = input("Enter roll number: ")
    name = input("Enter name: ")
    age = input("Enter age: ")
    course = input("Enter course: ") 
    students[roll_no] = {"name": name, "age": age, "course": course}
    print("Student added successfully!!")
def view_students():
    if students:
        print("List of students:")
        for roll, details in students.items():
            print(f"\nRoll No: {roll}\nName: {details['name']}\nAge: {details['age']}\nCourse: {details['course']}\n")
    else:
        print("No students found!!")
def search_student():
    if students:
       roll_no = input("Enter roll number to search: ")
       if roll_no in students:
          print("Student found!! Details are as follows:")
          for roll, details in students.items():
            if roll == roll_no:
                print(f"Roll No: {roll}\nName: {details['name']}\nAge: {details['age']}\nCourse: {details['course']}")
                break
       else:
        print("Student not found!!")
    else:        
        print("No students to search!!")
def update_student():
    if students:
       roll_no = input("Enter roll number to update: ")
       if roll_no in students:
        stu_name = input("Enter new name: ")
        stu_age = input("Enter new age: ")
        stu_course = input("Enter new course: ") 
        students[roll_no] = {"name": stu_name, "age": stu_age, "course": stu_course}
        print("Student details updated successfully!!")
       else:
        print("Student not found!!")
    else:
        print("No students to update!!")
def delete_student():
    if students:
       roll_no = input("Enter roll number to delete: ")
       if roll_no in students:
            del students[roll_no]
            print("Student deleted successfully!!")
       else:
            print("Student not found!!")
    else:
        print("No students to delete!!")
while True:
    print("\n********WElCOME TO YOUR STUDENT MANAGEMENT SYSTEM!!********")
    print("*******************************************************")
    print("Please select an option from the menu below:")
    print("\n1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        print("Thank you for using the Student Management System!")
        break
    else:
        print("Invalid choice!! Please try again.")