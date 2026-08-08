# Dictionary Basics
# Creating Dictionaries
# Method 1: Using curly braces
empty_dict = {}
student = {"name": "John", "age": 25, "grade": "A"}

# Method 2: Using dict() constructor
student2 = dict(name="Alice", age=22, grade="B")
student3 = dict([("name", "Bob"), ("age", 23), ("grade", "C")])

# Method 3: Using fromkeys() - creates dict with keys and default values
keys = ["name", "age", "grade"]
default_student = dict.fromkeys(keys, None)  # {'name': None, 'age': None, 'grade': None}


# Accessing Elements

student = {"name": "John", "age": 25, "grade": "A", "courses": ["Math", "Science"]}

# Direct access (raises KeyError if key doesn't exist)
print(student["name"])  # Output: John

# Using get() - safe access (returns None or default if key doesn't exist)
print(student.get("age"))  # Output: 25
print(student.get("city", "Unknown"))  # Output: Unknown

# Get all keys, values, and items
keys_list = student.keys()     # dict_keys(['name', 'age', 'grade', 'courses'])
values_list = student.values() # dict_values(['John', 25, 'A', ['Math', 'Science']])
items_list = student.items()   # dict_items([('name', 'John'), ('age', 25), ...])

# Convert to list if needed
keys_as_list = list(student.keys())


# Adding and Updating Elements

student = {"name": "John", "age": 25}

# Direct assignment (adds new key or updates existing)
student["grade"] = "A"           # Add new key
student["age"] = 26              # Update existing key

# Using update() - merges another dictionary or iterable
student.update({"city": "New York", "grade": "B"})
student.update([("major", "CS"), ("year", 2023)])

# Set default value if key doesn't exist
student.setdefault("email", "john@email.com")  # Adds if not exists
student.setdefault("age", 30)  # Doesn't change as key exists

# Using | operator (Python 3.9+)
student = student | {"phone": "123456", "age": 27}  # Merges dictionaries



# Removing Elements

student = {"name": "John", "age": 25, "grade": "A", "city": "NYC"}

# pop() - remove specific key and return value
age = student.pop("age")  # Returns 25, removes key
print(age)  # 25

# popitem() - remove and return last inserted item (LIFO)
last_item = student.popitem()  # Returns ('city', 'NYC')

# del - delete key (raises KeyError if not found)
del student["grade"]

# clear() - remove all items
student.clear()  # {}

# Using comprehension to delete multiple keys
student = {"name": "John", "age": 25, "grade": "A", "city": "NYC", "course": "Math"}
keys_to_delete = ["age", "city"]
student = {k: v for k, v in student.items() if k not in keys_to_delete}


# Dictionary Iteration


student = {"name": "John", "age": 25, "grade": "A"}

# Iterating through keys
for key in student:
    print(f"{key}: {student[key]}")

# Iterating through key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")

# Iterating through keys only
for key in student.keys():
    print(key)

# Iterating through values only
for value in student.values():
    print(value)

# Iterating with comprehension
upper_cased = {k.upper(): v for k, v in student.items()}
filtered = {k: v for k, v in student.items() if isinstance(v, int)}


# Dictionary Comprehension and Operations
# Creating dictionary from two lists
keys = ["name", "age", "grade"]
values = ["John", 25, "A"]
student = {k: v for k, v in zip(keys, values)}

# Conditional comprehension
numbers = {x: x**2 for x in range(1, 6)}  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}

# Merging two dictionaries (Python 3.9+)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = dict1 | dict2  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Using ** unpacking
merged2 = {**dict1, **dict2}

# Counter dictionary
from collections import Counter
text = "hello world"
char_count = Counter(text)  # {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}


# Dictionary Methods - Complete List

# ALL DICTIONARY METHODS WITH EXAMPLES
student = {"name": "John", "age": 25, "grade": "A"}

# 1. clear() - removes all items
student.clear()

# 2. copy() - shallow copy
original = {"name": "John", "age": 25}
copy_dict = original.copy()  # Different object

# 3. fromkeys() - creates new dict from iterable
keys = ["name", "age", "grade"]
new_dict = dict.fromkeys(keys, "Unknown")

# 4. get() - safe access
value = student.get("name", "Not found")

# 5. items() - returns view of key-value pairs
items_view = student.items()

# 6. keys() - returns view of keys
keys_view = student.keys()

# 7. values() - returns view of values
values_view = student.values()

# 8. pop() - remove key and return value
removed = student.pop("age", None)

