#write a program to develop complete mini project using arrays,strings and functionsstudents = []  # list of dicts: {roll, name, marks}
students=[]
def add_student():
    roll = int(input("Roll No: "))
    name = input("Name: ").strip().title()
    marks = float(input("Marks: "))
    students.append({"roll": roll, "name": name, "marks": marks})
    print("Student added.")

def display_all():
    if not students:
        print("No records found.")
        return
    print(f"\n{'Roll':<6}{'Name':<20}{'Marks':<6}")
    print("-" * 32)
    for s in students:
        print(f"{s['roll']:<6}{s['name']:<20}{s['marks']:<6}")

def search_student():
    key = input("Search by roll or name: ").strip()
    found = False
    for s in students:
        if key.isdigit() and s["roll"] == int(key):
            print(f"Found: {s['name']}, Marks: {s['marks']}")
            found = True
        elif key.lower() in s["name"].lower():
            print(f"Found: Roll {s['roll']}, {s['name']}, Marks: {s['marks']}")
            found = True
    if not found:
        print("No matching student.")

def update_marks():
    roll = int(input("Roll No to update: "))
    for s in students:
        if s["roll"] == roll:
            s["marks"] = float(input("New Marks: "))
            print("Updated.")
            return
    print("Student not found.")

def delete_student():
    roll = int(input("Roll No to delete: "))
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Deleted.")
            return
    print("Student not found.")

def sort_by_marks():
    students.sort(key=lambda s: s["marks"], reverse=True)
    print("Sorted by marks (highest first).")
    display_all()

def class_statistics():
    if not students:
        print("No records found.")
        return
    marks_list = [s["marks"] for s in students]
    avg = sum(marks_list) / len(marks_list)
    topper = max(students, key=lambda s: s["marks"])
    lowest = min(students, key=lambda s: s["marks"])
    print(f"Average Marks: {avg:.2f}")
    print(f"Topper: {topper['name']} ({topper['marks']})")
    print(f"Lowest: {lowest['name']} ({lowest['marks']})")

def save_to_file():
    with open("students.txt", "w") as f:
        for s in students:
            f.write(f"{s['roll']},{s['name']},{s['marks']}\n")
    print("Saved to students.txt")

def load_from_file():
    students.clear()
    try:
        with open("students.txt", "r") as f:
            for line in f:
                roll, name, marks = line.strip().split(",")
                students.append({"roll": int(roll), "name": name, "marks": float(marks)})
        print("Loaded from students.txt")
    except FileNotFoundError:
        print("No saved file found.")

def menu():
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. Display All")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Sort by Marks")
    print("7. Class Statistics")
    print("8. Save to File")
    print("9. Load from File")
    print("10. Exit")

def main():
    while True:
        menu()
        choice = input("Enter choice: ").strip()
        if choice == "1": add_student()
        elif choice == "2": display_all()
        elif choice == "3": search_student()
        elif choice == "4": update_marks()
        elif choice == "5": delete_student()
        elif choice == "6": sort_by_marks()
        elif choice == "7": class_statistics()
        elif choice == "8": save_to_file()
        elif choice == "9": load_from_file()
        elif choice == "10":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()