"""
tuples_comprehensive.py

Comprehensive tuple guide:
- Creation, indexing, slicing
- Operations, built-ins, methods
- Conversions, advanced patterns
- Common interview problems
- Extensive conditional examples (including nested)
- Inline comments explain expressions, operators, and intent

This file is runnable and aims to be safe (no intentional runtime errors).
"""

from functools import reduce
from collections import Counter, namedtuple, defaultdict
import sys
import time
import timeit
import math

# ---------------------------
# 1. TUPLE BASICS - Creation
# ---------------------------

# Empty tuple literal: parentheses with nothing inside
empty_tuple = ()  # empty tuple object

# Single-element tuple: comma is mandatory because parentheses alone are grouping
single_tuple = (5,)     # tuple with one element: 5
not_tuple = (5)         # parentheses only -> integer 5 (grouping expression)

# Multiple elements tuple
numbers = (1, 2, 3, 4, 5)               # tuple of ints
mixed = (1, "Hello", 3.14, True, None)  # heterogeneous tuple (allowed)
nested = ((1, 2), (3, 4), (5, 6))       # nested tuples

# tuple() constructor from iterables
from_list = tuple([1, 2, 3, 4])         # convert list to tuple
from_string = tuple("Hello")            # tuple of characters: ('H','e','l','l','o')
from_range = tuple(range(5))            # (0,1,2,3,4)

# Tuple unpacking: left-side variables receive elements from right-side tuple
a, b, c = (1, 2, 3)                     # a=1, b=2, c=3

# Extended unpacking: * collects remaining elements as list
first, *middle, last = (1, 2, 3, 4, 5)  # first=1, middle=[2,3,4], last=5

# ---------------------------
# 2. Accessing elements
# ---------------------------

my_tuple = (10, 20, 30, 40, 50, 60, 70)

# Indexing: 0-based
first_elem = my_tuple[0]    # 10, index 0 -> first element
last_elem = my_tuple[-1]    # 70, negative index -1 -> last element
second_last = my_tuple[-2]  # 60, negative index -2 -> second last

# Slicing: [start:end:step], end exclusive
first_three = my_tuple[:3]       # elements indices 0..2 -> (10,20,30)
last_three = my_tuple[-3:]       # last 3 elements -> (50,60,70)
middle_slice = my_tuple[1:4]     # indices 1..3 -> (20,30,40)
every_second = my_tuple[::2]     # step 2 -> (10,30,50,70)
reversed_tuple = my_tuple[::-1]  # reversed order

# Access nested tuple elements
first_nested = nested[0]         # (1,2)
nested_item = nested[1][1]       # 4 (second element of second tuple)

# Safe access helper: avoid IndexError by checking length first
def safe_get(tup, index, default=None):
    # if index within bounds, return element, else default
    if -len(tup) <= index < len(tup):
        return tup[index]
    return default

# ---------------------------
# 3. Tuple operations (immutable)
# ---------------------------

t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = (1, 2, 3)

# Concatenation: + returns new tuple
concatenated = t1 + t2           # (1,2,3,4,5,6)

# Repetition: * repeats the sequence
repeated = t1 * 3                 # (1,2,3,1,2,3,1,2,3)

# Membership: 'in' / 'not in' - O(n) linear search
has_two = (2 in t1)
has_five = (5 in t1)
not_has_five = (5 not in t1)

# Comparison: element-wise lexicographic comparisons
eq_test = (t1 == t3)              # True
ne_test = (t1 != t2)              # True
lt_test = (t1 < t2)               # True if t1 lexicographically less than t2

# Identity check (object identity): 'is' rarely used for tuples, use only to check same object
same_object = (t1 is t3)          # usually False unless interned/aliased

# Length
length_t1 = len(t1)

# ---------------------------
# 4. Built-in functions & methods
# ---------------------------

nums = (5, 2, 8, 1, 9, 3, 7, 4, 6, 5)

