"""
sets_comprehensive.py

Comprehensive examples and utilities for Python sets.
Covers:
- Basics and creation
- Mathematical operations and methods
- Advanced usage (frozenset, nested, large data)
- Common interview problems using sets
- Many conditional examples demonstrating operators and control flow
- Performance notes and gotchas

This file is intended to be runnable and educational.
"""

from collections import Counter, defaultdict
import time
import math

# ---------------------------
# 1. SET BASICS
# ---------------------------

# Key properties:
# - Unordered: no indexing, order not guaranteed
# - Mutable: you can add/remove elements
# - No duplicates: duplicates are automatically removed
# - Elements must be hashable (immutable types allowed: numbers, strings, tuples, frozenset)
# - Membership testing is O(1) on average

# Empty set creation: {} creates dict, so use set()
empty_set = set()           # correct empty set
empty_dict = {}             # dictionary (not a set)
# show types
# print(type(empty_set), type(empty_dict))

# Set with elements; duplicates removed automatically
fruits = {'apple', 'banana', 'orange', 'apple'}  # duplicate 'apple' kept once

# Mixed hashable types allowed
mixed_set = {1, 'hello', 3.14, (1, 2)}  # tuple is hashable
# unhashable example (commented out to avoid runtime error)
# invalid = {1, [2, 3]}  # TypeError: unhashable type: 'list'

# ---------------------------
# 2. SET CREATION METHODS
# ---------------------------

# Method 1: curly braces (literal)
set1 = {1, 2, 3, 4, 5}

# Method 2: set() constructor from iterables
set2 = set([1, 2, 3])
set3 = set((1, 2, 3))
set4 = set(range(1, 6))
set5 = set('hello')  # {'h', 'e', 'l', 'o'}

# Method 3: set comprehension
squares = {x**2 for x in range(1, 6)}
even_numbers = {x for x in range(10) if x % 2 == 0}

# Method 4: from dictionary keys (iterates keys)
dict_data = {'a': 1, 'b': 2}
set_from_dict = set(dict_data)  # {'a', 'b'}

# Method 5: set of tuples (tuples are hashable)
tuple_set = {('a', 1), ('b', 2)}

# ---------------------------
# 3. MATHEMATICAL SET OPERATIONS
# ---------------------------

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
C = {1, 2, 3}

# Union: elements in A or B (| or union())
union_op = A | B
union_method = A.union(B)

# Intersection: elements in both ( & or intersection() )
intersection_op = A & B
intersection_method = A.intersection(B)

# Difference: elements in A not in B ( - or difference() )
difference_op = A - B
difference_method = A.difference(B)

# Symmetric difference: elements in either but not both ( ^ or symmetric_difference() )
sym_diff_op = A ^ B
sym_diff_method = A.symmetric_difference(B)

# Multiple unions/intersections
multi_union = A.union(B, {9, 10}, {11, 12})
multi_intersection = A.intersection(B, {4, 5, 9})

# ---------------------------
# 4. BUILT-IN METHODS DEMONSTRATIONS
# ---------------------------

numbers = {1, 2, 3, 4, 5}
# add single element
numbers.add(6)

# update with any iterable (set/list/tuple/string)
numbers.update({7, 8})
numbers.update([9, 10])
numbers.update((11, 12))
numbers.update('13')  # adds characters '1' and '3' individually

# remove (raises KeyError if missing) vs discard (no error)
if 12 in numbers:
    numbers.remove(12)
numbers.discard(100)  # safe even if 100 not present

# pop removes and returns an arbitrary element (since set unordered)
popped = None
if numbers:
    popped = numbers.pop()

# clear removes all elements
temp_set = {1, 2, 3}
temp_set.clear()

# membership tests
_ = 5 in numbers
_ = 100 not in numbers

# shallow copy
original = {1, 2, 3}
copied = original.copy()
copied.add(4)  # original unchanged

# comparison helpers
s1 = {1, 2, 3}
s2 = {1, 2, 3, 4, 5}
s3 = {4, 5, 6}
_ = s1.issubset(s2)
_ = s2.issuperset(s1)
_ = s1.isdisjoint(s3)

# in-place update methods
a = {1, 2, 3}
b = {3, 4, 5}
# difference_update: remove items in b from a
a_diff = a.copy()
a_diff.difference_update(b)
# intersection_update: keep only common
a_int = a.copy()
a_int.intersection_update(b)
# symmetric_difference_update: keep items not in both
a_sym = a.copy()
a_sym.symmetric_difference_update(b)
# update: add all elements from other
a_upd = {1, 2}
a_upd.update({3, 4})

# ---------------------------
# 5. ADVANCED SETS
# ---------------------------

# Sets containing tuples (e.g., coordinates)
coordinates = {(1, 2), (3, 4)}
coordinates.add((5, 6))

# frozenset: immutable and hashable (can be dict key or element of set)
frozen = frozenset([1, 2, 3])
set_with_frozen = {frozen, (4, 5)}

