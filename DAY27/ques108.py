#write a program to create marksheet generation system.
print("===== Marksheet Generation System =====")

roll_no = input("Enter Roll Number: ")
name = input("Enter Student Name: ")

maths = int(input("Enter Maths Marks: "))
physics = int(input("Enter Physics Marks: "))
chemistry = int(input("Enter Chemistry Marks: "))
english = int(input("Enter English Marks: "))
computer = int(input("Enter Computer Marks: "))

total = maths + physics + chemistry + english + computer
percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
else:
    grade = "D"

if (maths >= 33 and physics >= 33 and chemistry >= 33
        and english >= 33 and computer >= 33):
    result = "PASS"
else:
    result = "FAIL"

print("\n========== MARKSHEET ==========")
print("Roll Number :", roll_no)
print("Name        :", name)

print("\nMarks")
print("Maths       :", maths)
print("Physics     :", physics)
print("Chemistry   :", chemistry)
print("English     :", english)
print("Computer    :", computer)

print("\nTotal Marks :", total)
print("Percentage  :", percentage, "%")
print("Grade       :", grade)
print("Result      :", result)
print("==============================")