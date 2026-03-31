# q1.declare variable
a = 10
b = 5
#printing type of a and b
print("Type of a is:", type(a))
print("Type of b is:", type(b))

# q2. Arithemetic Operation
print("addition of a and b is:", a + b)
print("subration(a-b)=", a - b)
print("multiplication of a and b is:", a * b)
print("Divsion(a/b)=", a / b)

# q3. Using Variables and Type Casting
x = int( a/b ) #converting into interger
y = int( a*b )
print("value of x:", x) #output=2
print("value of y:", y) #output=50
print("type of x:", type(x)) #output=integer
print("type of y:", type(y)) #output=integer

# q4. Working with Strings:
result = "The result of a multiplied by b is:"
print(result + str(y)) #expected: The result of a multiplied by b is: 50

# q5. Using Comparison Operators:
print("Is a smaller that b?", a<b) #output: False
print("Is a greater that b?", a>b) #output: True