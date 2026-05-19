#Ict105- Worksheet 3
# Session 5 and session 6

# ------------------------------------------
#Session 5- Working with Dictionaries
# ------------------------------------------
# 1. Create a dictionary to store course information
course_enrollments = {
    1001: ["CS101", "MATH101"],
    1002: ["CS101", "MATH102"],
    1003: ["CS202", "PHY101"],
    1004: ["CS202", "CHEM101"],
    1005: ["BIO101", "HIST101"]
}

# Print heading.
print("STUDENT COURSE ENROLLMENTS\n")

# Loop through the dictionary and print student details.
for student_id, courses in course_enrollments.items():

    # Print the student ID.
    print("Student ID:", student_id)

    # Print the enrolled courses.
    print("Enrolled Courses:", courses)

    # Print a blank line for readability.
    print()


# ---------------------------------------------------------
# 2. Class Schedule
# ---------------------------------------------------------

# Create a dictionary to store department course information.
departments = {

    "Computer Science": [
        ("CS101", "Introduction to Computer Science"),
        ("CS202", "Data Structures and Algorithms")
    ],

    "Mathematics": [
        ("MATH101", "Calculus I"),
        ("MATH102", "Calculus II")
    ],

    "Physics": [
        ("PHY101", "General Physics I"),
        ("PHY102", "General Physics II")
    ]
}

# Print heading.
print("CLASS SCHEDULE\n")

# Loop through each department.
for department, courses in departments.items():

    # Print the department name.
    print("Department:", department)

    # Loop through each course tuple.
    for course in courses:

        # Print course ID and course name.
        print("Course ID:", course[0], "-", "Course Name:", course[1])

    # Print a blank line.
    print()


# ---------------------------------------------------------
# 3. Lecturer Assignments
# ---------------------------------------------------------

# Create a dictionary to store lecturer assignments.
lecturer_assignments = {

    "Dr. Emily Brown": ["CS101", "MATH102"],
    "Mr. Michael Johnson": ["CS202", "PHY102"],
    "Prof. David Lee": ["PHY101"],
    "Asst. Prof. Olivia Taylor": ["MATH101", "CHEM101"]

}

# Print heading.
print("LECTURER ASSIGNMENTS\n")

# Loop through the lecturer dictionary.
for lecturer, courses in lecturer_assignments.items():

    # Print lecturer name.
    print("Lecturer:", lecturer)

    # Print assigned courses.
    print("Assigned Courses:", courses)

    # Print blank line.
    print()


# =========================================================
# SESSION 5 - READING CSV FILE INTO DICTIONARY
# =========================================================

# Import pandas library.
import pandas as pd

# Read the CSV file.
# NOTE: Ensure students.csv exists in the same folder.
# Example CSV row:
# 1001,Alice,Smith,sd1001@uni123st.edu.au

# Uncomment the next line if using a real CSV file.
# df = pd.read_csv("students.csv", header=None)

# Create a sample dataframe manually.
data = [
    [1001, "Alice", "Smith", "sd1001@uni123st.edu.au"],
    [1002, "Bob", "Johnson", "sd1002@uni123st.edu.au"],
    [1003, "Charlie", "Brown", "sd1003@uni123st.edu.au"]
]

# Convert data into dataframe.
df = pd.DataFrame(data)

# Create an empty dictionary.
student_details = {}

# Loop through dataframe rows.
for index, row in df.iterrows():

    # Store each column value into variables.
    student_id = row[0]
    student_firstname = row[1]
    student_surname = row[2]
    student_email = row[3]

    # Add student data into dictionary.
    student_details[student_id] = [
        student_firstname,
        student_surname,
        student_email
    ]

# Print heading.
print("CSV DATA STORED IN DICTIONARY\n")

# Print the dictionary.
print(student_details)

# Print blank line.
print()


# =========================================================
# SESSION 6 - USER INPUT AND WHILE LOOPS
# =========================================================

# ---------------------------------------------------------
# 1. User Input Loop
# ---------------------------------------------------------

# Create an empty list for student names.
students = []

# Print heading.
print("USER INPUT LOOP\n")

# Start infinite loop.
while True:

    # Ask user to enter student name.
    name = input("Enter student name (Press Enter to stop): ")

    # Exit loop if user presses Enter.
    if name == "":
        break

    # Add student name into list.
    students.append(name)

    # Print confirmation message.
    print(name, "has been added to the class.\n")

