"""
lists_with_conditionals.py
Comprehensive examples of Python list usage, list-related algorithms, and many varieties
of conditional statements. Designed to be readable, runnable, and educational.
"""

# Basic imports used in multiple examples
from array import array           # for memory-efficient numeric arrays
from functools import reduce     # for reduce examples
import bisect                    # for binary search helpers
import copy                      # for shallow/deep copy functions
import sys                       # for memory size examples
import math                      # for math helpers used below
import timeit                    # for performance micro-benchmarks

# ---------------------------
# 1. List creation and initialization
# ---------------------------

# Empty list creation (two equivalent ways)
empty_list = []       # literal empty list: fastest and most common
empty_list2 = list()  # constructor form, returns empty list too

# List with initial values (homogeneous or heterogeneous)
numbers = [1, 2, 3, 4, 5]                       # integers
fruits = ['apple', 'banana', 'orange']         # strings
mixed = [1, 'hello', 3.14, True]               # different types mixed in one list

# List comprehensions (concise, readable)
squares = [x**2 for x in range(10)]            # list of squares: 0..9 squared
even_numbers = [x for x in range(20) if x % 2 == 0]

# Nested lists: represent matrices or 2D grids
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Defensive check: avoid errors when using functions that expect non-empty lists
def safe_first(lst):
    # Return first element or None if list empty; avoids IndexError.
    return lst[0] if lst else None

# ---------------------------
# 2. Accessing and slicing
# ---------------------------

fruits = ['apple', 'banana', 'orange', 'grape', 'mango']  # example list

first = fruits[0]        # index 0 => first element
last = fruits[-1]        # negative index -1 => last element
second_last = fruits[-2] # -2 => second last

# Slicing uses [start:end:step], end is exclusive
first_two = fruits[0:2]      # elements at indices 0 and 1
last_three = fruits[-3:]     # last three elements
reverse = fruits[::-1]       # reversed list using step -1
every_second = fruits[::2]   # every second item starting at index 0

# Length and membership
length = len(fruits)                 # number of elements
has_banana = 'banana' in fruits      # True if 'banana' present
has_peach = 'peach' in fruits        # False if 'peach' not present

# ---------------------------
# 3. Adding elements
# ---------------------------

fruits = ['apple', 'banana']
fruits.append('orange')              # add to end

fruits.insert(1, 'grape')            # insert at index 1 (shifts later elements)

fruits.extend(['mango', 'peach'])    # extend by another iterable (adds each element)

# Concatenation and repetition (non-destructive unless reassigned)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2             # new list, original lists unchanged

repeated = [1, 2] * 3                # repetition operator, repeats elements

# ---------------------------
# 4. Removing elements
# ---------------------------

fruits = ['apple', 'banana', 'orange', 'banana']
fruits.remove('banana')              # removes first matching value (raises ValueError if absent)

# Use try/except to avoid exception when removing unknown item
try:
    fruits.remove('pineapple')
except ValueError:
    # safe fallback when item not present
    pass

fruits = ['apple', 'banana', 'orange']
last_item = fruits.pop()             # pop without index removes last and returns it
first_item = fruits.pop(0)           # pop index 0 removes and returns first element

fruits = ['apple', 'banana', 'orange', 'grape']
del fruits[1]                        # deletes element by index
del fruits[1:3]                      # deletes a slice of elements

fruits.clear()                       # remove all elements (fruits becomes [])

# ---------------------------
# 5. Searching and counting
# ---------------------------

fruits = ['apple', 'banana', 'orange', 'banana']
index_banana = fruits.index('banana') # index of first match (ValueError if missing)

count_banana = fruits.count('banana') # number of occurrences

# Linear search example (explicit)
def find_element(lst, target):
    # Return index of first target or -1 if not found; uses enumerate for index/value
    for i, element in enumerate(lst):
        if element == target:
            return i
    return -1

# Binary search using bisect (requires sorted list)
sorted_list = [1, 3, 5, 7, 9, 11]
pos_left = bisect.bisect_left(sorted_list, 7)   # insertion index to keep order (left)
pos_right = bisect.bisect_right(sorted_list, 7) # insertion index to the right

