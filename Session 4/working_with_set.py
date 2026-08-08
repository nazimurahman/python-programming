# 1. SET BASICS - Understanding the fundamentals

"""
KEY PROPERTIES OF SETS:
- Unordered collection (no indexing)
- Mutable (can add/remove elements)
- No duplicate elements allowed
- Elements must be hashable (immutable)
- Efficient for membership testing (O(1))
"""

# Empty set (Notice: {} creates dict, not set!)
empty_set = set()                    # Correct way
empty_dict = {}                      # This is a dictionary
print(f"Empty set: {empty_set}")     # set()
print(f"Empty dict: {empty_dict}")   # {}

# Set with elements
fruits = {'apple', 'banana', 'orange', 'apple'}  # Duplicate removed
print(f"Fruits: {fruits}")           # {'apple', 'banana', 'orange'}

# Set with mixed data types (all hashable)
mixed_set = {1, 'hello', 3.14, (1, 2)}  # Tuple is hashable
# mixed_set = {1, 'hello', [1, 2]}     # Error! List is not hashable

# Type checking
print(f"Type of set: {type(fruits)}")  # <class 'set'>


# ============================================================
# 2. SET CREATION METHODS

# Method 1: Using curly braces
set1 = {1, 2, 3, 4, 5}
print(f"Method 1: {set1}")

# Method 2: Using set() constructor
set2 = set([1, 2, 3, 4, 5])           # From list
set3 = set((1, 2, 3, 4, 5))           # From tuple
set4 = set(range(1, 6))               # From range
set5 = set('hello')                   # From string (creates {'h','e','l','o'})
print(f"From list: {set2}")
print(f"From tuple: {set3}")
print(f"From range: {set4}")
print(f"From string: {set5}")

# Method 3: Set comprehension
squares = {x**2 for x in range(1, 6)}
even_numbers = {x for x in range(10) if x % 2 == 0}
print(f"Set comprehension (squares): {squares}")
print(f"Set comprehension (even): {even_numbers}")

# Method 4: From dictionary keys
dict_data = {'a': 1, 'b': 2, 'c': 3}
set_from_dict = set(dict_data)
print(f"From dict keys: {set_from_dict}")

# Method 5: From set of tuples
tuple_set = {('a', 1), ('b', 2), ('c', 3)}
print(f"Set of tuples: {tuple_set}")

# ============================================================
# 3. SET OPERATIONS - Mathematical Set Operations
# ============================================================

# Sample sets for operations
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
C = {1, 2, 3}

# ---------- UNION (|) ----------
# Returns all elements from both sets (combines)
union_operator = A | B                # Using operator
union_method = A.union(B)             # Using method
print(f"Union (A | B): {union_operator}")        # {1,2,3,4,5,6,7,8}
print(f"Union (method): {union_method}")         # {1,2,3,4,5,6,7,8}

# Multiple union
multi_union = A.union(B, {9, 10}, {11, 12})
print(f"Multiple union: {multi_union}")

# ---------- INTERSECTION (&) ----------
# Returns elements common to both sets
intersection_operator = A & B         # Using operator
intersection_method = A.intersection(B)  # Using method
print(f"Intersection (A & B): {intersection_operator}")  # {4,5}

# Multiple intersection
multi_intersection = A.intersection(B, {4, 5, 9})
print(f"Multiple intersection: {multi_intersection}")    # {4,5}

# ---------- DIFFERENCE (-) ----------
# Returns elements in first set but not in second
difference_operator = A - B           # Using operator
difference_method = A.difference(B)   # Using method
print(f"Difference (A - B): {difference_operator}")      # {1,2,3}

# Symmetric difference (B - A)
sym_diff_operator = B - A
print(f"Difference (B - A): {sym_diff_operator}")        # {6,7,8}

# ---------- SYMMETRIC DIFFERENCE (^) ----------
# Returns elements in either set but not in both
sym_diff_operator = A ^ B             # Using operator
sym_diff_method = A.symmetric_difference(B)  # Using method
print(f"Symmetric diff (A ^ B): {sym_diff_operator}")   # {1,2,3,6,7,8}