min_val = min(nums)               # minimum value
max_val = max(nums)               # maximum value
sum_val = sum(nums)               # sum
len_nums = len(nums)              # length

# sorted() returns a new list (tuple unchanged)
sorted_list = sorted(nums)        # list
sorted_desc = sorted(nums, reverse=True)

# methods available on tuple objects (immutability -> only count and index)
count_5 = nums.count(5)           # occurrences of 5
index_8 = nums.index(8)           # first index of 8
index_5_after3 = nums.index(5, 3) # start search at position 3

# any/all treat elements as truthy/falsy
bool_tuple = (0, 0, 1, 0)
any_true = any(bool_tuple)        # True if any element truthy
all_true = all(bool_tuple)        # True if all truthy

# enumerate and zip examples
for index, value in enumerate(nums[:5]):  # enumerate yields (index, value) pairs
    pass

names = ("Alice", "Bob", "Charlie")
ages = (25, 30, 35)
zipped = tuple(zip(names, ages))  # ((name, age), ...)

# ---------------------------
# 5. Conversions between types
# ---------------------------

my_tuple = (1, 2, 3, 4, 5)

list_from_tuple = list(my_tuple)     # [1,2,3,4,5]
set_from_tuple = set(my_tuple)       # {1,2,3,4,5} (order unspecified)
str_from_tuple = ''.join(('H','e','l','l','o'))  # "Hello"
tuple_from_list = tuple([1,2,3])     # (1,2,3)
tuple_from_set = tuple({1,2,3})      # order unspecified

# ---------------------------
# 6. Advanced tuple patterns
# ---------------------------

# Generator expression inside tuple() creates a tuple of computed values
squares = tuple(x**2 for x in range(5))       # (0,1,4,9,16)

# Filtering and mapping via tuples uses generator expressions or map/filter then tuple()
even_numbers = tuple(x for x in range(10) if x % 2 == 0)
doubled = tuple(map(lambda x: x*2, (1,2,3,4)))
filtered = tuple(filter(lambda x: x > 2, (1,2,3,4,5)))

# reduce example
product = reduce(lambda x, y: x * y, (1,2,3,4))  # 24

# Sorting tuples (of tuples) returns list unless wrapped in tuple()
data = ((3, "c"), (1, "a"), (2, "b"))
sorted_data = tuple(sorted(data))                 # sorted by first element
sorted_by_second = tuple(sorted(data, key=lambda x: x[1]))

# Namedtuple for readable tuple-like records
Student = namedtuple('Student', ['name', 'age', 'major'])
student = Student("John", 25, "CS")
# Access by attr: student.name student.age

# Tuples as dict keys (hashable)
coordinates = {
    (0, 0): "Origin",
    (1, 0): "Right",
    (0, 1): "Up"
}

# swap using unpacking
def swap_variables(a, b):
    # a,b = b,a performs tuple packing on right then unpacking on left
    a, b = b, a
    return a, b

# return multiple values (function returns a tuple implicitly)
def get_min_max_avg(numbers):
    if not numbers:
        return None, None, None
    return min(numbers), max(numbers), sum(numbers)/len(numbers)

# merge two sorted tuples (like merge step of merge sort)
def merge_sorted_tuples(t1, t2):
    i = j = 0
    result = []
    while i < len(t1) and j < len(t2):
        if t1[i] <= t2[j]:
            result.append(t1[i])
            i += 1
        else:
            result.append(t2[j])
            j += 1
    result.extend(t1[i:])
    result.extend(t2[j:])
    return tuple(result)

# rotate tuple by k to the right
def rotate_tuple(tup, k):
    if not tup:
        return tup
    k = k % len(tup)
    if k == 0:
        return tup
    return tup[-k:] + tup[:-k]

# flatten nested tuple recursively
def flatten_tuple(nested):
    result = []
    def _flatten(x):
        if isinstance(x, tuple):
            for item in x:
                _flatten(item)
        else:
            result.append(x)
    _flatten(nested)
    return tuple(result)