# ---------------------------
# 6. Sorting and reversing
# ---------------------------

numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()                 # sorts in-place
numbers.sort(reverse=True)     # sorts in-place descending

numbers = [3, 1, 4, 1, 5, 9, 2]
sorted_numbers = sorted(numbers)                  # returns a new sorted list
sorted_desc = sorted(numbers, reverse=True)

words = ['banana', 'apple', 'cherry', 'date']
words.sort(key=len)            # sort by string length, mutates words
words.sort(key=lambda x: x[-1])# sort by last character

fruits = ['apple', 'banana', 'orange']
fruits.reverse()               # reverse in-place
for fruit in reversed(fruits): # reversed() returns iterator, original unchanged
    pass

# ---------------------------
# 7. Copying lists (shallow vs deep)
# ---------------------------

original = [1, 2, [3, 4]]      # nested list includes inner list

copy1 = original.copy()        # shallow copy; inner list is shared
copy2 = list(original)         # also shallow
copy3 = original[:]            # slicing shallow copy
copy4 = copy.copy(original)    # shallow via copy module

deep_copy = copy.deepcopy(original) # deep copy duplicates nested objects
deep_copy[2][0] = 99                 # modifying deep copy doesn't change original

# ---------------------------
# 8. Iteration patterns
# ---------------------------

fruits = ['apple', 'banana', 'orange']
for fruit in fruits:                     # iterate values directly
    pass

for index, fruit in enumerate(fruits):   # iterate with index starting at 0
    pass

for index, fruit in enumerate(fruits, start=1): # index starts at 1
    pass

names = ['Alice', 'Bob', 'Charlie']
scores = [85, 92, 78]
for name, score in zip(names, scores):   # iterate two lists in parallel; stops at shortest
    pass

squared = [x**2 for x in range(5)]       # list comprehension iteration

# ---------------------------
# 9. Data analysis helpers
# ---------------------------

numbers = [3, 1, 4, 1, 5, 9, 2]
minimum = min(numbers)                   # smallest element
maximum = max(numbers)                   # largest element

# Avoid division by zero when computing average:
average = (sum(numbers) / len(numbers)) if numbers else None

all_true = all([True, True, True])       # True if all elements truthy
some_truthy = any([0, 0, 5])             # True if any element truthy

even_numbers_filtered = list(filter(lambda x: x % 2 == 0, numbers))  # filter usage
squared_map = list(map(lambda x: x**2, numbers))                     # map usage

product = reduce(lambda x, y: x * y, [1, 2, 3, 4], 1)                 # reduce with initializer

# ---------------------------
# 10. Advanced operations
# ---------------------------

# Flatten nested list using comprehension
nested = [[1, 2], [3, 4], [5, 6]]
flattened = [item for sublist in nested for item in sublist]