# Use sets to remove duplicates from list
list_with_duplicates = [1, 2, 2, 3, 3, 4]
unique_list = list(set(list_with_duplicates))  # order not guaranteed

# find common elements across multiple lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7]
list3 = [3, 4, 5, 8]
common_three = set(list1) & set(list2) & set(list3)

# elements unique to each list
set1 = set(list1)
set2 = set(list2)
set3 = set(list3)
unique_to_1 = set1 - set2 - set3
unique_to_2 = set2 - set1 - set3

# complex set comprehension with conditionals
complex_set = {x for x in range(20) if x > 0 and x % 2 == 0 and x % 3 == 0}  # {6,12,18}

# flatten nested matrix to set
matrix = [[1,2,3],[4,5,6]]
flat_set = {n for row in matrix for n in row}

# string processing with sets
text = "hello world"
vowels = {'a','e','i','o','u'}
text_set = set(text)
vowels_in_text = text_set & vowels
consonants_in_text = text_set - vowels - {' '}

# ---------------------------
# 6. PERFORMANCE DEMO (membership)
# ---------------------------

big_list = list(range(1_000_000))
big_set = set(big_list)

start = time.time()
_ = (999_999 in big_list)
list_time = time.time() - start

start = time.time()
_ = (999_999 in big_set)
set_time = time.time() - start

# compute speedup safely (avoid division by zero)
speedup = (list_time / set_time) if set_time > 0 else float('inf')

# ---------------------------
# 7. INTERVIEW PROBLEMS (SET-BASED SOLUTIONS)
# ---------------------------

# Problem 1: All unique pairs that sum to target
def find_pairs_with_sum(arr, target):
    seen = set()
    pairs = set()
    for num in arr:
        comp = target - num
        if comp in seen:
            pairs.add(tuple(sorted((num, comp))))
        seen.add(num)
    return pairs

# Problem 2: Intersection including duplicates using Counter
def intersection_with_duplicates(arr1, arr2):
    c1 = Counter(arr1)
    c2 = Counter(arr2)
    res = []
    for num in c1:
        if num in c2:
            count = min(c1[num], c2[num])
            res.extend([num] * count)
    return res

# Problem 3: Longest consecutive sequence
def longest_consecutive_sequence(nums):
    if not nums:
        return 0
    num_set = set(nums)
    longest = 0
    for num in num_set:
        # start only at sequence beginnings
        if num - 1 not in num_set:
            current = num
            length = 1
            while current + 1 in num_set:
                current += 1
                length += 1
            longest = max(longest, length)
    return longest

# Problem 4: Missing number in 1..n (works when one missing)
def find_missing_number(nums):
    n = len(nums)
    full = set(range(1, n + 2))  # numbers 1..n+1 where one is missing in nums
    missing = full - set(nums)
    return missing.pop() if missing else None

# Problem 5: Find duplicates
def find_duplicates(nums):
    seen = set()
    dup = set()
    for x in nums:
        if x in seen:
            dup.add(x)
        else:
            seen.add(x)
    return list(dup)