# remove duplicates preserving order (returns tuple)
def remove_duplicates_preserve_order(data):
    seen = set()
    result = []
    for item in data:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return tuple(result)

# ---------------------------
# 7. Interview-style problems using tuples
# ---------------------------

# Two-sum returning indices as tuple
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        comp = target - num
        if comp in seen:
            return (seen[comp], i)
        seen[num] = i
    return None

# Most frequent element using Counter.most_common -> returns (elem, count) tuple
def most_frequent_element(nums):
    if not nums:
        return None, 0
    freq = Counter(nums)
    elem, cnt = freq.most_common(1)[0]
    return elem, cnt

# Flatten and merge patterns already above

# safe tuple operation demonstrating error handling
def safe_tuple_operation(data):
    try:
        # Attempt to modify tuple element (should raise TypeError)
        data[0] = 100
    except TypeError as e:
        # explain immutability
        err_msg = f"Caught TypeError: {e}"
    try:
        _ = data[10]   # may raise IndexError
    except IndexError as e:
        err_msg2 = f"Caught IndexError: {e}"
    try:
        data.index(999)  # may raise ValueError
    except ValueError as e:
        err_msg3 = f"Caught ValueError: {e}"
    return True  # function demonstrates handling, returns True to indicate completion

# ---------------------------
# 8. Conditional statements (exhaustive cases & nesting)
# ---------------------------

# We'll build many conditional examples relevant to tuples and general Python code,
# demonstrating operators, truthiness, short-circuiting, chained comparisons, nesting,
# ternary expressions, identity and membership checks, and error-safe guards.

# Example: classify a tuple based on contents and size
def classify_tuple(tup):
    # guard: ensure tup is actually a tuple
    if tup is None:                       # identity check for None
        return "no tuple"
    if not isinstance(tup, tuple):        # type check
        return "not a tuple"
    if not tup:                           # emptiness check (falsy if empty)
        return "empty tuple"

    # length-based branches
    n = len(tup)
    if n == 1:
        return "singleton tuple"
    elif 2 <= n <= 4:
        return "small tuple"
    elif n > 4:
        # further nested checks based on content
        # check for all elements being numbers (use all + isinstance)
        if all(isinstance(x, (int, float)) for x in tup):
            # chained comparison example: check if all between 0 and 100
            if all(0 <= x <= 100 for x in tup):
                return "large numeric tuple in range"
            else:
                return "large numeric tuple out of range"
        # check if tuple contains mutable items (like list/dict)
        elif any(isinstance(x, (list, dict, set)) for x in tup):
            return "large tuple with mutable elements"
        else:
            return "large tuple of mixed types"
    else:
        return "unknown"

# Ternary example
def tuple_status(tup):
    return "empty" if not tup else "non-empty"

# Short-circuit example using callables to show lazy evaluation
def short_circuit_demo(is_ready_fn, get_value_fn):
    # if is_ready_fn() is False, get_value_fn() is not called due to 'and' short-circuit
    if is_ready_fn() and get_value_fn():
        return True
    return False

# Nested condition with membership and identity
def nested_permissions(user):
    """
    user expected as dict with keys: 'role', 'active', 'permissions' (tuple/list)
    Demonstrates nested if/elif/else, membership, 'in', identity 'is', and ternary usage.
    """
    if user is None:
        return "no user"

    # guard clause: ensure dictionary structure
    if not isinstance(user, dict):
        return "invalid user object"

    if not user.get('active', False):
        return "inactive"

    role = user.get('role', 'guest')
    perms = tuple(user.get('permissions', ()))  # convert to tuple for membership checks

    if role == 'admin':
        # nested checks for admin
        if 'all' in perms:
            return "admin: full access"
        elif 'manage' in perms:
            return "admin: manage access"
        else:
            # ternary: return limited if age < 18 else admin-limited
            return "admin-limited" if user.get('age', 0) >= 18 else "admin-underage"
    elif role == 'editor':
        # combined logical operators
        if ('edit' in perms and 'publish' in perms) or user.get('senior', False):
            return "editor: publish"
        elif 'edit' in perms:
            return "editor: edit only"
        else:
            return "editor: no edit perms"
    elif role == 'viewer':
        return "viewer"
    else:
        # default: guest; nested ternary to decide level from groups
        groups = user.get('groups', ())
        return ("guest-public" if 'public' in groups else "guest-private") if groups else "guest"

