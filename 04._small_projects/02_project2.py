# 2. Advanced: Student Marks Analyzer
# Uses: dict + tuple + while + conditions

# Problem
# Build a system where the user:
#  - Enters a student name
#  - System prints average mark
#  - If name does not exist, skip
#  - Stop when typing "stop"

# Store student data as:
students = {
    "Sita": (78, 88, 91),
    "Ram": (55, 60, 72),
    "Gita": (92, 83, 89)
}

while True:
    name = input("Enter the name of student or stop to exit:")

    if name.lower() == "stop":
        break
    if name not in students:
        print("Student not found")
        continue
    
    #get marks from tuple | unpack tuple
    marks = students[name]
    avg = sum(marks) / len(marks)

    print(f"Name: {name}")
    print(f"Marks: {marks}")
    print(f"Average: {avg}")
    print("-" * 30)

    