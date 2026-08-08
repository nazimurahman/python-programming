# List Creation and Initialization
# Empty list creation
empty_list = []  # Most common way
empty_list2 = list()  # Using constructor

# List with initial values
numbers = [1, 2, 3, 4, 5]
fruits = ['apple', 'banana', 'orange']
mixed = [1, 'hello', 3.14, True]  # Heterogeneous list

# List comprehension - powerful creation technique
squares = [x**2 for x in range(10)]  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
even_numbers = [x for x in range(20) if x % 2 == 0]  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Nested lists (matrix)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# Basic List Operations
# Accessing elements (Indexing - 0-based)
fruits = ['apple', 'banana', 'orange', 'grape', 'mango']
first = fruits[0]  # 'apple'
last = fruits[-1]  # 'mango' (negative indexing)
second_last = fruits[-2]  # 'grape'

# Slicing - [start:end:step]
fruits = ['apple', 'banana', 'orange', 'grape', 'mango']
first_two = fruits[0:2]  # ['apple', 'banana']
last_three = fruits[-3:]  # ['orange', 'grape', 'mango']
reverse = fruits[::-1]  # ['mango', 'grape', 'orange', 'banana', 'apple']
every_second = fruits[::2]  # ['apple', 'orange', 'mango']

# Length of list
length = len(fruits)  # 5

# Membership testing
has_banana = 'banana' in fruits  # True
has_peach = 'peach' in fruits  # False


# Adding Elements to List
# append() - Add single element at end
fruits = ['apple', 'banana']
fruits.append('orange')  # ['apple', 'banana', 'orange']

# insert() - Add element at specific position
fruits.insert(1, 'grape')  # ['apple', 'grape', 'banana', 'orange']

# extend() - Add multiple elements (another iterable)
fruits.extend(['mango', 'peach'])  # ['apple', 'grape', 'banana', 'orange', 'mango', 'peach']

# Concatenation (+ operator)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2  # [1, 2, 3, 4, 5, 6]

# Repetition (* operator)
repeated = [1, 2] * 3  # [1, 2, 1, 2, 1, 2]

# Removing Elements from List
# remove() - Remove first occurrence of value
fruits = ['apple', 'banana', 'orange', 'banana']
fruits.remove('banana')  # ['apple', 'orange', 'banana'] (removes first banana only)

# pop() - Remove and return element at index (default last)
fruits = ['apple', 'banana', 'orange']
last = fruits.pop()  # 'orange', fruits = ['apple', 'banana']
first = fruits.pop(0)  # 'apple', fruits = ['banana']

# del - Delete element(s) by index
fruits = ['apple', 'banana', 'orange', 'grape']
del fruits[1]  # ['apple', 'orange', 'grape']
del fruits[1:3]  # ['apple'] (slice deletion)

# clear() - Remove all elements
fruits.clear()  # []

# Searching and Finding Elements
# index() - Find index of first occurrence
fruits = ['apple', 'banana', 'orange', 'banana']
index = fruits.index('banana')  # 1
# index = fruits.index('grape')  # ValueError: 'grape' is not in list

# count() - Count occurrences
count = fruits.count('banana')  # 2

# Linear search (manual)
def find_element(lst, target):
    for i, element in enumerate(lst):
        if element == target:
            return i
    return -1

# Binary search (list must be sorted)
import bisect
sorted_list = [1, 3, 5, 7, 9, 11]
position = bisect.bisect_left(sorted_list, 7)  # 3
position = bisect.bisect_right(sorted_list, 7)  # 4

# Sorting and Reversing
# sort() - Sort list in-place (modifies original)
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()  # [1, 1, 2, 3, 4, 5, 9]
numbers.sort(reverse=True)  # [9, 5, 4, 3, 2, 1, 1]

# sorted() - Return new sorted list (original unchanged)
numbers = [3, 1, 4, 1, 5, 9, 2]
sorted_numbers = sorted(numbers)  # [1, 1, 2, 3, 4, 5, 9]
sorted_desc = sorted(numbers, reverse=True)  # [9, 5, 4, 3, 2, 1, 1]