# Remove duplicates while preserving order
def remove_duplicates(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result

original = [1, 2, 2, 3, 4, 4, 5]
unique = remove_duplicates(original)

# Partition list into two lists by condition
def partition(lst, condition):
    # returns (matching, non_matching)
    matching = [x for x in lst if condition(x)]
    non_matching = [x for x in lst if not condition(x)]
    return matching, non_matching

numbers = [1, 2, 3, 4, 5, 6]
even, odd = partition(numbers, lambda x: x % 2 == 0)

# Chunk list into smaller lists
def chunk_list(lst, chunk_size):
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

data = [1, 2, 3, 4, 5, 6, 7, 8]
chunks = chunk_list(data, 3)

# ---------------------------
# 11. Comparisons, subset, differences
# ---------------------------

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [1, 2, 4]

# Equality compares element-wise
assert (list1 == list2) is True
assert (list1 == list3) is False
assert (list1 < list3) is True  # lexicographic comparison: compares first differing element

def is_subset(small, large):
    # check each item in small is present in large
    return all(item in large for item in small)

subset = [1, 2]
superset = [1, 2, 3, 4]
is_subset(subset, superset)

# Common elements
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = [x for x in list1 if x in list2]
diff = [x for x in list1 if x not in list2]

# ---------------------------
# 12. Memory and performance notes
# ---------------------------

# Large list vs generator (memory demo)
list_comp = [x**2 for x in range(100000)]    # big memory usage
gen_exp = (x**2 for x in range(100000))      # generator uses much less memory
size_list = sys.getsizeof(list_comp)
size_gen = sys.getsizeof(gen_exp)

# Using array module for numeric data (more compact)
numbers_array = array('i', [1, 2, 3, 4, 5])

# Pre-allocation for repeated append-heavy loops
n = 1000000
# preallocated = [0] * n   # uncomment if you need real preallocation; memory heavy

# Performance micro-benchmark functions
def using_append():
    result = []
    for i in range(1000):
        result.append(i)
    return result

def using_comprehension():
    return [i for i in range(1000)]

# ---------------------------
# 13. Common interview problems (cleaned, safe)
# ---------------------------

def two_sum(nums, target):
    """
    Find two indices where nums[i] + nums[j] == target.
    Time: O(n), Space: O(n)
    Returns list of indices or [] if none found.
    """
    seen = {}  # maps number -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# find_missing_number: assume nums contains distinct numbers from 0..n with one missing
def find_missing_number(nums):
    n = len(nums)
    # expected sum for numbers 0..n is n*(n+1)//2 if one number missing from 0..n
    # But if list len is n and numbers are from 0..n with one missing, expected_sum is n*(n+1)//2
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# rotate_array: rotate in-place to right by k steps; handle edge cases
def rotate_array(nums, k):
    if not nums:
        return nums
    n = len(nums)
    k = k % n
    if k == 0:
        return nums
    nums[:] = nums[-k:] + nums[:-k]
    return nums

# find_duplicate using Floyd's tortoise and hare (works when numbers are in 1..n and one duplicate)
def find_duplicate(nums):
    if not nums:
        raise ValueError("nums must be non-empty")
    slow = nums[0]
    fast = nums[0]
    # Find intersection
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    # Find entrance to cycle
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow

# merge_sorted_arrays: merge nums2 into nums1 which has buffer at end (LeetCode style)
def merge_sorted_arrays(nums1, m, nums2, n):
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

# ---------------------------
# 14. Practical examples
# ---------------------------

def process_data(data):
    """
    Convert CSV-like list of rows into list of dicts keyed by header row.
    Returns [] if data empty or only header.
    """
    if not data:
        return []
    headers = data[0]
    rows = data[1:]
    result = []
    for row in rows:
        # zip stops at shortest; we deliberately allow missing columns to be ignored
        row_dict = dict(zip(headers, row))
        result.append(row_dict)
    return result

def transpose_matrix(matrix):
    # Validate matrix non-empty and rectangular
    if not matrix:
        return []
    row_len = len(matrix[0])
    if any(len(row) != row_len for row in matrix):
        raise ValueError("All rows must have the same length")
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(row_len)]

def group_by_key(items, key_func):
    groups = {}
    for item in items:
        key = key_func(item)
        groups.setdefault(key, []).append(item)
    return groups

# ---------------------------
# 15. Conditional statements and many cases (examples)
# ---------------------------

# Basic if/elif/else
def classify_number(x):
    # Demonstrates comparisons and chained comparisons
    if x is None:                       # identity operator: check for None
        return "no value"
    if x < 0:
        return "negative"
    elif x == 0:
        return "zero"
    elif 0 < x < 1:                     # chained comparison
        return "fraction"
    elif x >= 1 and x < 10:             # logical and
        return "small"
    else:
        return "large"

# Ternary conditional expression
def sign(x):
    return "positive" if x > 0 else ("zero" if x == 0 else "negative")

# Truthiness examples
def truthiness_examples(value):
    # Demonstrates how different values evaluate in boolean context
    if value:                # truthy values (non-empty, non-zero)
        return "truthy"
    else:
        return "falsy"

# Membership and identity together
def membership_and_identity(x, container):
    # 'in' checks membership; 'is' checks identity
    return (x in container), (x is container)

