# =========================
# LISTS SECTION
# =========================

# Create different types of lists
int_list = [1, 2, 3, 4, 5]  # list of integers
str_list = ["apple", "banana", "cherry"]  # list of strings
mixed_list = [1, "hello", 3.14, True]  # mixed data types

# Access list elements using index
print(str_list[0])  # first element
print(int_list[1])  # second element
print(mixed_list[-1])  # last element

# Modify list element
str_list[2] = "orange"  # change cherry to orange
print(str_list)

# Add elements using insert and append
int_list.insert(2, 99)  # insert at index 2
int_list.append(100)  # add at end
print(int_list)

# Remove elements
del int_list[1]  # delete element at index 1
int_list.remove(99)  # remove value 99
last_value = int_list.pop()  # remove last item
print(int_list)
print(last_value)

# Sorting lists
num = [15, 5, 30, 25, 10]  # sample numbers

num.sort()  # permanent sort ascending
print(num)

sorted_num = sorted(num, reverse=True)  # temporary sort descending
print(sorted_num)

# Reverse list
str_list.reverse()  # reverse order
print(str_list)

# Loop through list
magicians = ["alice", "david", "carolina"]  # list of names

for magician in magicians:  # loop through each item
    print(magician)  # print each name

# Loop with extra message
for magician in magicians:
    print(magician.title(), "great trick")  # message per item

print("Show finished")  # runs after loop ends


# =========================
# CONDITIONAL STATEMENTS
# =========================

number = 10  # sample number

# if statement
if number > 5:
    print("Greater than 5")  # condition true

# if-else statement
if number % 2 == 0:
    print("Even number")  # even case
else:
    print("Odd number")  # odd case

# elif chain
age = 20  # sample age

if age < 13:
    print("Child")
elif age < 18:
    print("Teen")
else:
    print("Adult")

# multiple conditions in list
toppings = ["mushrooms", "cheese"]

if "mushrooms" in toppings:
    print("Add mushrooms")

if "cheese" in toppings:
    print("Add cheese")

# check empty list
items = []

if items:
    print("Processing items")
else:
    print("List is empty")


# =========================
# LOOPS WITH CONDITIONS
# =========================

available = ["mushrooms", "cheese", "olives"]
request = ["mushrooms", "chips"]

for item in request:
    if item in available:
        print("Adding", item)  # available item
    else:
        print("Not available:", item)  # unavailable item


# =========================
# DICTIONARIES SECTION
# =========================

# create dictionary
alien = {"color": "green", "points": 5}

# access values
print(alien["color"])

# add new key-value
alien["x_pos"] = 0
alien["y_pos"] = 25

# modify value
alien["color"] = "yellow"

# delete key-value
del alien["points"]

print(alien)

# dictionary get method
value = alien.get("speed", "Not defined")  # safe access
print(value)

# loop dictionary
fav_lang = {"jen": "python", "sarah": "c", "phil": "java"}

for name, lang in fav_lang.items():
    print(name, "knows", lang)

# loop keys sorted
for name in sorted(fav_lang.keys()):
    print("Thank you", name)

# loop values
for lang in fav_lang.values():
    print(lang)

# unique values using set
for lang in set(fav_lang.values()):
    print("Unique:", lang)


# =========================
# NESTED DICTIONARIES / LISTS
# =========================

# list of dictionaries
aliens = []

# create multiple aliens using loop
for i in range(5):
    aliens.append({"color": "green", "points": 5})

# modify first 2 aliens
for alien in aliens[:2]:
    alien["color"] = "yellow"
    alien["points"] = 10

# print aliens
for alien in aliens:
    print(alien)

# dictionary with list inside
pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "cheese"]
}

print("Pizza order:")
for topping in pizza["toppings"]:
    print(topping)

# nested dictionary
users = {
    "user1": {"first": "john", "last": "doe"},
    "user2": {"first": "jane", "last": "smith"}
}

for username, info in users.items():
    print(username, info["first"], info["last"])