# 9. popitem() - remove and return last inserted pair
last_pair = student.popitem()

# 10. setdefault() - get value or set default
value = student.setdefault("phone", "12345")

# 11. update() - update with another dict or iterable
student.update({"city": "NYC", "grade": "B"})

# 12. | operator (Python 3.9+)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = dict1 | dict2

# 13. |= operator - in-place merge
dict1 |= dict2


# Nested Dictionaries
# Creating nested dictionary
nested_dict = {
    "student1": {
        "name": "John",
        "age": 25,
        "grades": {"math": 90, "science": 85}
    },
    "student2": {
        "name": "Alice",
        "age": 22,
        "grades": {"math": 95, "science": 88}
    }
}

# Accessing nested elements
print(nested_dict["student1"]["grades"]["math"])  # Output: 90

# Safe access in nested dict
def safe_get(d, keys):
    """Safely access nested dictionary keys"""
    for key in keys:
        if isinstance(d, dict) and key in d:
            d = d[key]
        else:
            return None
    return d

math_grade = safe_get(nested_dict, ["student1", "grades", "math"])


# Advanced Operations

# Sorting dictionaries
student = {"John": 25, "Alice": 22, "Bob": 23, "Charlie": 24}

# Sort by keys
sorted_by_keys = dict(sorted(student.items()))
sorted_by_keys_desc = dict(sorted(student.items(), reverse=True))

# Sort by values
sorted_by_values = dict(sorted(student.items(), key=lambda x: x[1]))
sorted_by_values_desc = dict(sorted(student.items(), key=lambda x: x[1], reverse=True))

# Getting max/min values
max_age_student = max(student, key=student.get)  # John
min_age_student = min(student, key=student.get)  # Alice

# Dictionary as switch statement
def switch_case(operation):
    operations = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: x / y if y != 0 else "Error: Division by zero"
    }
    return operations.get(operation, lambda x, y: "Invalid operation")

# Inverting dictionary (keys become values)
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}

# Handling duplicate values during inversion
original = {"a": 1, "b": 2, "c": 1}
inverted = {}
for k, v in original.items():
    inverted.setdefault(v, []).append(k)  # {1: ['a', 'c'], 2: ['b']}



# Memory and Performance Optimization
# Using __slots__ to reduce memory usage
class Student:
    __slots__ = ['name', 'age', 'grade']  # Reduces memory for fixed attributes
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

# But for dictionaries, use specialized dict types
from collections import defaultdict, OrderedDict

# defaultdict - handles missing keys automatically
from collections import defaultdict
word_count = defaultdict(int)
for word in ["hello", "world", "hello"]:
    word_count[word] += 1  # No KeyError

# OrderedDict (Python 3.7+ dicts are ordered by default)
from collections import OrderedDict
ordered = OrderedDict([("a", 1), ("b", 2), ("c", 3)])
ordered.move_to_end("b")  # Move b to end
ordered.move_to_end("a", last=False)  # Move a to beginning

# For large dictionaries, consider using __slots__ classes    


# Error Handling
student = {"name": "John", "age": 25}

# KeyError handling
try:
    grade = student["grade"]
except KeyError:
    print("Grade key not found")
    
# Using get() to avoid errors
grade = student.get("grade", "Not available")

# Handling nested keys safely
def safe_nested_get(d, keys, default=None):
    try:
        for key in keys:
            d = d[key]
        return d
    except (KeyError, TypeError):
        return default

# Check if key exists
if "name" in student:
    print(student["name"])

# Using EAFP (Easier to Ask for Forgiveness than Permission)
try:
    student["grade"] = student["age"] * 2
except KeyError:
    pass  # Handle gracefully



# Interview Pattern Questions
# 1. Count character frequencies
def char_frequency(text):
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return freq

# 2. Find first non-repeating character
def first_non_repeating(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    for char in s:
        if freq[char] == 1:
            return char
    return None

# 3. Group anagrams
def group_anagrams(words):
    from collections import defaultdict
    anagrams = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)
    return list(anagrams.values())

# 4. Two sum problem
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# 5. LRU Cache implementation
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
    
    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)





# Common Dictionary Patterns
# 1. Merging dictionaries with conflicting keys
def merge_dicts(dict1, dict2):
    """Merge with conflict resolution (dict2 values override dict1)"""
    return {**dict1, **dict2}

