"""
VARIABLES IN PYTHON
Key Concepts:
1. Variables are dynamic - no type declaration needed
2. Can reassign with different data types
3. Variables are references to objects in memory
4. Scope rules: LEGB (Local, Enclosing, Global, Built-in)
"""

# BASIC VARIABLE ASSIGNMENT & REASSIGNMENT

# Assigning a value to a variable
score = 12
print(score)  # Output: 12

# Reassigning a new value (same or different type)
score = 13    # Same type (int)
print(score)  # Output: 13

# Python is dynamically typed - can change type anytime
score = "High"  # Now it's a string!
print(score)    # Output: High


# DYNAMIC TYPING DEMONSTRATION

# Same variable can hold different data types
data = 42                 # Integer
print(f"Value: {data}, Type: {type(data)}")  # <class 'int'>

data = 3.14              # Float
print(f"Value: {data}, Type: {type(data)}")  # <class 'float'>

data = "Hello"           # String
print(f"Value: {data}, Type: {type(data)}")  # <class 'str'>

data = [1, 2, 3]         # List
print(f"Value: {data}, Type: {type(data)}")  # <class 'list'>

data = {"name": "John"}  # Dictionary
print(f"Value: {data}, Type: {type(data)}")  # <class 'dict'>


# MULTIPLE ASSIGNMENTS

# Assign multiple variables in one line
x, y, z = 1, 2, 3
print(f"x={x}, y={y}, z={z}")  # Output: 1 2 3

# Assign same value to multiple variables
a = b = c = 100
print(f"a={a}, b={b}, c={c}")  # Output: 100 100 100

# Unpacking sequences (lists, tuples, etc.)
colors = ["red", "green", "blue"]
r, g, b = colors  # Unpack the list into variables
print(f"r={r}, g={g}, b={b}")  # Output: red green blue

# Mixed data types in multiple assignment
name, age, cgpa = 'Nazim', 23, 3.99
print(f"Name: {name} (Type: {type(name)})")
print(f"Age: {age} (Type: {type(age)})")
print(f"CGPA: {cgpa} (Type: {type(cgpa)})")


# VARIABLE SWAPPING (Elegant Python way)

# Traditional method (like other languages)
a = 10
b = 20
temp = a     # Store a in temp
a = b        # a becomes 20
b = temp     # b becomes 10
print(f"Traditional: a={a}, b={b}")  # Output: 20 10

# Python's elegant method
a, b = b, a  # Simultaneous swap
print(f"Python way: a={a}, b={b}")   # Output: 10 20

# Swapping multiple variables
x, y, z = 1, 2, 3
print(f"Before swap: x={x}, y={y}, z={z}")  # 1 2 3
x, y, z = z, x, y  # Rotate values
print(f"After swap: x={x}, y={y}, z={z}")   # 3 1 2


# CONSTANTS (By Convention Only)

# Python doesn't have true constants, but we use UPPERCASE
PI = 3.14159
MAX_CONNECTIONS = 100
API_BASE_URL = "https://api.example.com"
DEFAULT_TIMEOUT = 30

# These CAN be changed, but we shouldn't (convention)
PI = 3.14  # Python allows this, but violates convention
print(f"Pi changed to: {PI}")


# VARIABLES AS OBJECT REFERENCES

# Variables reference objects in memory
x = 10
y = x  # y references the same object as x
print(f"x id: {id(x)}, y id: {id(y)}")  # Same memory address

# Immutable objects (int, str, tuple) - create new objects
x = 10
y = x
x = 20  # Creates a new integer object
print(f"x={x}, y={y}")  # y remains 10 (unchanged)

# Mutable objects (list, dict, set) - can modify in-place
list1 = [1, 2, 3]
list2 = list1  # list2 references the SAME list
list1.append(4)
print(f"list1: {list1}")  # [1, 2, 3, 4]
print(f"list2: {list2}")  # [1, 2, 3, 4] (changed!)


# SHALLOW COPY VS DEEP COPY

