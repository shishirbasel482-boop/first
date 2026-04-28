"""
# WAP to input user frist name and find its length.
name = input("Enter your name:")
length = len(name)
print(length)

# WAP to find the occurance of a character in a string.
string = "My name is a Shishir a Baasel."
occurance = string.count("a")
print(occurance)

# WAP to check number is even or odd.
num = int(input("Enter a number"))
if (num % 2 == 0):
    print(The number is even.)
else
    print(The number is odd.)

Int_list = [5, 10, 20, 25, 30]
print("Original list:", Int_list)
del my_list[1] # Deletes the element at index 1 (10)
print("After del:", Int_list) # Output: [5, 20, 25, 30]g
"""
message = input("Enter a message or quit to exit: ")

while message != 'quit':
    print(message)
    message = input("Enter another message or quit to exit: ")