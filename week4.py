# ---------------------------------------------------
# ICT105 - Conditional Statements and Loops
# Chapter 5 Examples with Simple Single Line Comments
# ---------------------------------------------------

# ---------------------------------------------------
# SIMPLE IF STATEMENT
# ---------------------------------------------------

# Store a number in variable.
number = 10

# Check if number equals 10.
if number == 10:

    # Print message if condition is true.
    print("Number is equal to 10")

# Print statement outside if block.
print("After if code")

# ---------------------------------------------------
# IF ELSE STATEMENT
# ---------------------------------------------------

# Store another number.
number2 = 7

# Check if number is even.
if number2 % 2 == 0:

    # Execute if condition is true.
    print("\nEven number")

else:

    # Execute if condition is false.
    print("\nOdd number")

# Print statement after if else block.
print("After if else code")

# ---------------------------------------------------
# MULTIPLE ELIF BLOCKS
# ---------------------------------------------------

# Store age value.
age = 70

# Check first condition.
if age < 4:

    # Ticket price for children.
    price = 0

# Check second condition.
elif age < 18:

    # Ticket price for teenagers.
    price = 25

# Check third condition.
elif age < 65:

    # Ticket price for adults.
    price = 40

# Run if all conditions are false.
else:

    # Ticket price for seniors.
    price = 20

# Print ticket price.
print("\nTicket Price:", price)

# ---------------------------------------------------
# TESTING MULTIPLE CONDITIONS
# ---------------------------------------------------

# Create toppings list.
toppings = ["mushrooms", "extra cheese"]

# Check for mushrooms.
if "mushrooms" in toppings:

    # Print message.
    print("\nAdding mushrooms.")

# Check for extra cheese.
if "extra cheese" in toppings:

    # Print message.
    print("Adding extra cheese.")

# ---------------------------------------------------
# LOOPS WITH CONDITIONAL STATEMENTS
# ---------------------------------------------------

# Create toppings list.
pizza_toppings = ["mushrooms", "green peppers", "extra cheese"]

# Loop through toppings.
print("\nPizza Toppings:")

for topping in pizza_toppings:

    # Check for unavailable topping.
    if topping == "green peppers":

        # Print unavailable message.
        print("Sorry, we are out of green peppers right now.")

    else:

        # Print available topping.
        print(f"Adding {topping}.")

# Print completion message.
print("Finished making your pizza!")

# ---------------------------------------------------
# CHECKING FOR EMPTY LISTS
# ---------------------------------------------------

# Create empty list.
toppings_list = []

# Check if list contains items.
if toppings_list:

    # Loop through toppings.
    for topping in toppings_list:
        print(f"Adding {topping}.")

else:

    # Print message if list is empty.
    print("\nAre you sure you want a plain pizza?")

# ---------------------------------------------------
# VALIDATING INPUTS AGAINST A LIST
# ---------------------------------------------------

# Create available toppings list.
available_toppings = [
    "mushrooms",
    "olives",
    "green peppers",
    "extra cheese"
]

# Create requested toppings list.
requested_toppings = [
    "mushrooms",
    "french fries"
]

# Print heading.
print("\nChecking Requested Toppings:")

# Loop through requested toppings.
for topping in requested_toppings:

    # Check if topping is available.
    if topping in available_toppings:

        # Print confirmation message.
        print(f"Adding {topping}.")

    else:

        # Print unavailable message.
        print(f"Sorry, we don't have {topping}.")

# ---------------------------------------------------
# FOR LOOP EXAMPLE
# ---------------------------------------------------

# Create magician list.
magicians = ["alice", "david", "carolina"]

# Print heading.
print("\nMagician Show:")

# Loop through each magician.
for magician in magicians:

    # Print first message.
    print(f"{magician.title()}, that was a great trick!")

    # Print second message.
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

# Print final message after loop.
print("Thank you, everyone. That was a great magic show!")

# ---------------------------------------------------
# RANGE FUNCTION EXAMPLES
# ---------------------------------------------------

# Print heading.
print("\nRange Loop Example 1:")

# Loop from 1 to 4.
for value in range(1, 5):

    # Print value.
    print(value)

# Print heading.
print("\nRange Loop Example 2:")

# Loop from 2 to 5.
for i in range(2, 6):

    # Print number.
    print(i)

# ---------------------------------------------------
# LOOPING THROUGH A STRING
# ---------------------------------------------------

# Create string variable.
word = "Program"

# Print heading.
print("\nCharacters in Word:")

# Loop through each character.
for ch in word:

    # Print character.
    print(ch)

# ---------------------------------------------------
# WHILE LOOP EXAMPLE
# ---------------------------------------------------

# Set starting value.
count = 1

# Print heading.
print("\nWhile Loop Example:")

# Run loop while count is less than or equal to 5.
while count <= 5:

    # Print count value.
    print("Count:", count)

    # Increase count value.
    count += 1

# ---------------------------------------------------
# SIMPLE USER LOGIN CHECK
# ---------------------------------------------------

# Store username.
username = "admin"

# Store password.
password = "1234"

# Check username and password.
if username == "admin" and password == "1234":

    # Print success message.
    print("\nLogin successful.")

else:

    # Print failure message.
    print("\nInvalid username or password.")

# ---------------------------------------------------
# NESTED IF STATEMENT
# ---------------------------------------------------

# Store marks.
marks = 85

# Check passing marks.
if marks >= 50:

    # Check distinction marks.
    if marks >= 80:

        # Print distinction message.
        print("\nResult: Distinction")

    else:

        # Print pass message.
        print("\nResult: Pass")

else:

    # Print fail message.
    print("\nResult: Fail")

# ---------------------------------------------------
# PROGRAM END
# ---------------------------------------------------

# Print ending message.
print("\nProgram Finished Successfully.")