# Problem 6: Valid Sudoku checker
def is_valid_sudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    for i in range(9):
        for j in range(9):
            val = board[i][j]
            if val == '.':
                continue
            idx = (i // 3) * 3 + (j // 3)
            if val in rows[i] or val in cols[j] or val in boxes[idx]:
                return False
            rows[i].add(val)
            cols[j].add(val)
            boxes[idx].add(val)
    return True

# Problem 7: Common characters in all strings
def common_characters(words):
    if not words:
        return []
    common = set(words[0])
    for w in words[1:]:
        common &= set(w)
    return sorted(common)

# Problem 8: Group anagrams
def group_anagrams(words):
    groups = defaultdict(list)
    for w in words:
        key = ''.join(sorted(w))
        groups[key].append(w)
    return list(groups.values())

# Problem 9: Contains nearby duplicate III (naive set window approach)
def contains_nearby_duplicate(nums, k, t):
    if k < 1 or t < 0:
        return False
    window = set()
    for i, val in enumerate(nums):
        if i > k:
            window.remove(nums[i - k - 1])
        # naive scan inside window; for large window this is O(k) per iteration
        for w in window:
            if abs(val - w) <= t:
                return True
        window.add(val)
    return False

# Problem 10: Unique email addresses normalization
def num_unique_emails(emails):
    unique = set()
    for e in emails:
        local, domain = e.split('@')
        local = local.split('+')[0].replace('.', '')
        unique.add(f"{local}@{domain}")
    return len(unique)

# ---------------------------
# 8. CONDITIONAL STATEMENTS & OPERATOR EXAMPLES (many cases)
# ---------------------------

# Demonstrate various conditional forms related to sets

def classify_set(s):
    # s expected to be a set
    if s is None:                  # identity check
        return "no set"
    if not isinstance(s, set):     # type check
        return "not a set"
    if not s:                      # emptiness (falsy)
        return "empty set"
    # size-based branching
    size = len(s)
    if size == 1:
        return "singleton"
    elif 2 <= size <= 5:           # chained comparison via and
        return "small set"
    elif size > 5:
        return "large set"
    else:
        return "unknown size"

def membership_cases(x, s):
    # membership and not-in combined
    if x in s:
        return "present"
    elif x not in s:
        return "absent"
    else:
        return "impossible"  # logically unreachable but shown for completeness

def nested_condition_example(user):
    # nested conditions deciding access based on groups (illustrates real-world logic)
    if not user or 'active' not in user or not user['active']:
        return "inactive"
    role = user.get('role', 'guest')
    groups = user.get('groups', [])
    # nested and combined conditions
    if role == 'admin':
        if 'super' in groups and user.get('age', 0) >= 21:
            return "super admin"
        elif 'admin' in groups:
            return "admin"
        else:
            return "admin-limited"
    elif role == 'member':
        if 'beta' in groups or user.get('contribs', 0) > 10:
            return "privileged member"
        else:
            return "regular member"
    else:
        # ternary operator inside return
        return "guest" if 'public' in groups else "no access"

# Short-circuit examples with sets
def short_circuit_example(a_callable, b_callable):
    # If a_callable() returns falsy, b_callable() is not called
    if a_callable() and b_callable():
        return True
    return False

# Examples of bitwise, membership, logical operators in a single function
def set_operator_examples(s1, s2):
    """
    Demonstrates:
    - membership: in
    - logical: and/or/not
    - identity: is
    - bitwise set ops: | & ^ - are implemented as operators for sets
    """
    res = {}
    res['s1_has_three'] = 3 in s1
    res['s1_is_s2'] = (s1 is s2)
    res['union'] = s1 | s2
    res['intersection'] = s1 & s2
    res['symmetric'] = s1 ^ s2
    res['difference'] = s1 - s2
    return res

# ---------------------------
# 9. TIME COMPLEXITY SUMMARY (comment block)
# ---------------------------

"""
For sets (average cases):
- add/remove/membership: O(1) average, O(n) worst if hash collisions
- union/intersection/difference: O(len(s) + len(t)) typically
- iteration: O(n)
- copy: O(n)
Space: O(n)
"""

# ---------------------------
# 10. GOTCHAS & SAFE PATTERNS
# ---------------------------

# Gotcha: {} is dict not set
empty_set = set()
empty_dict = {}

# Gotcha: unhashable elements
try:
    invalid = {[1,2], 3}  # will raise TypeError
except TypeError as e:
    # print("Unhashable element error:", e)
    pass

# Gotcha: do not modify a set while iterating
my_set = {1, 2, 3, 4}
try:
    for item in my_set:
        my_set.remove(item)  # unsafe; may raise RuntimeError
except RuntimeError:
    # safe modification pattern: iterate over a copy or collect removals
    my_set = {1, 2, 3, 4}
    to_remove = {1, 2}
    my_set.difference_update(to_remove)  # safe in-place removal

# ---------------------------
# 11. DEMO / QUICK TESTS
# ---------------------------

if __name__ == "__main__":
    print("Fruits set:", fruits)
    print("Mixed set:", mixed_set)
    print("Set creation examples:", set1, set2, set3, set4, set5)
    print("Union A|B:", union_op)
    print("Intersection A&B:", intersection_op)
    print("Difference A-B:", difference_op)
    print("Symmetric difference A^B:", sym_diff_op)
    print("Complex set:", complex_set)
    print("Flat set from matrix:", flat_set)
    print(f"Membership speedup approx: {speedup:.2f}x faster (list_time={list_time:.6f}, set_time={set_time:.6f})")
    print("Pairs summing to 6:", find_pairs_with_sum([1,5,7,-1,5,3,6,2,4], 6))
    print("Intersection with duplicates:", intersection_with_duplicates([1,2,2,1],[2,2]))
    print("Longest consecutive sequence:", longest_consecutive_sequence([100,4,200,1,3,2]))
    print("Missing number example:", find_missing_number([1,2,4,5,6]))
    print("Duplicates example:", find_duplicates([4,3,2,7,8,2,3,1]))
    print("Valid sudoku:", is_valid_sudoku([
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]))
    print("Common characters:", common_characters(["bella","label","roller"]))
    print("Group anagrams:", group_anagrams(["eat","tea","tan","ate","nat","bat"]))
    print("Contains nearby duplicate (example):", contains_nearby_duplicate([1,5,9,1,5,9], 2, 3))
    print("Unique emails count:", num_unique_emails([
        "test.email+alex@leetcode.com",
        "test.e.mail+bob.cathy@leetcode.com",
        "testemail+david@lee.tcode.com"
    ]))
    print("Classify set:", classify_set({1,2,3}))
    print("Nested condition example:", nested_condition_example({'active': True, 'role': 'admin', 'groups': ['super'], 'age': 25}))