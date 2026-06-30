#write a program to create mini employee management system.
employees = []

def add_employee():
    emp_id = int(input("Emp ID: "))
    name = input("Name: ")
    dept = input("Department: ")
    salary = float(input("Salary: "))
    employees.append({"id": emp_id, "name": name, "dept": dept, "salary": salary})

def display_employees():
    for e in employees:
        print(f"{e['id']}\t{e['name']}\t{e['dept']}\t{e['salary']}")

def update_salary():
    emp_id = int(input("Emp ID: "))
    new_salary = float(input("New Salary: "))
    for e in employees:
        if e["id"] == emp_id:
            e["salary"] = new_salary
            print("Updated.")
            return
    print("Employee not found.")

def delete_employee():
    emp_id = int(input("Emp ID to delete: "))
    for e in employees:
        if e["id"] == emp_id:
            employees.remove(e)
            print("Deleted.")
            return
    print("Employee not found.")

while True:
    print("\n1.Add 2.Display 3.Update Salary 4.Delete 5.Exit")
    choice = int(input("Choice: "))
    if choice == 1: add_employee()
    elif choice == 2: display_employees()
    elif choice == 3: update_salary()
    elif choice == 4: delete_employee()
    elif choice == 5: break