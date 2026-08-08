# Tuple Basics
# CREATING TUPLES

# Empty tuple
empty_tuple = ()
print(f"Empty tuple: {empty_tuple}")

# Single element tuple (NOTE: comma is mandatory!)
single_tuple = (5,)  # Without comma, it's just int
not_tuple = (5)      # This is int, not tuple
print(f"Single element tuple: {single_tuple}")
print(f"Type of single_tuple: {type(single_tuple)}")
print(f"Type of not_tuple: {type(not_tuple)}")

# Multiple elements
numbers = (1, 2, 3, 4, 5)
mixed = (1, "Hello", 3.14, True, [1, 2])  # Can contain different types
nested = ((1, 2), (3, 4), (5, 6))        # Nested tuples

# Using tuple() constructor
from_list = tuple([1, 2, 3, 4])
from_string = tuple("Hello")
from_range = tuple(range(5))

print(f"From list: {from_list}")
print(f"From string: {from_string}")
print(f"From range: {from_range}")

# Tuple unpacking
a, b, c = (1, 2, 3)
print(f"Unpacked values: a={a}, b={b}, c={c}")

# Extended unpacking with *
first, *middle, last = (1, 2, 3, 4, 5)
print(f"First: {first}, Middle: {middle}, Last: {last}")


# Accessing Elements
# ACCESSING TUPLE ELEMENTS
# -------------------------

my_tuple = (10, 20, 30, 40, 50, 60, 70)

# Indexing (0-based)
print(f"First element: {my_tuple[0]}")        # 10
print(f"Last element: {my_tuple[-1]}")        # 70
print(f"Second last: {my_tuple[-2]}")         # 60

# Slicing [start:end:step]
print(f"First 3 elements: {my_tuple[:3]}")    # (10, 20, 30)
print(f"Last 3 elements: {my_tuple[-3:]}")    # (50, 60, 70)
print(f"Elements 2-4: {my_tuple[1:4]}")       # (20, 30, 40)
print(f"Every 2nd element: {my_tuple[::2]}")  # (10, 30, 50, 70)
print(f"Reverse tuple: {my_tuple[::-1]}")     # (70, 60, 50, 40, 30, 20, 10)

# Accessing nested tuple
nested = ((1, 2), (3, 4), (5, 6))
print(f"First nested: {nested[0]}")           # (1, 2)
print(f"Element at [1][1]: {nested[1][1]}")   # 4


# Tuple Operations
# TUPLE OPERATIONS
# -----------------

t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = (1, 2, 3)

# Concatenation (+)
concatenated = t1 + t2
print(f"Concatenation: {concatenated}")       # (1, 2, 3, 4, 5, 6)

# Repetition (*)
repeated = t1 * 3
print(f"Repetition: {repeated}")              # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Membership (in, not in)
print(f"Is 2 in t1? {2 in t1}")               # True
print(f"Is 5 in t1? {5 in t1}")               # False
print(f"Is 5 not in t1? {5 not in t1}")       # True

# Comparison operators
print(f"t1 == t3: {t1 == t3}")                # True
print(f"t1 != t2: {t1 != t2}")                # True
print(f"t1 < t2: {t1 < t2}")                  # True (lexicographic)

# Identity comparison
print(f"t1 is t3: {t1 is t3}")                # False (different objects)

# Length
print(f"Length of t1: {len(t1)}")             # 3


# Built-in Functions

# BUILT-IN FUNCTIONS FOR TUPLES
# ------------------------------

numbers = (5, 2, 8, 1, 9, 3, 7, 4, 6, 5)

# min() - minimum value
print(f"Minimum: {min(numbers)}")             # 1

# max() - maximum value
print(f"Maximum: {max(numbers)}")             # 9

# sum() - sum of all elements
print(f"Sum: {sum(numbers)}")                 # 50

# len() - length of tuple
print(f"Length: {len(numbers)}")              # 10

# sorted() - returns sorted list (tuple remains unchanged)
sorted_list = sorted(numbers)
print(f"Sorted list: {sorted_list}")
print(f"Original tuple unchanged: {numbers}")

