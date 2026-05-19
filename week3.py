# ---------------------------------------------
# ICT105 - Data Collections and Lists
# Lists, Loops, and Tuples Examples
# ---------------------------------------------

# ---------------------------------------------
# LIST EXAMPLES
# ---------------------------------------------

# Create a list of integers.
int_list = [1, 2, 3, 4, 5]

# Create a list of strings.
str_list = ["apple", "banana", "cherry"]

# Create a mixed data type list.
mixed_list = [1, "hello", 3.14, True]

# Print all lists.
print("Integer List:", int_list)
print("String List:", str_list)
print("Mixed List:", mixed_list)

# ---------------------------------------------
# ACCESSING LIST ELEMENTS
# ---------------------------------------------

# Access the first item in string list.
print("\nFirst fruit:", str_list[0])

# Access the second item in integer list.
print("Second number:", int_list[1])

# Access the last item using negative index.
print("Last mixed item:", mixed_list[-1])

# ---------------------------------------------
# MODIFYING LIST ELEMENTS
# ---------------------------------------------

# Change "cherry" to "orange".
str_list[2] = "orange"

# Print modified list.
print("\nModified String List:", str_list)

# ---------------------------------------------
# ADDING ELEMENTS TO A LIST
# ---------------------------------------------

# Create a new list.
numbers = [5, 10, 20, 35, 50]

# Print original list.
print("\nOriginal Numbers:", numbers)

# Insert 25 at index position 3.
numbers.insert(3, 25)

# Print list after insert.
print("After Insert:", numbers)

# Add 60 at the end of the list.
numbers.append(60)

# Print list after append.
print("After Append:", numbers)

# ---------------------------------------------
# REMOVING ELEMENTS FROM A LIST
# ---------------------------------------------

# Delete item at index 1.
del numbers[1]

# Print updated list.
print("\nAfter del:", numbers)

# Remove value 25 from list.
numbers.remove(25)

# Print updated list.
print("After remove:", numbers)

# Remove last item using pop().
last_item = numbers.pop()

# Print updated list.
print("After pop:", numbers)

# Print removed item.
print("Popped item:", last_item)

# ---------------------------------------------
# SORTING LISTS
# ---------------------------------------------

# Create a number list.
num = [15, 5, 30, 25, 10]

# Sort list permanently in ascending order.
num.sort()

# Print sorted list.
print("\nPermanent Ascending Sort:", num)

# Create another list.
num2 = [15, 5, 30, 25, 10]

# Sort list temporarily.
sorted_num = sorted(num2)

# Print temporary sorted list.
print("Temporary Ascending Sort:", sorted_num)

# Print original list.
print("Original List:", num2)

# ---------------------------------------------
# SORTING IN DESCENDING ORDER
# ---------------------------------------------

# Sort permanently in descending order.
num2.sort(reverse=True)

# Print descending sorted list.
print("\nPermanent Descending Sort:", num2)

# Temporary descending sort.
temp_desc = sorted(num2, reverse=True)

# Print temporary descending sorted list.
print("Temporary Descending Sort:", temp_desc)

# ---------------------------------------------
# REVERSING LIST ORDER
# ---------------------------------------------

# Create fruit list.
fruits = ["apple", "banana", "orange", "berry"]

# Reverse list order.
fruits.reverse()

# Print reversed list.
print("\nReversed List:", fruits)

# ---------------------------------------------
# AVOIDING INDEX ERRORS
# ---------------------------------------------

# Create a list of names.
names = ["John", "George", "Josh"]

# Use try-except to avoid program crash.
try:
    # Attempt to access invalid index.
    print(names[3])

# Handle index error.
except IndexError:
    print("\nError: List index out of range.")

# ---------------------------------------------
# FOR LOOP EXAMPLE
# ---------------------------------------------

# Create a magician list.
magicians = ["alice", "david", "carolina"]

# Loop through the list.
print("\nMagician Messages:")

for magician in magicians:

    # Print personalised message.
    print(f"{magician.title()}, that was a great trick!")

    # Print second message.
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

# Print message after loop finishes.
print("Thank you, everyone. That was a great magic show!")

# ---------------------------------------------
# RANGE FUNCTION EXAMPLES
# ---------------------------------------------

# Loop from 1 to 4.
print("\nRange Example 1:")

for value in range(1, 5):
    print(value)

# Loop from 2 to 5.
print("\nRange Example 2:")

for i in range(2, 6):
    print(i)

# ---------------------------------------------
# LOOPING THROUGH A STRING
# ---------------------------------------------

# Create a word variable.
word = "Program"

# Print each character in the word.
print("\nCharacters in Word:")

for ch in word:
    print(ch)

# ---------------------------------------------
# LOOPING THROUGH STRING USING INDEX
# ---------------------------------------------

# Create a string.
my_string = "Hello"

# Loop through string indexes.
print("\nString Index Example:")

for i in range(len(my_string)):

    # Print index and character.
    print(f"Index {i}: {my_string[i]}")

# ---------------------------------------------
# TUPLE EXAMPLES
# ---------------------------------------------

# Create a tuple.
my_tuple = (1, 2, 3)

# Print tuple.
print("\nTuple:", my_tuple)

# Access tuple element.
print("First Tuple Element:", my_tuple[0])

# Tuple unpacking.
a, b, c = my_tuple

# Print unpacked values.
print("Unpacked Values:", a, b, c)

# Create another tuple.
another_tuple = (4, 5)

# Concatenate tuples.
new_tuple = my_tuple + another_tuple

# Print concatenated tuple.
print("Concatenated Tuple:", new_tuple)

# Repeat tuple.
repeat_tuple = my_tuple * 3

# Print repeated tuple.
print("Repeated Tuple:", repeat_tuple)

# Loop through tuple.
print("\nLoop Through Tuple:")

for item in my_tuple:
    print(item)

# Slice tuple.
sub_tuple = new_tuple[1:4]

# Print sliced tuple.
print("\nSliced Tuple:", sub_tuple)

# ---------------------------------------------
# END OF PROGRAM
# ---------------------------------------------
print("\nProgram Finished Successfully.")