# Shallow copy - only copies top level
original = [1, 2, [3, 4]]
shallow_copy = original.copy()
shallow_copy[2][0] = 99  # Modify nested list
print(f"Original: {original}")     # [1, 2, [99, 4]] - changed!
print(f"Shallow: {shallow_copy}")  # [1, 2, [99, 4]] - changed!

# Deep copy - creates completely independent copy
import copy
deep_copy = copy.deepcopy(original)
deep_copy[2][0] = 100
print(f"Original: {original}")  # [1, 2, [99, 4]] - unchanged
print(f"Deep: {deep_copy}")     # [1, 2, [100, 4]] - changed


# VARIABLE SCOPE - GLOBAL, LOCAL, ENCLOSING

# Global variable (accessible everywhere)
global_var = "I'm global"

def my_function():
    """Demonstrating local variable scope"""
    # Local variable (only accessible inside function)
    local_var = "I'm local"
    print(global_var)  # Can access global
    print(local_var)   # Can access local
    # print(non_existent)  # This would cause error

my_function()

def modify_global():
    """Need 'global' keyword to modify global variable"""
    global global_var  # Tell Python we're using the global variable
    global_var = "Modified!"
    print(f"Inside function: {global_var}")

modify_global()
print(f"Outside function: {global_var}")  # Output: Modified!


# NESTED FUNCTIONS AND NONLOCAL

def outer():
    """Demonstrating enclosing scope with nonlocal"""
    x = "outer"  # Enclosing variable
    
    def inner():
        nonlocal x  # Access and modify outer's x
        x = "inner"  # Modify the enclosing variable
        print(f"Inner: {x}")  # Output: inner
    
    inner()
    print(f"Outer after inner: {x}")  # Output: inner (modified)

outer()


# 10. LEGB RULE - Scope Resolution Order

x = "global"  # GLOBAL scope

def outer():
    x = "outer enclosing"  # ENCLOSING scope
    
    def inner():
        x = "local"  # LOCAL scope (highest priority)
        print(f"Inner: {x}")  # Output: local
    
    inner()
    print(f"Outer: {x}")  # Output: outer enclosing

outer()
print(f"Global: {x}")  # Output: global


# DELETING VARIABLES
# Delete a single variable
x = 10
print(f"Before delete: x={x}")
del x  # Remove x from memory
# print(x)  # NameError: name 'x' is not defined

# Delete multiple variables
a, b, c = 1, 2, 3
del a, b, c  # Delete all three
# print(a)  # NameError


# TYPE HINTS (Type Annotations) - Python 3.5+

# Type hints for variables (not enforced, just documentation)
name: str = "Python"
age: int = 30
scores: list[int] = [85, 90, 78]
person: dict[str, any] = {"name": "John", "age": 25}

# Function with type hints
def greet(name: str) -> str:
    """Return a greeting message"""
    return f"Hello, {name}"

def calculate(a: int, b: int) -> int:
    """Return sum of two numbers"""
    return a + b

# Type hints don't prevent different types
scores = [85, "90", 78]  # This is allowed despite type hint
print(f"Scores: {scores}")  # Works fine



# PRACTICAL EXAMPLES

# Example: User input handling
def get_user_info():
    """Collect user information with proper type conversion"""
    name = input("Enter your name: ")
    age_input = input("Enter your age: ")
    age = int(age_input) if age_input.isdigit() else 0
    
    # Multiple variables from single input
    first, middle, last = "John", "Doe", "Smith"
    
    return name, age, (first, middle, last)

# Example: Using variables in loops
counter = 0
total = 0
numbers = [10, 20, 30, 40, 50]

for num in numbers:
    total += num
    counter += 1

print(f"Sum: {total}, Count: {counter}, Average: {total/counter:.2f}")

# Example: Flag variables
is_valid = True
has_error = False

if is_valid and not has_error:
    print("Processing continues...")

# Example: Accumulator pattern
accumulator = 0
for i in range(1, 6):
    accumulator += i
    print(f"After adding {i}: {accumulator}")

# Example: Using None as placeholder
result = None
print(f"Result initially: {result}")

# Later assign a value
result = 42
print(f"Result now: {result}")