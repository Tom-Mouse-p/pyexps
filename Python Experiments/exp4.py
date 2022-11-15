print("--Students Log--")
student_list = []
go_on = True

while go_on:
    choice = int(input("1: Add Student Record.\n2: Display Details Of Student 'Python'.\n3: Show All Students Details."
                       "\n4: Sort Students By Name.\n5: Exit\n > "))
    if choice == 1:
        students = int(input("Enter The Number Of Students, To Add Details Of\n > "))
        for student in range(students):
            roll_no, name = input(f"Enter Roll_No & Name Of Student {student + 1}\n > ").split(" ")
            marks = tuple(map(int, input("Enter Marks In 3 Subjects\n > ").strip().split(" ")))
            details = (roll_no, name, marks)
            student_list.append(details)
            print("Added Details.")
    elif choice == 2:
        found = False
        for student in student_list:
            if 'Python' in student:
                print(student[0], student[1])
                found = True
        if not found:
            print("Student 'Python' Not Found.")
    elif choice == 3:
        print(student_list)
    elif choice == 4:
        student_list.sort(key=lambda x: x[1])
        print(student_list)
    elif choice == 5:
        go_on = False
        print("Bye!")
    else:
        print("Wrong Option Selected.")