# sorted() with reverse
sorted_desc = sorted(numbers, reverse=True)
print(f"Sorted descending: {sorted_desc}")

# count() - count occurrences
print(f"Count of 5: {numbers.count(5)}")      # 2

# index() - find first occurrence
print(f"Index of 8: {numbers.index(8)}")      # 2
print(f"Index of 5 from position 3: {numbers.index(5, 3)}")  # 9

# any() - True if any element is True
bool_tuple = (0, 0, 1, 0)
print(f"any() on bool_tuple: {any(bool_tuple)}")  # True

# all() - True if all elements are True
print(f"all() on bool_tuple: {all(bool_tuple)}")  # False

# enumerate() - get index-value pairs
for index, value in enumerate(numbers[:5]):
    print(f"Index {index}: {value}")

# zip() - combine multiple tuples
names = ("Alice", "Bob", "Charlie")
ages = (25, 30, 35)
combined = tuple(zip(names, ages))
print(f"Zipped: {combined}")                  # (('Alice', 25), ('Bob', 30), ('Charlie', 35))


# Tuple Methods
# TUPLE METHODS
# --------------

my_tuple = (1, 2, 3, 2, 4, 2, 5)

# count() - count occurrences of value
print(f"Count of 2: {my_tuple.count(2)}")     # 3

# index() - find index of value
print(f"First index of 2: {my_tuple.index(2)}")  # 1
print(f"Index of 2 after position 2: {my_tuple.index(2, 2)}")  # 3
print(f"Index of 2 between 2 and 5: {my_tuple.index(2, 2, 5)}")  # 3

# NOTE: No append(), insert(), remove(), pop(), clear() 
# because tuples are IMMUTABLE

# Converting Between Types
# TYPE CONVERSIONS
# ----------------

my_tuple = (1, 2, 3, 4, 5)

# Tuple to List
list_from_tuple = list(my_tuple)
print(f"Tuple to list: {list_from_tuple}")

# Tuple to Set (removes duplicates)
set_from_tuple = set(my_tuple)
print(f"Tuple to set: {set_from_tuple}")

# Tuple to String (for strings)
str_tuple = ('H', 'e', 'l', 'l', 'o')
string_from_tuple = ''.join(str_tuple)
print(f"Tuple to string: {string_from_tuple}")

# List to Tuple
list_data = [1, 2, 3]
tuple_from_list = tuple(list_data)
print(f"List to tuple: {tuple_from_list}")

# Set to Tuple
set_data = {1, 2, 3}
tuple_from_set = tuple(set_data)
print(f"Set to tuple: {tuple_from_set}")


# Advanced Tuple Operations
# ADVANCED OPERATIONS
# -------------------

# Tuple comprehension (actually generator expression)
squares = tuple(x**2 for x in range(5))
print(f"Squares: {squares}")  # (0, 1, 4, 9, 16)

# Filtering with tuple
even_numbers = tuple(x for x in range(10) if x % 2 == 0)
print(f"Even numbers: {even_numbers}")  # (0, 2, 4, 6, 8)

# Mapping with tuple
doubled = tuple(map(lambda x: x*2, (1, 2, 3, 4)))
print(f"Doubled: {doubled}")  # (2, 4, 6, 8)

# Filter with tuple
filtered = tuple(filter(lambda x: x > 2, (1, 2, 3, 4, 5)))
print(f"Filtered (>2): {filtered}")  # (3, 4, 5)

# Reduce (from functools)
from functools import reduce
product = reduce(lambda x, y: x * y, (1, 2, 3, 4))
print(f"Product: {product}")  # 24

# Sorting tuple of tuples
data = ((3, "c"), (1, "a"), (2, "b"))
sorted_data = tuple(sorted(data))
print(f"Sorted: {sorted_data}")  # ((1, 'a'), (2, 'b'), (3, 'c'))

# Sorting by second element
sorted_by_second = tuple(sorted(data, key=lambda x: x[1]))
print(f"Sorted by second: {sorted_by_second}")  # ((1, 'a'), (2, 'b'), (3, 'c'))



# Tuple as Dictionary Keys

# TUPLE AS DICTIONARY KEYS
# -------------------------