# ============================================================
# 4. BUILT-IN METHODS - Complete List
# ============================================================

# Sample set for method demonstrations
numbers = {1, 2, 3, 4, 5, 6}
print(f"Original set: {numbers}")

# ---------- ADDING ELEMENTS ----------
# add() - Adds a single element
numbers.add(7)
print(f"After add(7): {numbers}")        # {1,2,3,4,5,6,7}

# update() - Adds multiple elements (accepts any iterable)
numbers.update({8, 9})                   # Add from set
numbers.update([10, 11])                 # Add from list
numbers.update((12, 13))                 # Add from tuple
numbers.update('14')                     # Add from string (adds '1','4')
print(f"After update(): {numbers}")

# ---------- REMOVING ELEMENTS ----------
# remove() - Removes element, raises KeyError if not found
numbers.remove(13)
print(f"After remove(13): {numbers}")

# discard() - Removes element, no error if not found
numbers.discard(100)                     # No error
numbers.discard(12)
print(f"After discard(): {numbers}")

# pop() - Removes and returns arbitrary element
popped = numbers.pop()                    # Removes random element
print(f"Popped element: {popped}")
print(f"After pop(): {numbers}")

# clear() - Removes all elements
temp_set = {1, 2, 3}
temp_set.clear()
print(f"After clear(): {temp_set}")      # set()

# ---------- MEMBERSHIP & COMPARISON ----------
# in operator - Check membership
print(f"Is 5 in numbers? {5 in numbers}")        # True/False
print(f"Is 100 in numbers? {100 in numbers}")    # False

# not in operator
print(f"Is 7 not in numbers? {7 not in numbers}")

# ---------- COPYING SETS ----------
# copy() - Creates a shallow copy
original = {1, 2, 3}
copied = original.copy()
copied.add(4)
print(f"Original: {original}")          # {1,2,3}
print(f"Copied: {copied}")              # {1,2,3,4}

# ---------- SET COMPARISON METHODS ----------
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
set3 = {1, 2, 3}
set4 = {4, 5, 6}

# issubset() - Check if all elements are in another set
print(f"set1 subset of set2? {set1.issubset(set2)}")     # True
print(f"set1 subset of set3? {set1.issubset(set3)}")     # True

# issuperset() - Check if contains all elements of another set
print(f"set2 superset of set1? {set2.issuperset(set1)}") # True
print(f"set1 superset of set2? {set1.issuperset(set2)}") # False

# isdisjoint() - Check if no common elements
print(f"set1 and set4 disjoint? {set1.isdisjoint(set4)}") # True
print(f"set1 and set2 disjoint? {set1.isdisjoint(set2)}") # False

# ---------- UPDATE METHODS (In-place operations) ----------
a = {1, 2, 3}
b = {3, 4, 5}

# difference_update() - Removes elements found in another set
a.difference_update(b)
print(f"After difference_update: {a}")    # {1,2}

# intersection_update() - Keeps only common elements
a = {1, 2, 3}
a.intersection_update(b)
print(f"After intersection_update: {a}")  # {3}

# symmetric_difference_update() - Keeps elements not in both
a = {1, 2, 3}
a.symmetric_difference_update(b)
print(f"After symmetric_difference_update: {a}")  # {1,2,4,5}

# update() - Adds all elements from another set
a = {1, 2}
a.update({3, 4})
print(f"After update: {a}")               # {1,2,3,4}


# ============================================================
# 5. ADVANCED SET OPERATIONS
# ============================================================

# ---------- SETS WITH NESTED STRUCTURES ----------
# Sets can contain tuples (immutable)
coordinates = {(1, 2), (3, 4), (5, 6)}
coordinates.add((7, 8))
print(f"Coordinates set: {coordinates}")