# Demonstration of chained comparisons, bitwise example, and tuple content checks
def complex_checks(tup):
    # ensure tuple
    if not isinstance(tup, tuple):
        raise TypeError("Expected tuple")

    results = {}
    # chained comparison: check first element within range if numeric
    if tup and isinstance(tup[0], (int, float)):
        x = tup[0]
        results['first_in_range'] = (0 <= x <= 10)  # uses chained comparison
    else:
        results['first_in_range'] = False

    # bitwise operator example on integers present in tuple
    ints = [i for i in tup if isinstance(i, int)]
    if len(ints) >= 2:
        a, b = ints[0], ints[1]
        results['bitwise_and'] = a & b
        results['bitwise_or'] = a | b
        results['bitwise_xor'] = a ^ b
    else:
        results['bitwise'] = None

    # membership and identity
    results['has_zero'] = (0 in tup)
    results['is_singleton'] = (len(tup) == 1)

    return results

# ---------------------------
# 9. Operators used in real-life code (examples)
# ---------------------------

# Arithmetic: + - * / // % ** (used in calculations)
def arithmetic_examples(a, b):
    return {
        'add': a + b,
        'sub': a - b,
        'mul': a * b,
        'true_div': a / b if b != 0 else None,
        'floor_div': a // b if b != 0 else None,
        'mod': a % b if b != 0 else None,
        'pow': a ** b
    }

# Comparison: == != < <= > >= (used for sorting, branching)
def compare_examples(x, y):
    return {
        'eq': x == y,
        'ne': x != y,
        'lt': x < y,
        'le': x <= y,
        'gt': x > y,
        'ge': x >= y
    }

# Logical: and, or, not (used in guards and combined conditions)
def logical_examples(a, b):
    return {
        'and': bool(a and b),
        'or': bool(a or b),
        'not_a': not a
    }

# Membership: in, not in (used for membership checks)
def membership_examples(elem, seq):
    return {
        'in': elem in seq,
        'not_in': elem not in seq
    }

# Identity: is, is not (used to check None or same object)
def identity_examples(a, b):
    return {
        'is': a is b,
        'is_not': a is not b
    }

# Bitwise: &, |, ^, <<, >>, ~ (used in low-level or performance code)
def bitwise_examples(a, b):
    return {
        'and': a & b,
        'or': a | b,
        'xor': a ^ b,
        'lshift': a << 1,
        'rshift': a >> 1,
        'invert': ~a
    }

# Augmented assignments: +=, -=, *=, etc. (used for counters and accumulation)
def augmented_assignment_demo():
    x = 10
    x += 5  # x = x + 5
    x *= 2  # x = x * 2
    x -= 3
    x //= 4
    x ^= 2  # bitwise XOR and assign
    return x

# ---------------------------
# 10. Performance comparisons and memory
# ---------------------------

# Memory size difference between list and tuple containers
list_mem = [1,2,3,4,5]
tuple_mem = (1,2,3,4,5)
list_size = sys.getsizeof(list_mem)
tuple_size = sys.getsizeof(tuple_mem)
memory_saving = list_size - tuple_size

# Creation time comparison (small demonstration)
tuple_iter_time = timeit.timeit('for i in (1,2,3,4,5): pass', number=1000000)
list_iter_time = timeit.timeit('for i in [1,2,3,4,5]: pass', number=1000000)