# 2. Dictionary to list conversion
def dict_to_list(d):
    keys = list(d.keys())
    values = list(d.values())
    items = list(d.items())
    return keys, values, items

# 3. List to dictionary conversion
def list_to_dict(list1, list2=None):
    if list2:
        return dict(zip(list1, list2))
    return {i: val for i, val in enumerate(list1)}

# 4. Flatten nested dictionary
def flatten_dict(nested, parent_key='', sep='_'):
    items = {}
    for k, v in nested.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_dict(v, new_key, sep=sep))
        else:
            items[new_key] = v
    return items

# 5. Deep merge dictionaries
def deep_merge(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result



# Performance Tips

# 1. Use dictionary comprehension vs manual loop (faster)
# SLOW:
result = {}
for i in range(1000):
    result[i] = i ** 2
# FAST:
result = {i: i**2 for i in range(1000)}

# 2. Use get() for lookups (faster than try/except for missing keys)
# SLOW:
try:
    value = d['key']
except KeyError:
    value = None
# FAST:
value = d.get('key')

# 3. Use dict.fromkeys() for initialization
# SLOW:
d = {k: 0 for k in keys}
# FAST:
d = dict.fromkeys(keys, 0)

# 4. Use defaultdict for default values
from collections import defaultdict
# SLOW:
d = {}
for item in items:
    if item not in d:
        d[item] = 0
    d[item] += 1
# FAST:
d = defaultdict(int)
for item in items:
    d[item] += 1

# 5. Use Counter for counting (most optimized)
from collections import Counter
# FASTEST:
counts = Counter(items)


# Complete Interview Ready Functions
class DictionaryInterviewPrep:
    """Collection of dictionary interview solutions"""
    
    @staticmethod
    def word_frequency(text):
        """Count frequency of each word in text"""
        word_count = {}
        for word in text.lower().split():
            word_count[word] = word_count.get(word, 0) + 1
        return word_count
    
    @staticmethod
    def merge_dicts_with_priority(dict1, dict2, priority='second'):
        """Merge dictionaries with priority"""
        if priority == 'first':
            return {**dict2, **dict1}
        return {**dict1, **dict2}
    
    @staticmethod
    def find_common_keys(*dicts):
        """Find keys common to all dictionaries"""
        if not dicts:
            return set()
        common = set(dicts[0].keys())
        for d in dicts[1:]:
            common &= set(d.keys())
        return common
    
    @staticmethod
    def group_by_key(items, key_func):
        """Group items by a key function"""
        grouped = defaultdict(list)
        for item in items:
            key = key_func(item)
            grouped[key].append(item)
        return dict(grouped)
    
    @staticmethod
    def invert_dictionary_safe(d):
        """Invert dictionary handling duplicate values"""
        inverted = defaultdict(list)
        for k, v in d.items():
            inverted[v].append(k)
        return dict(inverted)
    
    @staticmethod
    def filter_dictionary(d, condition):
        """Filter dictionary based on condition"""
        return {k: v for k, v in d.items() if condition(k, v)}
    
    @staticmethod
    def max_value_keys(d):
        """Find all keys with maximum value"""
        if not d:
            return []
        max_val = max(d.values())
        return [k for k, v in d.items() if v == max_val]
    
    @staticmethod
    def sort_dict_by_key(d, reverse=False):
        """Sort dictionary by keys"""
        return dict(sorted(d.items(), reverse=reverse))
    
    @staticmethod
    def sort_dict_by_value(d, reverse=False):
        """Sort dictionary by values"""
        return dict(sorted(d.items(), key=lambda x: x[1], reverse=reverse))
    
    @staticmethod
    def get_nested_value(d, keys, default=None):
        """Get nested dictionary value safely"""
        current = d
        for key in keys:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return default
        return current

# Example usage in interview:
if __name__ == "__main__":
    # Test the solutions
    prep = DictionaryInterviewPrep()
    
    # Word frequency
    text = "hello world hello python world"
    print(prep.word_frequency(text))
    # Output: {'hello': 2, 'world': 2, 'python': 1}
    
    # Group by length
    words = ["apple", "banana", "cat", "dog", "elephant"]
    grouped = prep.group_by_key(words, len)
    print(grouped)
    # Output: {5: ['apple'], 6: ['banana'], 3: ['cat', 'dog'], 8: ['elephant']}
    
    # Nested access
    data = {"user": {"profile": {"name": "John", "age": 25}}}
    print(prep.get_nested_value(data, ["user", "profile", "name"]))
    # Output: John