# frozenset - Immutable set (hashable, can be used as dict key)
frozen = frozenset([1, 2, 3, 4])
set_with_frozenset = {frozen, (5, 6)}
print(f"Set with frozenset: {set_with_frozenset}")

# ---------- SET OPERATIONS ON LARGE DATA ----------
# Using sets for efficient data processing

# Remove duplicates from list
list_with_duplicates = [1, 2, 2, 3, 3, 4, 5, 5]
unique_list = list(set(list_with_duplicates))
print(f"Unique list: {unique_list}")

# Find common elements in multiple lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
list3 = [3, 4, 5, 9, 10]

common = set(list1) & set(list2) & set(list3)
print(f"Common elements: {common}")      # {4,5}

# Find elements unique to each list
set1 = set(list1)
set2 = set(list2)
set3 = set(list3)

unique_to_set1 = set1 - set2 - set3
unique_to_set2 = set2 - set1 - set3
unique_to_set3 = set3 - set1 - set2
print(f"Unique to list1: {unique_to_set1}")    # {1,2}
print(f"Unique to list2: {unique_to_set2}")    # {6,7,8}
print(f"Unique to list3: {unique_to_set3}")    # {9,10}

# ---------- SET COMPREHENSION WITH CONDITIONAL ----------
# Complex set comprehension
numbers = range(20)
complex_set = {x for x in numbers 
               if x % 2 == 0 
               and x % 3 == 0 
               and x > 0}
print(f"Complex set comprehension: {complex_set}")  # {6,12,18}

# Nested set comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_set = {num for row in matrix for num in row}
print(f"Flattened matrix to set: {flat_set}")

# ---------- WORKING WITH STRINGS ----------
text = "hello world"
vowels = {'a', 'e', 'i', 'o', 'u'}
text_set = set(text)
vowels_in_text = text_set & vowels
consonants_in_text = text_set - vowels - {' '}
print(f"Vowels in text: {vowels_in_text}")
print(f"Consonants in text: {consonants_in_text}")

# ---------- PERFORMANCE COMPARISON ----------
import time

# List vs Set membership testing
big_list = list(range(1000000))
big_set = set(range(1000000))

# Test list membership
start = time.time()
result = 999999 in big_list
list_time = time.time() - start

# Test set membership
start = time.time()
result = 999999 in big_set
set_time = time.time() - start

print(f"List membership time: {list_time:.6f} seconds")
print(f"Set membership time: {set_time:.6f} seconds")
print(f"Set is {list_time/set_time:.2f}x faster!")


# ============================================================
# 6. INTERVIEW PROBLEMS WITH SOLUTIONS
# ============================================================

# PROBLEM 1: Find all pairs with given sum
def find_pairs_with_sum(arr, target_sum):
    """
    Find all unique pairs that sum to target
    Time: O(n), Space: O(n)
    """
    seen = set()
    pairs = set()
    
    for num in arr:
        complement = target_sum - num
        if complement in seen:
            # Use tuple of (min, max) to avoid duplicates
            pairs.add(tuple(sorted((num, complement))))
        seen.add(num)
    
    return pairs

# Test
arr = [1, 5, 7, -1, 5, 3, 6, 2, 4]
target = 6
print(f"Problem 1 - Pairs summing to {target}: {find_pairs_with_sum(arr, target)}")
# Output: {(1,5), (2,4), (3,3)} but 3,3 not in input, so {(1,5), (2,4)}

# PROBLEM 2: Find intersection of two arrays (including duplicates)
def intersection_with_duplicates(arr1, arr2):
    """
    Find intersection including duplicates
    Using sets and counters
    """
    from collections import Counter
    
    count1 = Counter(arr1)
    count2 = Counter(arr2)
    
    result = []
    for num in count1:
        if num in count2:
            result.extend([num] * min(count1[num], count2[num]))
    
    return result

arr1 = [1, 2, 2, 1]
arr2 = [2, 2]
print(f"Problem 2 - Intersection with duplicates: {intersection_with_duplicates(arr1, arr2)}")

