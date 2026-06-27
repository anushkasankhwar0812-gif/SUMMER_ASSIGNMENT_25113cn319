#write a program to create salary management system

employees = []

while True:
    print("\n===== Salary Management System =====")
    print("1. Add Employee Salary")
    print("2. View Salary Records")
    print("3. Search Employee")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        basic_salary = float(input("Enter Basic Salary: "))

        hra = basic_salary * 0.20
        da = basic_salary * 0.10
        net_salary = basic_salary + hra + da

        employee = {
            "ID": emp_id,
            "Name": name,
            "Basic Salary": basic_salary,
            "HRA": hra,
            "DA": da,
            "Net Salary": net_salary
        }

        employees.append(employee)
        print("Salary record added successfully!")

    elif choice == 2:
        if len(employees) == 0:
            print("No records found.")
        else:
            for emp in employees:
                print("\n----------------------")
                print("Employee ID :", emp["ID"])
                print("Name        :", emp["Name"])
                print("Basic Salary:", emp["Basic Salary"])
                print("HRA         :", emp["HRA"])
                print("DA          :", emp["DA"])
                print("Net Salary  :", emp["Net Salary"])

    elif choice == 3:
        search_id = input("Enter Employee ID: ")
        found = False

        for emp in employees:
            if emp["ID"] == search_id:
                print("\nEmployee Found")
                print("Name        :", emp["Name"])
                print("Basic Salary:", emp["Basic Salary"])
                print("HRA         :", emp["HRA"])
                print("DA          :", emp["DA"])
                print("Net Salary  :", emp["Net Salary"])
                found = True
                break

        if not found:
            print("Employee not found.")

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice.")