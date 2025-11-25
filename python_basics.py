"""
Python Basics - A Simple Introduction to Python Syntax
"""

# 1. Variables and Data Types
print("=== Variables and Data Types ===")
name = "Python"
version = 3.12
is_awesome = True
my_list = [1, 2, 3, 4, 5]
my_dict = {"language": "Python", "year": 1991}

print(f"Language: {name}")
print(f"Version: {version}")
print(f"Is awesome: {is_awesome}")
print(f"List: {my_list}")
print(f"Dictionary: {my_dict}")

# 2. Conditional Statements
print("\n=== Conditional Statements ===")
age = 25
if age >= 18:
    print("You are an adult")
elif age >= 13:
    print("You are a teenager")
else:
    print("You are a child")

# 3. Loops
print("\n=== Loops ===")
# For loop
print("For loop:")
for i in range(5):
    print(f"  Count: {i}")

# While loop
print("While loop:")
counter = 0
while counter < 3:
    print(f"  Counter: {counter}")
    counter += 1

# 4. Functions
print("\n=== Functions ===")
def greet(name):
    """A simple greeting function"""
    return f"Hello, {name}!"

def add(a, b):
    """Add two numbers"""
    return a + b

print(greet("World"))
print(f"5 + 3 = {add(5, 3)}")

# 5. List Comprehension
print("\n=== List Comprehension ===")
squares = [x**2 for x in range(10)]
print(f"Squares: {squares}")

# 6. Classes
print("\n=== Classes ===")
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

    def get_info(self):
        return f"{self.name} is {self.age} years old"

my_dog = Dog("Buddy", 3)
print(my_dog.bark())
print(my_dog.get_info())

# 7. Exception Handling
print("\n=== Exception Handling ===")
try:
    result = 10 / 2
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Execution completed")

print("\n=== End of Python Basics ===")
