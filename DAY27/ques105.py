#write a program to create student record management system.
students = []

while True:
    print("\n----- Student Record Management System -----")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        roll = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        father = input("Enter Father's Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email Address: ")

        student = {
            "Roll No": roll,
            "Name": name,
            "Father Name": father,
            "Phone": phone,
            "Email": email
        }

        students.append(student)
        print("Student record added successfully!")

    elif choice == 2:
        if len(students) == 0:
            print("No records found.")
        else:
            print("\nStudent Records:")
            for s in students:
                print("\n------------------------")
                print("Roll No      :", s["Roll No"])
                print("Name         :", s["Name"])
                print("Father Name  :", s["Father Name"])
                print("Phone Number :", s["Phone"])
                print("Email        :", s["Email"])

    elif choice == 3:
        search_roll = input("Enter Roll Number to search: ")
        found = False

        for s in students:
            if s["Roll No"] == search_roll:
                print("\nStudent Found")
                print("Roll No      :", s["Roll No"])
                print("Name         :", s["Name"])
                print("Father Name  :", s["Father Name"])
                print("Phone Number :", s["Phone"])
                print("Email        :", s["Email"])
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice.")