# Tuples can be used as dictionary keys (lists cannot)
coordinates = {
    (0, 0): "Origin",
    (1, 0): "Right",
    (0, 1): "Up",
    (-1, 0): "Left",
    (0, -1): "Down"
}

print(f"Coordinate (0,0): {coordinates[(0, 0)]}")
print(f"Coordinate (1,0): {coordinates[(1, 0)]}")

# Iterating over dictionary with tuple keys
for (x, y), label in coordinates.items():
    print(f"Position ({x}, {y}): {label}")



# Problem 1: Swap Two Variables Without Temp
# PROBLEM 1: Swap two variables
# ------------------------------

def swap_variables(a, b):
    """
    Swap two variables using tuple unpacking
    Time: O(1), Space: O(1)
    """
    print(f"Before swap: a={a}, b={b}")
    a, b = b, a
    print(f"After swap: a={a}, b={b}")
    return a, b

# Test
swap_variables(10, 20)


# Problem 2: Return Multiple Values from Function
# PROBLEM 2: Return multiple values
# ---------------------------------

def get_min_max_avg(numbers):
    """
    Return min, max, and average of a list
    Time: O(n), Space: O(1)
    """
    if not numbers:
        return None, None, None
    
    min_val = min(numbers)
    max_val = max(numbers)
    avg_val = sum(numbers) / len(numbers)
    
    return min_val, max_val, avg_val

# Test
numbers = [10, 20, 30, 40, 50]
min_val, max_val, avg_val = get_min_max_avg(numbers)
print(f"Min: {min_val}, Max: {max_val}, Avg: {avg_val:.2f}")


# Problem 3: Find Most Frequent Element
# PROBLEM 3: Most frequent element
# ---------------------------------

def most_frequent_element(nums):
    """
    Find the most frequent element using tuple
    Time: O(n), Space: O(n)
    """
    from collections import Counter
    
    # Count frequencies
    freq = Counter(nums)
    
    # Get most common as tuple (element, count)
    most_common = freq.most_common(1)[0]
    
    return most_common[0], most_common[1]

# Test
nums = [1, 3, 2, 1, 4, 1, 3, 2, 1]
element, count = most_frequent_element(nums)
print(f"Most frequent: {element} (appears {count} times)")


# Problem 4: Merge Two Sorted Tuples
# PROBLEM 4: Merge two sorted tuples
# ----------------------------------

def merge_sorted_tuples(t1, t2):
    """
    Merge two sorted tuples into one sorted tuple
    Time: O(n+m), Space: O(n+m)
    """
    i = j = 0
    result = []
    
    while i < len(t1) and j < len(t2):
        if t1[i] <= t2[j]:
            result.append(t1[i])
            i += 1
        else:
            result.append(t2[j])
            j += 1
    
    # Add remaining elements
    result.extend(t1[i:])
    result.extend(t2[j:])
    
    return tuple(result)

# Test
t1 = (1, 3, 5, 7)
t2 = (2, 4, 6, 8)
merged = merge_sorted_tuples(t1, t2)
print(f"Merged: {merged}")  # (1, 2, 3, 4, 5, 6, 7, 8)


# Problem 5: Find Pair with Target Sum
# PROBLEM 5: Two Sum Problem
# --------------------------

def two_sum(nums, target):
    """
    Find two numbers that sum to target
    Returns tuple of indices or None
    Time: O(n), Space: O(n)
    """
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i
    
    return None

# Test
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(f"Indices: {result}")  # (0, 1)


# Problem 6: Remove Duplicates While Preserving Order
# PROBLEM 6: Remove duplicates preserving order
# ---------------------------------------------

def remove_duplicates_preserve_order(data):
    """
    Remove duplicates while preserving order using tuple
    Time: O(n), Space: O(n)
    """
    seen = set()
    result = []
    
    for item in data:
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return tuple(result)

# Test
data = (1, 2, 2, 3, 4, 4, 4, 5)
unique = remove_duplicates_preserve_order(data)
print(f"Unique: {unique}")  # (1, 2, 3, 4, 5)


# Problem 7: Rotate Tuple
# PROBLEM 7: Rotate tuple by k positions
# --------------------------------------