# Short-circuit evaluation
def short_circuit(a, b):
    # a and b are callables to demonstrate short-circuiting
    # logical AND: if first is falsy, second not evaluated
    if a() and b():
        return True
    return False

# Nested conditionals: more complex real-world flow
def access_control(user):
    """
    Example of nested and combined conditionals to decide access level.
    user is expected to be a dict with keys: 'active', 'role', 'age', 'groups'
    """
    if not user or not isinstance(user, dict):           # guard clause
        return "no access"

    if not user.get('active', False):                    # check boolean flag
        return "inactive user"

    role = user.get('role', 'guest')
    age = user.get('age', 0)
    groups = user.get('groups', [])

    # nested ifs with combined conditions
    if role == 'admin':
        # admins with age check (compound condition)
        if age >= 18:
            return "full admin access"
        else:
            return "limited admin access"

    elif role == 'editor':
        # editors need to be in 'editors' group or be older than 21
        if 'editors' in groups or age > 21:
            return "editor access"
        else:
            return "no editor privileges"

    elif role == 'user':
        # regular users: nested permission checks
        if 'beta' in groups:
            return "beta user"
        elif age >= 13:
            return "standard user"
        else:
            return "child account"

    else:
        # guest or unknown roles: ternary inside return
        return "guest" if 'public' in groups else "no access"

# Chained comparisons and bitwise operator example
def compare_and_bitwise(a, b):
    # demonstrates comparison operators and bitwise AND/OR
    is_a_gt_b = a > b
    in_range = 0 <= a <= 100              # chained
    bitwise_and = a & b                   # bitwise AND (integers)
    bitwise_or = a | b                    # bitwise OR
    return is_a_gt_b, in_range, bitwise_and, bitwise_or

# Demonstrate assignment operators and augmented assignment
def assignment_examples():
    x = 10               # simple assignment
    x += 5               # augmented: same as x = x + 5
    x *= 2               # x = x * 2
    x //= 3              # integer floor-division and assign
    x ^= 3               # bitwise XOR and assign
    return x

# try/except with conditional inside
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return math.inf   # return infinity when dividing by zero
    except TypeError:
        return None       # return None if wrong types passed

# ---------------------------
# 16. Operators in real-life code examples (list)
# ---------------------------
# Arithmetic: +, -, *, /, //, %, **
# Comparison: ==, !=, <, <=, >, >=
# Logical: and, or, not
# Membership: in, not in
# Identity: is, is not
# Bitwise: &, |, ^, ~, <<, >>
# Assignment (incl augmented): =, +=, -=, *=, /=, //=, %=, **=, &=, |=, ^=

# Example function that uses many operator types together
def financial_rounding(balance, rate_percent, years):
    """
    Example using arithmetic, comparison, logical, and bitwise in a realistic formula.
    R = final value after compound interest, but we ensure inputs valid.
    """
    if balance is None or rate_percent is None or years is None:
        return None
    if balance < 0 or years < 0:
        return None

    # arithmetic and power operator
    rate = rate_percent / 100.0
    final = balance * ((1 + rate) ** years)

    # comparison
    if final >= 1_000_000:   # underscore allowed in numeric literals for readability
        status = "millionaire"
    elif final >= 100_000:
        status = "rich"
    else:
        status = "normal"

    # bitwise used for a toy condition (not common in finance) to show operator usage
    flag = (int(years) & 1)  # 1 if years odd, 0 if even
    return final, status, bool(flag)

# ---------------------------
# 17. Tests / demonstrations (simple)
# ---------------------------

if __name__ == "__main__":
    # quick functional tests to ensure basic operations run
    print("two_sum:", two_sum([2, 7, 11, 15], 9))
    print("missing:", find_missing_number([3, 0, 1]))
    print("rotate:", rotate_array([1, 2, 3, 4, 5], 2))
    print("merge:", merge_sorted_arrays([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
    print("transpose:", transpose_matrix([[1,2,3],[4,5,6]]))
    print("access:", access_control({'active': True, 'role': 'user', 'age': 14, 'groups': []}))
    print("financial:", financial_rounding(50000, 5, 10))






    
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