# PROBLEM 3: Find longest consecutive sequence
def longest_consecutive_sequence(nums):
    """
    Find longest consecutive sequence length
    Time: O(n), Space: O(n)
    """
    if not nums:
        return 0
    
    num_set = set(nums)
    longest = 0
    
    for num in num_set:
        # Check if this is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            
            # Count consecutive numbers
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            
            longest = max(longest, current_streak)
    
    return longest

nums = [100, 4, 200, 1, 3, 2]
print(f"Problem 3 - Longest consecutive sequence: {longest_consecutive_sequence(nums)}")  # 4

# PROBLEM 4: Find missing number
def find_missing_number(nums):
    """
    Find missing number in array 1 to n
    Using set for O(n) solution
    """
    n = len(nums)
    full_set = set(range(1, n + 2))  # 1 to n+1
    num_set = set(nums)
    missing = full_set - num_set
    return missing.pop()

nums = [1, 2, 4, 5, 6]
print(f"Problem 4 - Missing number: {find_missing_number(nums)}")  # 3

# PROBLEM 5: Find duplicates in array
def find_duplicates(nums):
    """
    Find all duplicates using set
    Time: O(n), Space: O(n)
    """
    seen = set()
    duplicates = set()
    
    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    
    return list(duplicates)

nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(f"Problem 5 - Duplicates: {find_duplicates(nums)}")  # [2,3]

