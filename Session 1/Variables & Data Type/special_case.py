"""
Variable:
 -> We can change the values or any variable by assigning a new value
 -> Python is Dynamically typed, means you can't need to declair the data_type of the value
 -> Can Hold new value even with different data_types of the value.
"""


# Value Assigning 
score = 12
# print(score) # output: 12
# Value Reassigning
score = 13 
# print(score)  # output: 13

# Type changes automatically
data = 42                # int
print(type(data))        # <class 'int'>

data = 3.14              # float
print(type(data))        # <class 'float'>

data = "Hello"           # str
print(type(data))        # <class 'str'>

data = [1, 2, 3]         # list
print(type(data))        # <class 'list'>


# Multiple variables in one line
x, y, z = 1, 2, 3
print(x, y, z)           # 1 2 3

# Assign same value to multiple variables
a = b = c = 100
print(a, b, c)           # 100 100 100

# Unpacking sequences
colors = ["red", "green", "blue"]
r, g, b = colors
print(r, g, b)           # red green blue

# Multiple assignments with the different data_types
name, age, cgpa = 'nazim', 23, 3.99
# print(f'{name} Data Type{type(name)} \n{age} Data Type{type(age)} \n{cgpa} Data Type{type(cgpa)}')

# Variabels swaping
# Traditional way (other languages)
a = 10
b = 20
temp = a
a = b
b = temp
print(a, b)              # 20 10

# ✅ Python way (Elegant)
a, b = b, a
print(a, b)              # 10 20

# Swapping multiple variables
x, y, z = 1, 2, 3
x, y, z = z, x, y
print(x, y, z)           # 3 1 2


# Constants 
# By convention, treat these as constants
PI = 3.14159
MAX_CONNECTIONS = 100
API_BASE_URL = "https://api.example.com"
DEFAULT_TIMEOUT = 30

# But they can still be reassigned (no enforcement)
PI = 3.14  # Python allows this but violates convention

# Variables are references to objects in memory
x = 10
y = x  # y references same object as x
print(id(x), id(y))    # Same memory address

# Immutable objects (int, str, tuple)
x = 10
y = x
x = 20  # Creates new object
print(y)  # Still 10 (unchanged)

# Mutable objects (list, dict, set)
list1 = [1, 2, 3]
list2 = list1
list1.append(4)
print(list2)  # [1, 2, 3, 4] (changed!)


# Shallow copy
original = [1, 2, [3, 4]]
copy1 = original.copy()
copy1[2][0] = 99
print(original)  # [1, 2, [99, 4]]  # Nested changes affect original

# Deep copy (for complete independence)
import copy
copy2 = copy.deepcopy(original)
copy2[2][0] = 100
print(original)  # [1, 2, [99, 4]]  # Original unchanged


# Global variable
global_var = "I'm global"

def my_function():
    # Local variable
    local_var = "I'm local"
    print(global_var)    # Can access global
    print(local_var)     # Can access local

def modify_global():
    global global_var    # Need 'global' to modify
    global_var = "Modified!"

my_function()
modify_global()
print(global_var)        # "Modified!"

def outer():
    x = "outer"
    
    def inner():
        nonlocal x      # Access parent's variable
        x = "inner"
        print(x)        # "inner"
    
    inner()
    print(x)            # "inner" (modified by inner function)

outer()



#  Variable Scope & Lifetime scope Rules (LEGB):
# L - Local
# E - Enclosing
# G - Global
# B - Built-in

x = "global"

def outer():
    x = "outer enclosing"
    
    def inner():
        x = "local"
        print(x)           # "local" (Local scope)
    
    inner()
    print(x)               # "outer enclosing" (Enclosing scope)

outer()
print(x)                   # "global" (Global scope)

# Delete any value, data
# Using del Statement:

x = 10
print(x)      # 10
del x         # Delete variable
# print(x)    # ❌ NameError: name 'x' is not defined

# Delete multiple variables
a, b, c = 1, 2, 3
del a, b, c





# Type annotations (doesn't enforce, just for clarity)
name: str = "Python"
age: int = 30
scores: list[int] = [85, 90, 78]
person: dict[str, any] = {"name": "John", "age": 25}

# Function annotations
def greet(name: str) -> str:
    return f"Hello, {name}"

def calculate(a: int, b: int) -> int:
    return a + b