def rotate_tuple(tup, k):
    """
    Rotate tuple by k positions to the right
    Time: O(n), Space: O(n)
    """
    if not tup:
        return tup
    
    k = k % len(tup)  # Handle k > len
    return tup[-k:] + tup[:-k]

# Test
tup = (1, 2, 3, 4, 5)
print(f"Rotate by 2: {rotate_tuple(tup, 2)}")  # (4, 5, 1, 2, 3)
print(f"Rotate by 7: {rotate_tuple(tup, 7)}")  # (4, 5, 1, 2, 3)



# Problem 8: Flatten Nested Tuple

# PROBLEM 8: Flatten nested tuple
# -------------------------------

def flatten_tuple(nested):
    """
    Flatten a nested tuple
    Time: O(n), Space: O(n)
    """
    result = []
    
    def flatten_recursive(item):
        if isinstance(item, tuple):
            for sub_item in item:
                flatten_recursive(sub_item)
        else:
            result.append(item)
    
    flatten_recursive(nested)
    return tuple(result)

# Test
nested = (1, (2, 3), (4, (5, 6)), 7)
flattened = flatten_tuple(nested)
print(f"Flattened: {flattened}")  # (1, 2, 3, 4, 5, 6, 7)


# Tuple vs List: When to Use
# TUPLE VS LIST - USE CASES
# -------------------------

# USE TUPLE WHEN:
# 1. Data should not change (immutable)
# 2. Dictionary keys needed
# 3. Faster iteration (slightly)
# 4. Memory efficiency
# 5. Returning multiple values from function
# 6. Representing fixed data (coordinates, RGB values)

# Examples:
rgb = (255, 128, 0)  # RGB color (never changes)
coordinates = (45.5, -122.6)  # GPS coordinates

# USE LIST WHEN:
# 1. Data needs to change (mutable)
# 2. Need to add/remove elements
# 3. Dynamic collection of items
# 4. Need to sort in-place

# Performance comparison
import timeit

# Tuple is slightly faster for iteration
tuple_iter = timeit.timeit('for i in (1,2,3,4,5): pass', number=1000000)
list_iter = timeit.timeit('for i in [1,2,3,4,5]: pass', number=1000000)

print(f"Tuple iteration: {tuple_iter:.6f} seconds")
print(f"List iteration: {list_iter:.6f} seconds")



# COMMON INTERVIEW QUESTIONS
# --------------------------

# Q1: Why are tuples immutable?
"""
A: Tuples are immutable for:
1. Performance optimization
2. Hashable (can be used as dict keys)
3. Data integrity (data won't change accidentally)
4. Memory efficiency (smaller than lists)
"""

# Q2: How to convert tuple to list and vice versa?
# Answer: Use list() and tuple() constructors

# Q3: What is tuple unpacking?
# Answer: Assigning tuple elements to variables in one line

# Q4: When to use tuple over list?
# Answer: When data is constant, need dict keys, return multiple values

# Q5: Can tuple contain mutable elements?
# Answer: Yes, tuples can contain lists, dictionaries, etc.
mixed_tuple = (1, [2, 3], {"a": 4})
print(f"Tuple with mutable elements: {mixed_tuple}")

# Q6: How to modify a tuple?
# Answer: Convert to list, modify, convert back to tuple
def modify_tuple(tup, index, new_value):
    temp_list = list(tup)
    temp_list[index] = new_value
    return tuple(temp_list)

modified = modify_tuple((1, 2, 3), 1, 99)
print(f"Modified tuple: {modified}")  # (1, 99, 3)

# Q7: How to concatenate tuples?
# Answer: Using + operator
t1 = (1, 2)
t2 = (3, 4)
result = t1 + t2
print(f"Concatenated: {result}")  # (1, 2, 3, 4)

# Q8: How to multiply tuples?
# Answer: Using * operator
result = t1 * 3
print(f"Multiplied: {result}")  # (1, 2, 1, 2, 1, 2)

# Q9: How to check if element exists?
# Answer: Using 'in' operator
print(f"2 in (1,2,3): {2 in (1,2,3)}")  # True

# Q10: How to get index of element?
# Answer: Using index() method
print(f"Index of 2: {(1,2,3).index(2)}")  # 1




