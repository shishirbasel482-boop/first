# =========================================================
# ICT105 - FILES, EXCEPTIONS, JSON & REFACTORING
# =========================================================

# Import pathlib for file handling.
from pathlib import Path

# Import json module for JSON data storage.
import json


# =========================================================
# 1. READING FROM A FILE
# =========================================================

# Create a Path object for pi_digits.txt file.
path = Path("pi_digits.txt")

# Write sample data into the file.
path.write_text("3.1415926535\n8979323846\n2643383279")

# Read the entire file contents.
contents = path.read_text()

# Print the file contents.
print("READING FROM FILE")
print(contents)

# Print blank line.
print()


# =========================================================
# 2. REMOVE EXTRA BLANK SPACES USING rstrip()
# =========================================================

# Read file contents and remove extra spaces/newlines.
contents = path.read_text().rstrip()

# Print cleaned contents.
print("REMOVE EXTRA SPACES")
print(contents)

# Print blank line.
print()


# =========================================================
# 3. RELATIVE AND ABSOLUTE FILE PATHS
# =========================================================

# Create a relative file path.
relative_path = Path("files/filename.txt")

# Create an absolute file path.
absolute_path = Path("C:/Users/data/files/filename.txt")

# Print paths.
print("FILE PATHS")
print("Relative Path:", relative_path)
print("Absolute Path:", absolute_path)

# Print blank line.
print()


# =========================================================
# 4. ACCESSING FILE LINES
# =========================================================

# Create greetings file.
greeting_path = Path("greetings.txt")

# Write sample greetings into the file.
greeting_path.write_text("Hello!\nHow are you?\nWelcome to Python!")

# Read the entire file.
contents = greeting_path.read_text()

# Split contents into lines.
lines = contents.splitlines()

# Print heading.
print("ACCESSING FILE LINES")

# Loop through each line.
for line in lines:

    # Print each line.
    print(line)

# Print blank line.
print()


# =========================================================
# 5. WORKING WITH FILE CONTENTS
# =========================================================

# Create marks file.
marks_path = Path("marks.txt")

# Write marks into file.
marks_path.write_text("56\n78")

# Read marks line by line.
numbers = marks_path.read_text().splitlines()

# Create total variable.
total = 0

# Loop through numbers.
for num in numbers:

    # Convert string into integer.
    num = int(num)

    # Add numbers into total.
    total = total + num

# Print total marks.
print("TOTAL MARKS")
print(total)

# Print blank line.
print()


# =========================================================
# 6. LARGE FILES - PI DIGITS
# =========================================================

# Create large pi file.
large_pi_path = Path("pi_million_digits.txt")

# Write sample pi digits.
large_pi_path.write_text(
    "3.1415926535\n"
    "8979323846\n"
    "2643383279\n"
)

# Read file contents.
contents = large_pi_path.read_text()

# Split contents into lines.
lines = contents.splitlines()

# Create empty string.
pi_string = ""

# Loop through each line.
for line in lines:

    # Add stripped line into pi string.
    pi_string += line.lstrip()

# Print first 50 characters.
print("PI STRING")
print(pi_string[:50])

# Print total length.
print("TOTAL LENGTH")
print(len(pi_string))

# Print blank line.
print()


# =========================================================
# 7. WRITING TO A FILE
# =========================================================

# Create Path object.
programming_path = Path("programming.txt")

# Write one line into file.
programming_path.write_text("I love programming.")

# Read and print file contents.
print("WRITING TO FILE")
print(programming_path.read_text())

# Print blank line.
print()


# =========================================================
# 8. WRITING MULTIPLE LINES
# =========================================================

# Create multiple line contents.
contents = "I love programming.\n"
contents += "I love creating games.\n"
contents += "I also love data science.\n"

# Write multiple lines into file.
programming_path.write_text(contents)

# Print file contents.
print("WRITING MULTIPLE LINES")
print(programming_path.read_text())

# Print blank line.
print()


# =========================================================
# 9. ZERO DIVISION ERROR
# =========================================================

# Print heading.
print("ZERO DIVISION ERROR")

# Use try block.
try:

    # Attempt division by zero.
    print(5 / 0)

# Catch division error.
except ZeroDivisionError:

    # Print error message.
    print("You cannot divide by zero!")

# Print blank line.
print()


# =========================================================
# 10. USING try-except BLOCK
# =========================================================

# Print heading.
print("TRY-EXCEPT EXAMPLE")

# Use try block.
try:

    # Perform division.
    result = 10 / 2

# Catch division error.
except ZeroDivisionError:

    # Print error message.
    print("Division error occurred.")

# Else block runs if no error occurs.
else:

    # Print result.
    print("Answer:", result)

# Print blank line.
print()


# =========================================================
# 11. USER INPUT DIVISION PROGRAM
# =========================================================

# Print heading.
print("DIVISION PROGRAM")

# Create sample values.
first_number = "20"
second_number = "5"

# Use try block.
try:

    # Convert values and divide.
    answer = int(first_number) / int(second_number)

# Catch divide by zero error.
except ZeroDivisionError:

    # Print error message.
    print("You cannot divide by zero.")

# Else block runs if successful.
else:

    # Print answer.
    print("Division Answer:", answer)

# Print blank line.
print()


# =========================================================
# 12. FILE NOT FOUND ERROR
# =========================================================

# Create path for missing file.
missing_path = Path("alice.txt")

# Print heading.
print("FILE NOT FOUND EXAMPLE")