# Print heading.
print("\nCLASS LIST")

# Loop through student list.
for student in students:

    # Print each student name.
    print(student)

# Print blank line.
print()


# ---------------------------------------------------------
# 2. Locate Rooms That Support Number of Users
# ---------------------------------------------------------

# Create dictionary for room details.
rooms = {

    101: [15, "Ground Floor", "Building A"],
    103: [20, "Ground Floor", "Building A"],
    105: [25, "Ground Floor", "Building A"],
    107: [30, "Ground Floor", "Building A"],
    206: [40, "1st Floor", "Building A"]

}

# Print heading.
print("ROOM LOCATION PROGRAM\n")

# Ask user for number of students.
student_count = int(input("Enter number of students: "))

# Loop through room dictionary.
for room, details in rooms.items():

    # Store room details into variables.
    capacity = details[0]
    floor = details[1]
    location = details[2]

    # Check if room capacity is enough.
    if capacity >= student_count:

        # Print suitable room details.
        print("\nSuitable Room Found")
        print("Room Number:", room)
        print("Capacity:", capacity)
        print("Floor:", floor)
        print("Location:", location)

        # Stop loop after finding room.
        break

# Print blank line.
print()


# ---------------------------------------------------------
# 3. Exit Program Loop Using Conditional Test
# ---------------------------------------------------------

# Create empty student list.
students = []

# Print heading.
print("EXIT PROGRAM LOOP\n")

# Start infinite loop.
while True:

    # Ask user for student name.
    name = input("Enter student name (quit, exit or 0 to stop): ")

    # Check exit conditions.
    if name.lower() == "quit" or name.lower() == "exit" or name == "0":

        # Print exit parameter.
        print("\nProgram exited using:", name)

        # Exit loop.
        break

    # Add student to list.
    students.append(name)

# Print heading.
print("\nSTUDENT LIST")

# Print all student names.
for student in students:

    print(student)

# Print total number of students.
print("Total Students:", len(students))

# Print blank line.
print()


# ---------------------------------------------------------
# 4. Active Variable Loop
# ---------------------------------------------------------

# Create empty student list.
students = []

# Create active variable.
active = True

# Print heading.
print("ACTIVE VARIABLE LOOP\n")

# Loop while active is True.
while active:

    # Ask user for name.
    name = input("Enter student name (type exit to stop): ")

    # Check if user wants to exit.
    if name.lower() == "exit":

        # Change active to False.
        active = False

    else:

        # Add name to list.
        students.append(name)

        # Print confirmation message.
        print(name, "added successfully.\n")

# Print heading.
print("\nFINAL STUDENT LIST")

# Print all students.
for student in students:

    print(student)

# Print blank line.
print()


# ---------------------------------------------------------
# 5. Break Statement Using Maximum Capacity
# ---------------------------------------------------------

# Create empty student list.
students = []

# Set maximum capacity.
max_cap = 3

# Print heading.
print("BREAK STATEMENT LOOP\n")

# Start infinite loop.
while True:

    # Ask user for student name.
    name = input("Enter student name: ")

    # Add name into list.
    students.append(name)

    # Check if maximum capacity reached.
    if len(students) >= max_cap:

        # Print message.
        print("\nMaximum capacity reached.")

        # Exit loop using break.
        break

# Print heading.
print("\nSTUDENTS IN CLASS")

# Print student names.
for student in students:

    print(student)

# Print maximum capacity.
print("Maximum Capacity:", max_cap)

# Print blank line.
print()


# ---------------------------------------------------------
# 6. Infinite Loop
# ---------------------------------------------------------

# Create counter variable.
count = 0

# Print heading.
print("INFINITE LOOP PROGRAM\n")

# Use try block to handle CTRL + C.
try:

    # Start infinite loop.
    while True:

        # Ask user for text input.
        text = input("Enter text: ")

        # Print user input.
        print(text)

        # Increase line counter.
        count += 1

# Catch keyboard interrupt exception.
except KeyboardInterrupt:

    # Print exit message.
    print("\nProgram stopped using CTRL + C")

    # Print total number of lines entered.
    print("Total Lines Entered:", count)       ]
