# =========================================================
# ICT105 - SESSION 7 & SESSION 8
# FUNCTIONS, TKINTER GUI, AND OOP
# =========================================================

# =========================================================
# SESSION 7 - WORKING WITH FUNCTIONS
# =========================================================

# ---------------------------------------------------------
# EXERCISE 1 - STUDENT REGISTRATION FUNCTION
# ---------------------------------------------------------

# Create a function to register a student into a course.
def course_enrollment(student_id, first_name, last_name,
                      course_id, course_name,
                      action="Echo"):

    # Print action type.
    print("Action:", action)

    # Print student details.
    print("Student ID:", student_id)
    print("Student Name:", first_name, last_name)

    # Print course details.
    print("Course ID:", course_id)
    print("Course Name:", course_name)

    # Print confirmation message.
    print(first_name, "has been enrolled successfully.")

    # Print blank line.
    print()


# Call function using positional arguments.
course_enrollment(
    1001,
    "Alice",
    "Smith",
    "CS101",
    "Introduction to Computer Science"
)

# Call function using keyword argument.
course_enrollment(
    1002,
    "Bob",
    "Johnson",
    "MATH101",
    "Calculus I",
    action="Add"
)

# Call function using Amend action.
course_enrollment(
    1003,
    "Charlie",
    "Brown",
    "PHY101",
    "General Physics I",
    action="Amend"
)

# Call function using Delete action.
course_enrollment(
    1004,
    "David",
    "Lee",
    "CHEM101",
    "General Chemistry I",
    action="Delete"
)


# ---------------------------------------------------------
# EXERCISE 2 - STUDENT COURSE LIST
# ---------------------------------------------------------

# Create function to collect courses from user.
def student_course_list(student_id, student_name):

    # Create empty list for courses.
    courses = []

    # Loop 4 times to collect 4 courses.
    for i in range(4):

        # Ask user for course ID.
        course = input("Enter Course " + str(i + 1) + ": ")

        # Add course into list.
        courses.append(course)

    # Ask for semester.
    semester = input("Enter Semester: ")

    # Ask for year.
    year = input("Enter Year: ")

    # Print student summary.
    print("\nSTUDENT COURSE SUMMARY")
    print("Student ID:", student_id)
    print("Student Name:", student_name)
    print("Courses:", courses)
    print("Semester:", semester)
    print("Year:", year)

    # Print blank line.
    print()


# Call the function.
# Uncomment to run.
# student_course_list(1001, "Alice Smith")


# ---------------------------------------------------------
# EXERCISE 2.2 - STORE COURSES IN DICTIONARY
# ---------------------------------------------------------

# Create function using keyword arguments.
def add_courses(**courses):

    # Print heading.
    print("COURSE DICTIONARY")

    # Loop through dictionary.
    for course_id, course_name in courses.items():

        # Print course details.
        print(course_id, ":", course_name)

    # Print blank line.
    print()


# Call the function.
add_courses(
    CS101="Introduction to Computer Science",
    MATH101="Calculus I",
    PHY101="General Physics I",
    CHEM101="General Chemistry I"
)


# =========================================================
# EXERCISE 3 - TKINTER CALCULATOR
# =========================================================

# Import tkinter library.
import tkinter as tk

# Create main window.
root = tk.Tk()

# Set window title.
root.title("Simple Calculator")

# Set window size.
root.geometry("300x300")


# ---------------------------------------------------------
# FUNCTION TO ADD NUMBERS
# ---------------------------------------------------------
def add():

    # Get numbers from entry boxes.
    num1 = float(entry1.get())
    num2 = float(entry2.get())

    # Calculate result.
    result = num1 + num2

    # Display result.
    result_label.config(text="Result: " + str(result))


# ---------------------------------------------------------
# FUNCTION TO SUBTRACT NUMBERS
# ---------------------------------------------------------
def subtract():

    # Get numbers from entry boxes.
    num1 = float(entry1.get())
    num2 = float(entry2.get())

    # Calculate result.
    result = num1 - num2

    # Display result.
    result_label.config(text="Result: " + str(result))


# ---------------------------------------------------------
# FUNCTION TO MULTIPLY NUMBERS
# ---------------------------------------------------------
def multiply():

    # Get numbers from entry boxes.
    num1 = float(entry1.get())
    num2 = float(entry2.get())

    # Calculate result.
    result = num1 * num2

    # Display result.
    result_label.config(text="Result: " + str(result))


# ---------------------------------------------------------
# FUNCTION TO DIVIDE NUMBERS
# ---------------------------------------------------------
def divide():

    # Get numbers from entry boxes.
    num1 = float(entry1.get())
    num2 = float(entry2.get())

    # Check division by zero.
    if num2 != 0:

        # Calculate result.
        result = num1 / num2

        # Display result.
        result_label.config(text="Result: " + str(result))

    else:

        # Display error message.
        result_label.config(text="Cannot divide by zero")


# Create label for first number.
label1 = tk.Label(root, text="Number 1")
label1.pack()

# Create entry box for first number.
entry1 = tk.Entry(root)
entry1.pack()

# Create label for second number.
label2 = tk.Label(root, text="Number 2")
label2.pack()

# Create entry box for second number.
entry2 = tk.Entry(root)
entry2.pack()

# Create Add button.
add_button = tk.Button(root, text="Add", command=add)
add_button.pack()

# Create Subtract button.
subtract_button = tk.Button(root, text="Subtract", command=subtract)
subtract_button.pack()