# Use try block.
try:

    # Attempt to read file.
    contents = missing_path.read_text()

# Catch missing file error.
except FileNotFoundError:

    # Print error message.
    print("Sorry, the file does not exist.")

# Print blank line.
print()


# =========================================================
# 13. ANALYZING TEXT FILE
# =========================================================

# Create sample text file.
sample_path = Path("sample_text.txt")

# Write sample paragraph.
sample_path.write_text(
    "Python is easy to learn. "
    "Python is powerful. "
    "Python is popular."
)

# Print heading.
print("ANALYZING TEXT")

# Use try block.
try:

    # Read file contents.
    contents = sample_path.read_text()

# Catch missing file error.
except FileNotFoundError:

    # Print error message.
    print("File not found.")

# Else block runs if file exists.
else:

    # Split text into words.
    words = contents.split()

    # Count total words.
    num_words = len(words)

    # Print total words.
    print("Total Words:", num_words)

# Print blank line.
print()


# =========================================================
# 14. WORKING WITH MULTIPLE FILES
# =========================================================

# Create function to count words.
def count_words(path):

    # Use try block.
    try:

        # Read file contents.
        contents = path.read_text()

    # Catch missing file error.
    except FileNotFoundError:

        # Print error message.
        print("Missing File:", path)

    # Else block runs if successful.
    else:

        # Split contents into words.
        words = contents.split()

        # Count words.
        num_words = len(words)

        # Print result.
        print(path, "has", num_words, "words.")


# Create sample files.
Path("file1.txt").write_text("Hello Python")
Path("file2.txt").write_text("Python programming is fun")

# Create file list.
filenames = ["file1.txt", "file2.txt", "missing.txt"]

# Loop through files.
for filename in filenames:

    # Create Path object.
    path = Path(filename)

    # Call function.
    count_words(path)

# Print blank line.
print()


# =========================================================
# 15. FAILING SILENTLY
# =========================================================

# Create function.
def silent_count_words(path):

    # Use try block.
    try:

        # Read file contents.
        contents = path.read_text()

    # Ignore missing file error.
    except FileNotFoundError:

        # Do nothing.
        pass

    # Else block.
    else:

        # Split contents into words.
        words = contents.split()

        # Count words.
        num_words = len(words)

        # Print word count.
        print(path, "contains", num_words, "words.")


# Call function.
silent_count_words(Path("file1.txt"))
silent_count_words(Path("unknown.txt"))

# Print blank line.
print()


# =========================================================
# 16. JSON - WRITING DATA
# =========================================================

# Create list of numbers.
numbers = [2, 3, 5, 7, 11, 13]

# Create JSON file path.
json_path = Path("numbers.json")

# Convert list into JSON format.
contents = json.dumps(numbers)

# Write JSON data into file.
json_path.write_text(contents)

# Print heading.
print("JSON DATA WRITTEN")

# Print JSON text.
print(contents)

# Print blank line.
print()


# =========================================================
# 17. JSON - READING DATA
# =========================================================

# Read JSON file contents.
contents = json_path.read_text()

# Convert JSON back into Python list.
numbers = json.loads(contents)

# Print numbers.
print("JSON DATA READ")
print(numbers)

# Print blank line.
print()


# =========================================================
# 18. SAVING USER DATA
# =========================================================

# Create username variable.
username = "Eric"

# Create username file path.
username_path = Path("username.json")

# Convert username into JSON.
contents = json.dumps(username)

# Write username into file.
username_path.write_text(contents)

# Read username from file.
contents = username_path.read_text()

# Convert JSON into Python string.
username = json.loads(contents)

# Print welcome message.
print("WELCOME USER")
print("Welcome back,", username)

# Print blank line.
print()


# =========================================================
# 19. CHECKING IF FILE EXISTS
# =========================================================

# Print heading.
print("CHECK EXISTING USER")

# Check if file exists.
if username_path.exists():

    # Read file contents.
    contents = username_path.read_text()

    # Load username.
    username = json.loads(contents)

    # Print message.
    print("Welcome back,", username)

# Else block runs if file missing.
else:

    # Create new username.
    username = "NewUser"

    # Convert to JSON.
    contents = json.dumps(username)

    # Save into file.
    username_path.write_text(contents)

    # Print message.
    print("We will remember you next time.")

# Print blank line.
print()


# =========================================================
# 20. REFACTORING PROGRAM
# =========================================================

# Function to get stored username.
def get_stored_username(path):

    # Check if file exists.
    if path.exists():

        # Read contents.
        contents = path.read_text()

        # Convert JSON into Python string.
        username = json.loads(contents)

        # Return username.
        return username

    # Return None if file missing.
    else:

        return None


# Function to create new username.
def get_new_username(path):

    # Create new username.
    username = "StudentUser"

    # Convert username into JSON.
    contents = json.dumps(username)

    # Save username into file.
    path.write_text(contents)

    # Return username.
    return username


# Function to greet user.
def greet_user():

    # Create file path.
    path = Path("username.json")

    # Get stored username.
    username = get_stored_username(path)

    # Check if username exists.
    if username:

        # Print welcome back message.
        print("Welcome back,", username)

    # Else create new user.
    else:

        # Create new username.
        username = get_new_username(path)

        # Print new user message.
        print("We will remember you,", username)


# Print heading.
print("REFACTORING PROGRAM")

# Call greet function.
greet_user()

# Print blank line.
print()


# =========================================================
# END OF PROGRAM
# =========================================================

print("PROGRAM FINISHED SUCCESSFULLY")