#write a program to create student record system using array and strings.
students = []

def add_student():
    roll = int(input("Roll No: "))
    name = input("Name: ")
    marks = float(input("Marks: "))
    students.append({"roll": roll, "name": name, "marks": marks})

def display_students():
    for s in students:
        print(f"{s['roll']}\t{s['name']}\t{s['marks']}")

def search_student():
    r = int(input("Enter roll to search: "))
    for s in students:
        if s["roll"] == r:
            print(f"Found: {s['name']}, Marks: {s['marks']}")
            return
    print("Not found.")

while True:
    print("\n1.Add 2.Display 3.Search 4.Exit")
    choice = int(input("Choice: "))
    if choice == 1: add_student()
    elif choice == 2: display_students()
    elif choice == 3: search_student()
    elif choice == 4: break