# Create Multiply button.
multiply_button = tk.Button(root, text="Multiply", command=multiply)
multiply_button.pack()

# Create Divide button.
divide_button = tk.Button(root, text="Divide", command=divide)
divide_button.pack()

# Create result label.
result_label = tk.Label(root, text="Result:")
result_label.pack()


# =========================================================
# SESSION 8 - OBJECT ORIENTED PROGRAMMING
# =========================================================

# ---------------------------------------------------------
# EXERCISE 1 - USER CLASS
# ---------------------------------------------------------

# Create User class.
class User:

    # Constructor method.
    def __init__(self, first_name, last_name,
                 email, username,
                 date_of_birth, location):

        # Store user details.
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.date_of_birth = date_of_birth
        self.location = location

        # Set login attempts to zero.
        self.login_attempts = 0

    # Method to display user details.
    def describe_user(self):

        print("USER DETAILS")
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Email:", self.email)
        print("Username:", self.username)
        print("Date of Birth:", self.date_of_birth)
        print("Location:", self.location)
        print()

    # Method to greet user.
    def greet_user(self):

        print("Welcome", self.first_name)
        print()

    # Method to increase login attempts.
    def increment_login_attempts(self):

        self.login_attempts += 1

    # Method to reset login attempts.
    def reset_login_attempts(self):

        self.login_attempts = 0


# Create user objects.
user1 = User(
    "Alice",
    "Smith",
    "alice@uni.edu.au",
    "alice123",
    "01/01/2000",
    "Perth"
)

user2 = User(
    "Bob",
    "Johnson",
    "bob@uni.edu.au",
    "bob123",
    "02/02/2001",
    "Sydney"
)

# Call methods.
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

# Test login attempts.
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

# Print login attempts.
print("Login Attempts:", user1.login_attempts)

# Reset login attempts.
user1.reset_login_attempts()

# Print login attempts again.
print("Login Attempts After Reset:", user1.login_attempts)

print()


# ---------------------------------------------------------
# EXERCISE 3 - CLASSROOM CLASS
# ---------------------------------------------------------

# Create Classroom class.
class Classroom:

    # Constructor method.
    def __init__(self, classroom_name,
                 classroom_location,
                 seats_in_class):

        # Store classroom details.
        self.classroom_name = classroom_name
        self.classroom_location = classroom_location
        self.seats_in_class = seats_in_class

        # Default students enrolled.
        self.students_enrolled = 0

        # Create audit log list.
        self.audit_log = []

    # Method to describe classroom.
    def describe_classroom(self):

        print("CLASSROOM DETAILS")
        print("Classroom Name:", self.classroom_name)
        print("Location:", self.classroom_location)
        print("Seats:", self.seats_in_class)
        print()

    # Method to check classroom size.
    def checksize_classroom(self):

        print("This classroom supports",
              self.seats_in_class,
              "students.")
        print()

    # Method to set enrolled students.
    def set_number_enrolled(self, number):

        self.students_enrolled = number

    # Method to update enrolled students.
    def update_number_enrolled(self, number):

        # Update student count.
        self.students_enrolled += number

        # Create audit message.
        log_message = str(number) + " students added."

        # Add log into audit list.
        self.audit_log.append(log_message)

    # Method to display audit log.
    def show_audit_log(self):

        print("AUDIT LOG")

        # Loop through log list.
        for log in self.audit_log:

            print(log)

        print()


# Create classroom objects.
classroom1 = Classroom(
    "ICT105 Lab",
    "Building A",
    30
)

classroom2 = Classroom(
    "Physics Lab",
    "Building B",
    40
)

classroom3 = Classroom(
    "Chemistry Lab",
    "Building C",
    25
)

# Print classroom details.
classroom1.describe_classroom()
classroom1.checksize_classroom()

classroom2.describe_classroom()
classroom3.describe_classroom()

# Print students enrolled.
print("Students Enrolled:",
      classroom1.students_enrolled)

# Change enrolled students.
classroom1.set_number_enrolled(20)

# Print updated value.
print("Updated Students Enrolled:",
      classroom1.students_enrolled)

# Update enrolled students.
classroom1.update_number_enrolled(5)
classroom1.update_number_enrolled(3)

# Print latest student count.
print("Final Students Enrolled:",
      classroom1.students_enrolled)

# Display audit log.
classroom1.show_audit_log()


# ---------------------------------------------------------
# EXERCISE 5 - EQUIPMENT CLASS
# ---------------------------------------------------------

# Create Equipment class inheriting Classroom.
class Equipment(Classroom):

    # Constructor method.
    def __init__(self, classroom_name,
                 classroom_location,
                 seats_in_class,
                 devices):

        # Inherit parent class constructor.
        super().__init__(
            classroom_name,
            classroom_location,
            seats_in_class
        )

        # Store device list.
        self.devices = devices

    # Method to display devices.
    def show_devices(self):

        print("CLASSROOM EQUIPMENT")

        # Loop through device list.
        for device in self.devices:

            print(device)

        print()


# Create Equipment object.
equipment_room = Equipment(
    "ICT105 Smart Classroom",
    "Building A",
    40,
    [
        "Interactive Whiteboard",
        "Desktop Computers",
        "Projector",
        "WiFi Access Point",
        "Sound System"
    ]
)

# Display classroom details.
equipment_room.describe_classroom()

# Display devices.
equipment_room.show_devices()


# =========================================================
# START TKINTER GUI
# =========================================================

# Start GUI application.
root.mainloop()