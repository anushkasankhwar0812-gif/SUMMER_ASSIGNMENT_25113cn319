#write a program to create employee management system
employees = []

while True:
    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        department = input("Enter Department: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email Address: ")

        employee = {
            "ID": emp_id,
            "Name": name,
            "Department": department,
            "Phone": phone,
            "Email": email
        }

        employees.append(employee)
        print("Employee added successfully!")

    elif choice == 2:
        if len(employees) == 0:
            print("No employee records found.")
        else:
            print("\nEmployee Records:")
            for emp in employees:
                print("\n----------------------")
                print("Employee ID :", emp["ID"])
                print("Name        :", emp["Name"])
                print("Department  :", emp["Department"])
                print("Phone       :", emp["Phone"])
                print("Email       :", emp["Email"])

    elif choice == 3:
        search_id = input("Enter Employee ID to search: ")
        found = False

        for emp in employees:
            if emp["ID"] == search_id:
                print("\nEmployee Found")
                print("Employee ID :", emp["ID"])
                print("Name        :", emp["Name"])
                print("Department  :", emp["Department"])
                print("Phone       :", emp["Phone"])
                print("Email       :", emp["Email"])
                found = True
                break

        if not found:
            print("Employee not found.")

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")