# ==========================================
# SESSION - LISTS, TUPLES, LOOPS, CONDITIONS
# Using ALL 15 courses
# ==========================================

# ------------------------------------------
# 1. Create list (NOT alphabetical)
# ------------------------------------------
courses = [
    "Physics I",
    "Introduction to Programming",
    "Calculus I",
    "Biology I",
    "History I",
    "Chemistry I",
    "Discrete Mathematics",
    "Psychology I",
    "English Composition I",
    "Microeconomics",
    "Linear Algebra",
    "Macroeconomics",
    "Calculus II",
    "Introduction to Philosophy",
    "Data Structures and Algorithms"
]

print("Original course list:")
print(courses)

# ------------------------------------------
# 2. sorted() (does NOT change original)
# ------------------------------------------
print("\nSorted list:")
print(sorted(courses))

print("\nReverse sorted list:")
print(sorted(courses, reverse=True))

# ------------------------------------------
# 3. reverse()
# ------------------------------------------
courses.reverse()
print("\nAfter reverse():")
print(courses)

courses.reverse()
print("\nAfter reversing again:")
print(courses)

# ------------------------------------------
# 4. sort()
# ------------------------------------------
courses.sort()
print("\nAfter sort():")
print(courses)

courses.sort(reverse=True)
print("\nAfter sort(reverse=True):")
print(courses)

# ------------------------------------------
# 5. Print available courses
# ------------------------------------------
print("\nThe following courses are available for expression of interest:")
for course in sorted(courses):
    print("-", course)

# ------------------------------------------
# 6. Replace a course
# ------------------------------------------
old_course = courses[0]
courses[0] = "Artificial Intelligence"

print(f"\nWithdrawn course: {old_course}")
print("New course added: Artificial Intelligence")

# ------------------------------------------
# 7. Add 3 more courses
# ------------------------------------------
courses.insert(0, "Cyber Security")
courses.insert(len(courses)//2, "Data Science")
courses.append("Machine Learning")

print("\nUpdated course list:")
for course in courses:
    print("-", course)

# ------------------------------------------
# 8. Remove 4 courses using pop()
# ------------------------------------------
print("\nCourses removed due to issues:")

removed1 = courses.pop()
removed2 = courses.pop()
removed3 = courses.pop()
removed4 = courses.pop()

print(removed1)
print(removed2)
print(removed3)
print(removed4)

print("\nRemaining courses:")
for course in courses:
    print("-", course)

# ------------------------------------------
# 9. Tuples and loops
# ------------------------------------------
course_tuples = [
    (1, "Introduction to Programming"),
    (2, "Calculus I"),
    (3, "Data Structures and Algorithms"),
    (4, "Linear Algebra"),
    (5, "Physics I"),
    (6, "Chemistry I"),
    (7, "Biology I"),
    (8, "Microeconomics"),
    (9, "Macroeconomics"),
    (10, "Psychology I"),
    (11, "History I"),
    (12, "English Composition I"),
    (13, "Introduction to Philosophy"),
    (14, "Calculus II"),
    (15, "Discrete Mathematics")
]

course_names = []

for cid, cname in course_tuples:
    course_names.append(cname)

print("\nCourse names extracted:")
print(course_names)

# ------------------------------------------
# 10. Course ID → Department search
# ------------------------------------------
departments = [
    [1, "Computer Science"],
    [2, "Mathematics"],
    [3, "Computer Science"],
    [4, "Mathematics"],
    [5, "Physics"],
    [6, "Chemistry"],
    [7, "Biology"],
    [8, "Economics"],
    [9, "Economics"],
    [10, "Psychology"],
    [11, "History"],
    [12, "English"],
    [13, "Philosophy"],
    [14, "Mathematics"],
    [15, "Computer Science"]
]

print("\nCourse Department Search")

while True:
    user_input = input("Enter course ID (1-15) or 0/quit: ")

    if user_input == "quit" or user_input == "0":
        print("Exited program.")
        break

    if not user_input.isdigit():
        print("Invalid input.")
        continue

    course_id = int(user_input)

    if 1 <= course_id <= 15:
        found = False
        for item in departments:
            if item[0] == course_id:
                print(f"Course ID {course_id} is in the {item[1]} department.")
                found = True
                break
        if not found:
            print("Course not found.")
    else:
        print("Course ID is out of range (1-15).")

# ------------------------------------------
# 11. Course Information Retrieval System
# ------------------------------------------
course_info = [
    [1, "Introduction to Programming", "Computer Science", "None"],
    [2, "Calculus I", "Mathematics", "None"],
    [3, "Data Structures and Algorithms", "Computer Science", "Intro to Programming"],
    [4, "Linear Algebra", "Mathematics", "None"],
    [5, "Physics I", "Physics", "None"],
    [6, "Chemistry I", "Chemistry", "None"],
    [7, "Biology I", "Biology", "None"],
    [8, "Microeconomics", "Economics", "None"],
    [9, "Macroeconomics", "Economics", "Microeconomics"],
    [10, "Psychology I", "Psychology", "None"],
    [11, "History I", "History", "None"],
    [12, "English Composition I", "English", "None"],
    [13, "Introduction to Philosophy", "Philosophy", "None"],
    [14, "Calculus II", "Mathematics", "Calculus I"],
    [15, "Discrete Mathematics", "Computer Science", "Intro to Programming"]
]

search_id = int(input("\nEnter course ID to get details: "))

found = False

for course in course_info:
    if course[0] == search_id:
        print("\nCourse Found:")
        print("Name:", course[1])
        print("Department:", course[2])
        print("Prerequisite:", course[3])
        found = True
        break

if not found:
    print("Course ID not found.")