# ---------------------------
# 11. Error handling patterns (safe code)
# ---------------------------

def modify_tuple_safe(tup, index, new_value):
    # To 'modify' a tuple, convert to list, change, convert back
    if not isinstance(tup, tuple):
        raise TypeError("Expected tuple")
    lst = list(tup)
    if not (-len(lst) <= index < len(lst)):
        raise IndexError("Index out of range")
    lst[index] = new_value
    return tuple(lst)

# Safe index retrieval with default
def index_or_default(tup, value, default=-1):
    try:
        return tup.index(value)
    except ValueError:
        return default

# ---------------------------
# 12. Quick reference (examples)
# ---------------------------

# Creation: (), (x,), tuple(iterable)
# Access: tup[i], tup[-1], tup[a:b]
# Operations: +, *, in, len(), count(), index()
# Conversion: list(tup), set(tup), tuple(list)
# Use-cases: immutability, dict keys, function returns

# ---------------------------
# 13. Demo / Tests
# ---------------------------

if __name__ == "__main__":
    # Basic prints
    print("empty_tuple:", empty_tuple)
    print("single_tuple:", single_tuple, type(single_tuple))
    print("not_tuple:", not_tuple, type(not_tuple))
    print("from_list:", from_list)
    print("from_string:", from_string)
    print("from_range:", from_range)
    print("unpacked a,b,c:", a, b, c)
    print("first,middle,last:", first, middle, last)

    # Access
    print("first_elem:", first_elem, "last_elem:", last_elem, "second_last:", second_last)
    print("first_three:", first_three, "reversed:", reversed_tuple)

    # Operations
    print("concatenated:", concatenated)
    print("repeated:", repeated)
    print("membership 2 in t1:", has_two, "5 in t1:", has_five)

    # Built-ins & methods
    print("min,max,sum,len:", min_val, max_val, sum_val, len_nums)
    print("sorted_list sample:", sorted_list[:5])
    print("count_5,index_8:", count_5, index_8)

    # Conversions
    print("list_from_tuple:", list_from_tuple)
    print("set_from_tuple:", set_from_tuple)

    # Advanced
    print("squares:", squares)
    print("namedtuple student:", student)
    print("coordinates dict lookup:", coordinates[(0,0)])

    # Functions
    print("swap(10,20):", swap_variables(10,20))
    print("get_min_max_avg:", get_min_max_avg([10,20,30,40,50]))
    print("merge_sorted:", merge_sorted_tuples((1,3,5),(2,4,6)))
    print("rotate (1..5) by 2:", rotate_tuple((1,2,3,4,5), 2))
    print("flatten nested:", flatten_tuple((1,(2,3),(4,(5,6)))))

    # Interview problems
    print("two_sum indices:", two_sum([2,7,11,15], 9))
    print("most_frequent:", most_frequent_element([1,3,2,1,4,1,3,2,1]))
    print("remove_duplicates_preserve_order:", remove_duplicates_preserve_order((1,2,2,3,4,4,5)))

    # Conditionals
    print("classify_tuple:", classify_tuple((1,2,3)))
    print("tuple_status empty:", tuple_status(()), "non-empty:", tuple_status((1,)))
    print("nested_permissions:", nested_permissions({'role':'admin','active':True,'permissions':('manage',),'age':20}))

    # Operators examples
    print("arithmetic_examples:", arithmetic_examples(10,3))
    print("compare_examples:", compare_examples(2,3))
    print("logical_examples:", logical_examples(True, False))
    print("membership_examples:", membership_examples(2, (1,2,3)))
    print("identity_examples:", identity_examples((1,2), (1,2)))  # likely False

    # Performance/memory
    print(f"list_size={list_size}, tuple_size={tuple_size}, memory_saving={memory_saving}")
    print(f"tuple iter time: {tuple_iter_time:.6f}, list iter time: {list_iter_time:.6f}")