import json
import os
from tabulate import tabulate


def load_students():

    if os.path.exists("students.json"):

        with open("students.json", "r") as file:
            return json.load(file)

    return []


def save_students(students):

    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)


def add_student(students):

    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    student = {
        "Roll": roll,
        "Name": name,
        "Age": age,
        "Course": course
    }

    students.append(student)

    save_students(students)

    print("Student Added Successfully!")


def view_students(students):

    if len(students) == 0:

        print("No Student Records Found")

    else:

        print(tabulate(students,
                       headers="keys",
                       tablefmt="grid"))


def search_student(students):

    roll = input("Enter Roll Number to Search: ")

    for student in students:

        if student["Roll"] == roll:

            print(student)

            return

    print("Student Not Found")


def update_student(students):

    roll = input("Enter Roll Number to Update: ")

    for student in students:

        if student["Roll"] == roll:

            student["Name"] = input("Enter New Name: ")
            student["Age"] = input("Enter New Age: ")
            student["Course"] = input("Enter New Course: ")

            save_students(students)

            print("Student Updated Successfully!")

            return

    print("Student Not Found")


def delete_student(students):

    roll = input("Enter Roll Number to Delete: ")

    for student in students:

        if student["Roll"] == roll:

            students.remove(student)

            save_students(students)

            print("Student Deleted Successfully!")

            return

    print("Student Not Found")


def main():

    students = load_students()

    while True:

        print("\n===== STUDENT MANAGEMENT SYSTEM =====")

        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":

            add_student(students)

        elif choice == "2":

            view_students(students)

        elif choice == "3":

            search_student(students)

        elif choice == "4":

            update_student(students)

        elif choice == "5":

            delete_student(students)

        elif choice == "6":

            print("Thank You!")

            break

        else:

            print("Invalid Choice")


if __name__ == "__main__":

    main()