# PERFORMANCE COMPARISON
# ----------------------

import sys
import time

# Memory comparison
list_memory = [1, 2, 3, 4, 5]
tuple_memory = (1, 2, 3, 4, 5)

print(f"List memory: {sys.getsizeof(list_memory)} bytes")
print(f"Tuple memory: {sys.getsizeof(tuple_memory)} bytes")
print(f"Tuple uses {sys.getsizeof(list_memory) - sys.getsizeof(tuple_memory)} bytes less")

# Creation time comparison
def measure_creation(n):
    start = time.time()
    list_comp = [i for i in range(n)]
    list_time = time.time() - start
    
    start = time.time()
    tuple_comp = tuple(i for i in range(n))
    tuple_time = time.time() - start
    
    return list_time, tuple_time

n = 1000000
list_time, tuple_time = measure_creation(n)
print(f"List creation time: {list_time:.6f} seconds")
print(f"Tuple creation time: {tuple_time:.6f} seconds")
print(f"Tuple is {((list_time - tuple_time) / list_time * 100):.2f}% faster")




# ADVANCED Inteview PATTERNS


# Pattern 1: Function returning multiple values with names
def get_student_info():
    return ("John", 25, "Computer Science")

# Using namedtuple for better readability
from collections import namedtuple

Student = namedtuple('Student', ['name', 'age', 'major'])
student = Student("John", 25, "Computer Science")
print(f"Student: {student.name}, {student.age}, {student.major}")

# Pattern 2: Tuple as function arguments
def calculate(*args):
    """Calculate sum and product of any number of arguments"""
    return sum(args), reduce(lambda x, y: x * y, args) if args else 0

print(f"Sum and Product: {calculate(1, 2, 3, 4)}")

# Pattern 3: Tuple in dictionary comprehensions
data = [("a", 1), ("b", 2), ("c", 3)]
dict_from_tuples = {k: v for k, v in data}
print(f"Dictionary from tuples: {dict_from_tuples}")

# Pattern 4: Swapping using tuple (already covered)

# Pattern 5: Comparing tuples lexicographically
print(f"(1,2,3) < (1,2,4): {(1,2,3) < (1,2,4)}")  # True
print(f"(1,2,3) < (1,2,3,1): {(1,2,3) < (1,2,3,1)}")  # True
print(f"(1,2,3) == (1,2,3): {(1,2,3) == (1,2,3)}")  # True


# ERROR HANDLING
# --------------

def safe_tuple_operation(data):
    """
    Demonstrates error handling with tuples
    """
    try:
        # Attempt to modify tuple (will raise TypeError)
        data[0] = 100
    except TypeError as e:
        print(f"Caught error: {e} (tuples are immutable)")
    
    try:
        # Attempt to get index that doesn't exist
        print(data[10])
    except IndexError as e:
        print(f"Caught error: {e} (index out of range)")
    
    try:
        # Attempt to find value that doesn't exist
        print(data.index(999))
    except ValueError as e:
        print(f"Caught error: {e} (value not in tuple)")

# Test
safe_tuple_operation((1, 2, 3))




# QUICK REFERENCE CARD
# --------------------

# Creation
t = ()                     # Empty
t = (1,)                   # Single element (comma needed!)
t = (1, 2, 3)              # Multiple elements
t = tuple([1, 2, 3])       # From list

# Access
t[0]                       # First element
t[-1]                      # Last element
t[1:3]                     # Slicing

# Operations
t1 + t2                    # Concatenation
t * 3                      # Repetition
2 in t                     # Membership
len(t)                     # Length

# Methods
t.count(x)                 # Count occurrences
t.index(x)                 # Find index

# Functions
min(t), max(t)             # Min, max
sum(t)                     # Sum
sorted(t)                  # Sorted list
tuple(sorted(t))           # Sorted tuple

# Unpacking
a, b, c = t                # Basic unpacking
a, *b = t                  # Extended unpacking

# Conversion
list(t)                    # To list
set(t)                     # To set
tuple(list)                # From list

# Hashable (can be dict key)
d = {t: "value"}           # Tuple as key