# PROBLEM 6: Valid Sudoku
def is_valid_sudoku(board):
    """
    Check if Sudoku board is valid
    Using sets for rows, columns, and boxes
    """
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                continue
            
            num = board[i][j]
            box_index = (i // 3) * 3 + (j // 3)
            
            # Check duplicates
            if num in rows[i] or num in cols[j] or num in boxes[box_index]:
                return False
            
            rows[i].add(num)
            cols[j].add(num)
            boxes[box_index].add(num)
    
    return True

# Test Sudoku board
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
print(f"Problem 6 - Valid Sudoku: {is_valid_sudoku(board)}")  # True

# PROBLEM 7: Find common characters
def common_characters(words):
    """
    Find characters that appear in all strings
    """
    if not words:
        return []
    
    # Start with characters from first word
    common = set(words[0])
    
    # Intersect with each subsequent word
    for word in words[1:]:
        common &= set(word)
    
    return sorted(list(common))

words = ["bella", "label", "roller"]
print(f"Problem 7 - Common characters: {common_characters(words)}")  # ['e','l']

# PROBLEM 8: Group anagrams
def group_anagrams(words):
    """
    Group words that are anagrams
    Using frozenset and sorted strings
    """
    from collections import defaultdict
    
    anagram_groups = defaultdict(list)
    
    for word in words:
        # Sort string to get key
        key = ''.join(sorted(word))
        anagram_groups[key].append(word)
    
    return list(anagram_groups.values())

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(f"Problem 8 - Group anagrams: {group_anagrams(words)}")
# Output: [['eat','tea','ate'], ['tan','nat'], ['bat']]

# PROBLEM 9: Contains duplicate III
def contains_nearby_duplicate(nums, k, t):
    """
    Check if there are two distinct indices i and j
    such that abs(nums[i] - nums[j]) <= t and abs(i - j) <= k
    Using sliding window with set
    """
    if k < 1 or t < 0:
        return False
    
    window = set()
    
    for i in range(len(nums)):
        # Remove element outside window
        if i > k:
            window.remove(nums[i - k - 1])
        
        # Check if any element within t range exists
        for num in window:
            if abs(nums[i] - num) <= t:
                return True
        
        window.add(nums[i])
    
    return False

nums = [1, 5, 9, 1, 5, 9]
k, t = 2, 3
print(f"Problem 9 - Contains nearby duplicate: {contains_nearby_duplicate(nums, k, t)}")  # True

# PROBLEM 10: Find unique email addresses
def num_unique_emails(emails):
    """
    Count unique email addresses
    Rules: 
    - '.' is ignored
    - Everything after '+' is ignored (for local part)
    """
    unique_emails = set()
    
    for email in emails:
        local, domain = email.split('@')
        
        # Remove '.' and everything after '+'
        local = local.split('+')[0]
        local = local.replace('.', '')
        
        unique_emails.add(f"{local}@{domain}")
    
    return len(unique_emails)

emails = [
    "test.email+alex@leetcode.com",
    "test.e.mail+bob.cathy@leetcode.com",
    "testemail+david@lee.tcode.com"
]
print(f"Problem 10 - Unique emails: {num_unique_emails(emails)}")  # 2




# ============================================================
# 7. TIME COMPLEXITY SUMMARY
# ============================================================

"""
OPERATION                    AVERAGE CASE    WORST CASE
============================================================
Add element                 O(1)            O(n)
Remove element              O(1)            O(n)
Membership (in)             O(1)            O(n)
Union (|)                   O(len(s) + len(t))  O(len(s) + len(t))
Intersection (&)            O(min(len(s), len(t)))  O(len(s) * len(t))
Difference (-)              O(len(s))       O(len(s))
Symmetric Difference (^)    O(len(s) + len(t))  O(len(s) + len(t))
Copy                        O(n)            O(n)
Iteration                   O(n)            O(n)
Length (len)                O(1)            O(1)

SPACE COMPLEXITY: O(n) where n is number of elements
"""

# Performance tips:
def performance_tips():
    """
    1. Use sets for membership testing instead of lists
    2. Use set operations instead of loops for common operations
    3. Use frozenset when you need hashable set
    4. Use set comprehension for concise code
    5. Be aware that sets are unordered
    """
    pass



# ============================================================
# QUICK REFERENCE CARD FOR INTERVIEWS
# ============================================================

# 1. Create set
my_set = {1, 2, 3}                    # Direct
my_set = set([1, 2, 3])               # From list
my_set = set()                        # Empty set

# 2. Add/Remove
my_set.add(4)                         # Add single
my_set.update([5, 6, 7])              # Add multiple
my_set.remove(3)                      # Remove (raises error if missing)
my_set.discard(10)                    # Remove (no error if missing)
my_set.pop()                          # Remove arbitrary

# 3. Set Operations
A | B                                 # Union
A & B                                 # Intersection
A - B                                 # Difference
A ^ B                                 # Symmetric Difference
A.union(B, C)                         # Multiple union
A.intersection(B, C)                  # Multiple intersection

# 4. Membership
if item in my_set:                    # O(1) check
    pass

# 5. Comparison
A.issubset(B)                         # A ⊆ B
A.issuperset(B)                       # A ⊇ B
A.isdisjoint(B)                       # A ∩ B = ∅

# 6. Common Interview Patterns
# Remove duplicates: list(set(arr))
# Find intersection: set1 & set2
# Find difference: set1 - set2
# Check uniqueness: len(set(arr)) == len(arr)
# Find common in multiple: set1 & set2 & set3


# Gotcha 1: Empty set vs empty dict
empty_set = set()        # Correct
empty_dict = {}          # This is dict, not set!

# Gotcha 2: Sets don't preserve order
ordered = {1, 2, 3}
print(ordered)           # May print {1,2,3} but not guaranteed

# Gotcha 3: Unhashable types can't be in sets
try:
    invalid_set = {[1, 2], [3, 4]}  # TypeError!
except TypeError as e:
    print(f"Error: {e}")

# Gotcha 4: Modifying set during iteration
my_set = {1, 2, 3, 4}
try:
    for item in my_set:
        my_set.remove(item)         # RuntimeError!
except RuntimeError as e:
    print(f"Error: {e}")
    
# Correct way to modify during iteration
my_set = {1, 2, 3, 4}
to_remove = {1, 2}
my_set.difference_update(to_remove)  # Safe way
print(f"Safe removal: {my_set}")



