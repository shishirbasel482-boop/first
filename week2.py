"""
# Week 2: Python Basics
# Syntax is clean and readable.
x = 5
if x < 10:
    print("x is less than 10")
else:
     print("x is 10 or more")

# Example of a simple if-else condition

x = 5  # Assign a value to x

# Check if x is less than 10
if x < 10:
    print("x is less than 10")
else:
    print("x is 10 or more") 

# Variables store data in memory

message = "Hello Python world!"  # String variable
number = 10                      # Integer variable

print(message)
print(number)

# Local variables exist only inside the function

def my_function():
    x = 10  # Local variable
    print("Inside function:", x)

my_function()

# print(x)  #This will cause an error because x is local

# Global variable (accessible everywhere)

x = 10

def my_function():
    global x  # Declare that we are using the global variable
    x += 5    # Modify global variable
    print("Inside function:", x)

my_function()

# Accessing modified global variable outside the function
print("Outside function:", x)

# Integer arithmetic

a = 5
b = 2

print(a + b)   # Addition → 7
print(a - b)   # Subtraction → 3
print(a * b)   # Multiplication → 10
print(a // b)  # Integer division → 2
print(a ** b)  # Exponent → 25

# Float (decimal numbers)

price = 23.56
tax_rate = 0.07

# Calculate total price
total_price = price + (price * tax_rate)
print("Total price:", total_price)

# Floating-point precision issue
print(0.1 + 0.2)  # Output: 0.30000000000000004

# Fix using round()
print(round(0.1 + 0.2, 2))  # Output: 0.3

# Demonstrating different operators

x = 5
y = 3
"""
# Arithmetic operators
print(x + y)  # Addition
print(x - y)  # Subtraction

# Assignment operators
x += 2  # Same as x = x + 2
print(x)

# Comparison operators
print(x > y)   # True or False
print(x == y)  # Equal check

# Logical operators
print(x > 0 and y > 0)  # Both conditions must be True
print(x > 0 or y < 0)   # At least one condition True
print(not(x > 0))       # Reverse condition