# Custom sorting with key function
words = ['banana', 'apple', 'cherry', 'date']
words.sort(key=len)  # Sort by length: ['date', 'apple', 'banana', 'cherry']
words.sort(key=lambda x: x[-1])  # Sort by last character

# reverse() - Reverse list in-place
fruits = ['apple', 'banana', 'orange']
fruits.reverse()  # ['orange', 'banana', 'apple']

# reversed() - Return reverse iterator (original unchanged)
fruits = ['apple', 'banana', 'orange']
for fruit in reversed(fruits):
    print(fruit)  # orange, banana, apple


# List Copying

# Shallow copy methods
original = [1, 2, [3, 4]]

# Method 1: copy() method
copy1 = original.copy()

# Method 2: list() constructor
copy2 = list(original)

# Method 3: slicing
copy3 = original[:]

# Method 4: copy module
import copy
copy4 = copy.copy(original)

# Deep copy (for nested lists)
deep_copy = copy.deepcopy(original)
# Modifying nested list in deep copy doesn't affect original
deep_copy[2][0] = 99  # Only deep_copy changes


# List Iteration Techniques

# Basic iteration
fruits = ['apple', 'banana', 'orange']
for fruit in fruits:
    print(fruit)

# With index using enumerate
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# With starting index
for index, fruit in enumerate(fruits, start=1):
    print(f"Position {index}: {fruit}")

# Multiple lists simultaneously (zip)
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# List comprehension iteration
squared = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]


# List Methods for Data Analysis

# min(), max(), sum()
numbers = [3, 1, 4, 1, 5, 9, 2]
minimum = min(numbers)  # 1
maximum = max(numbers)  # 9
total = sum(numbers)  # 25
average = sum(numbers) / len(numbers)  # 3.571...

# all() - True if all elements are True
all_true = all([True, True, True])  # True
all_numbers = all([1, 2, 3])  # True (non-zero numbers are truthy)
mixed = all([1, 0, 3])  # False

# any() - True if any element is True
any_true = any([False, False, True])  # True
any_numbers = any([0, 0, 5])  # True

# filter() - Filter elements based on condition
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4, 6]

# map() - Apply function to all elements
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))  # [1, 4, 9, 16, 25]

# reduce() - Reduce list to single value
from functools import reduce
product = reduce(lambda x, y: x * y, [1, 2, 3, 4])  # 24


# Advanced List Operations

# Flatten nested list
nested = [[1, 2], [3, 4], [5, 6]]
flattened = [item for sublist in nested for item in sublist]  # [1, 2, 3, 4, 5, 6]

# Remove duplicates while preserving order
def remove_duplicates(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

original = [1, 2, 2, 3, 4, 4, 5]
unique = remove_duplicates(original)  # [1, 2, 3, 4, 5]

# Grouping elements by condition
numbers = [1, 2, 3, 4, 5, 6]
even = [x for x in numbers if x % 2 == 0]  # [2, 4, 6]
odd = [x for x in numbers if x % 2 != 0]  # [1, 3, 5]

# Partition list
def partition(lst, condition):
    return [x for x in lst if condition(x)], [x for x in lst if not condition(x)]

numbers = [1, 2, 3, 4, 5, 6]
even, odd = partition(numbers, lambda x: x % 2 == 0)

# Chunk list into smaller lists
def chunk_list(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

data = [1, 2, 3, 4, 5, 6, 7, 8]
chunks = chunk_list(data, 3)  # [[1, 2, 3], [4, 5, 6], [7, 8]]


# List Comparison and Equality

# Comparing lists (lexicographical order)
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [1, 2, 4]

print(list1 == list2)  # True
print(list1 == list3)  # False
print(list1 < list3)   # True (3 < 4)

# Check if one list is subset/superset
def is_subset(small, large):
    return all(item in large for item in small)

subset = [1, 2]
superset = [1, 2, 3, 4]
is_subset(subset, superset)  # True

# Find common elements
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = [x for x in list1 if x in list2]  # [3, 4]

# Find differences
diff = [x for x in list1 if x not in list2]  # [1, 2]


# Memory Optimization and Performance

# List vs Generator (memory efficient)
import sys

# List comprehension (eager evaluation)
list_comp = [x**2 for x in range(1000000)]
memory_usage = sys.getsizeof(list_comp)  # Large memory usage

# Generator expression (lazy evaluation)
gen_exp = (x**2 for x in range(1000000))
memory_usage = sys.getsizeof(gen_exp)  # Small memory usage

# Using list of lists vs array module
from array import array
# For large numeric data
numbers = array('i', [1, 2, 3, 4, 5])  # More memory efficient

# Pre-allocating list for performance
n = 1000000
preallocated = [0] * n  # Faster than append

# Performance comparison
import timeit

def using_append():
    result = []
    for i in range(1000):
        result.append(i)
    return result

def using_comprehension():
    return [i for i in range(1000)]

# List comprehension is usually faster


# Common Interview Problems: -> Problem Two Sum
def two_sum(nums, target):
    """
    Find two numbers in list that sum to target.
    Time: O(n), Space: O(n)
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Test
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # [0, 1]


# Problem Find Missing Number
def find_missing_number(nums):
    """
    Find missing number in list of 0 to n
    Time: O(n), Space: O(1)
    """
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# Test
nums = [3, 0, 1]
print(find_missing_number(nums))  # 2

# Problem Rotate Array

def rotate_array(nums, k):
    """
    Rotate array to right by k steps
    Time: O(n), Space: O(1)
    """
    n = len(nums)
    k = k % n  # Handle k > n
    nums[:] = nums[-k:] + nums[:-k]  # In-place rotation
    return nums

# Test
nums = [1, 2, 3, 4, 5]
print(rotate_array(nums, 2))  # [4, 5, 1, 2, 3]

# Problem Find Duplicate
def find_duplicate(nums):
    """
    Find duplicate in array (Floyd's algorithm)
    Time: O(n), Space: O(1)
    """
    slow = nums[0]
    fast = nums[0]
    
    # Find intersection point
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    # Find duplicate
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow

# Test
nums = [1, 3, 4, 2, 2]
print(find_duplicate(nums))  # 2

# Problem Merge Sorted Arrays

def merge_sorted_arrays(nums1, m, nums2, n):
    """
    Merge nums2 into nums1 (in-place)
    Time: O(m+n), Space: O(1)
    """
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1
    
    while p2 >= 0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    return nums1

# Test
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
print(merge_sorted_arrays(nums1, m, nums2, n))  # [1, 2, 2, 3, 5, 6]

# Practical Examples
# Example 1: Processing CSV-like data
def process_data(data):
    """
    Process list of lists as CSV data
    """
    if not data:
        return {}
    
    headers = data[0]
    rows = data[1:]
    
    result = []
    for row in rows:
        row_dict = dict(zip(headers, row))
        result.append(row_dict)
    
    return result

# Test
data = [
    ['Name', 'Age', 'City'],
    ['Alice', '30', 'New York'],
    ['Bob', '25', 'London']
]
print(process_data(data))

# Example 2: Matrix operations
def transpose_matrix(matrix):
    """
    Transpose a matrix (list of lists)
    """
    return [[matrix[j][i] for j in range(len(matrix))]
            for i in range(len(matrix[0]))]

matrix = [[1, 2, 3], [4, 5, 6]]
print(transpose_matrix(matrix))  # [[1, 4], [2, 5], [3, 6]]

# Example 3: Group similar items
def group_by_key(items, key_func):
    """
    Group items by computed key
    """
    groups = {}
    for item in items:
        key = key_func(item)
        if key not in groups:
            groups[key] = []
        groups[key].append(item)
    return groups

people = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 30}
]
grouped = group_by_key(people, lambda x: x['age'])
print(grouped)  # {30: [{'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 30}], 25: [{'name': 'Bob', 'age': 25}]}



# Summary:
#   -> Mastering lists in Python is crucial for coding interviews and everyday programming. Key concepts to remember:
#   -> Time Complexity: Understanding Big O for each operation
#   -> Memory Management: When to use lists vs generators
#   -> Common Patterns: Two-pointer, sliding window, etc.
#   -> Built-in Functions: Leverage Python's rich built-in functions
#   -> List Comprehensions: Write concise and efficient code
#   -> Slicing: Powerful for array manipulation
#   -> In-place vs Copy: Know when to modify vs create new
#   -> Edge Cases: Empty lists, negative indexing, etc.
