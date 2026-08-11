# dictionary_conditionals_demo.py
# Cleaned dictionary examples + exhaustive conditional-operator demos with inline comments.

# ----------------------------
# 1. Creating dictionaries
# ----------------------------

# Method 1: literal syntax with curly braces
empty_dict = {}                                 # empty_dict: variable assigned to empty dict literal {}
student = {"name": "John", "age": 25, "grade": "A"}  # dict with string keys and mixed values

# Method 2: dict() constructor with keyword arguments
student2 = dict(name="Alice", age=22, grade="B")  # dict() builds dict from named args

# Method 2b: dict() from list of (key, value) pairs
student3 = dict([("name", "Bob"), ("age", 23), ("grade", "C")])  # list of tuples -> dict

# Method 3: fromkeys() to create dict with same default value for many keys
keys = ["name", "age", "grade"]                     # keys: list of strings to use as keys
default_student = dict.fromkeys(keys, None)         # fromkeys: creates dict with each key -> None

# ----------------------------
# 2. Accessing elements
# ----------------------------

student = {"name": "John", "age": 25, "grade": "A", "courses": ["Math", "Science"]}

# Direct indexing (raises KeyError if key missing)
name_value = student["name"]                        # ["name"]: index operator, fetch value for key "name"

# Safe access using get() (returns None or default if key missing)
age_value = student.get("age")                      # get(): returns value or None if key absent
city_value = student.get("city", "Unknown")         # second arg is default if key not present

# Views: keys, values, items (dynamic, not static lists)
keys_view = student.keys()                          # keys(): returns dict_keys view object
values_view = student.values()                      # values(): returns dict_values view
items_view = student.items()                        # items(): returns dict_items of (key, value) pairs

# Convert views to lists if you need a real list
keys_list = list(student.keys())                    # list(): casts view to list

# ----------------------------
# 3. Adding and updating elements
# ----------------------------

student = {"name": "John", "age": 25}

# Direct assignment: add or update
student["grade"] = "A"                              # adds new key "grade" with value "A"
student["age"] = 26                                 # updates existing key "age" to 26

# update(): merge another dict or iterable of pairs
student.update({"city": "New York", "grade": "B"})  # merges dict; existing keys overwritten
student.update([("major", "CS"), ("year", 2023)])   # merges list of (key, value) pairs

# setdefault(): get value if exists, else set and return default
email_value = student.setdefault("email", "john@email.com")  # adds "email" if missing
age_default = student.setdefault("age", 30)         # does nothing because "age" already exists

# Merge using | operator (Python 3.9+)
student = student | {"phone": "123456", "age": 27}  # | creates new dict with right side overriding

# ----------------------------
# 4. Removing elements
# ----------------------------

student = {"name": "John", "age": 25, "grade": "A", "city": "NYC"}

# pop(key[, default]): remove key and return its value; default avoids KeyError
age_removed = student.pop("age")                    # pop(): removes "age" and returns 25
age_missing = student.pop("age", None)              # returns None if key not present

# popitem(): remove and return last inserted (key, value) pair (LIFO)
last_pair = student.popitem()                       # returns ('city', 'NYC') and removes it

# del statement: delete a key (raises KeyError if missing)
del student["grade"]                                # del: removes key "grade" from dict

# clear(): remove all items
student.clear()                                     # clear(): empties dict to {}

# Comprehension to delete multiple keys
student = {"name": "John", "age": 25, "grade": "A", "city": "NYC", "course": "Math"}
keys_to_delete = ["age", "city"]                    # list of keys we want to remove
student = {k: v for k, v in student.items()         # dict comprehension: rebuild dict
           if k not in keys_to_delete}              # if: condition to keep only wanted keys

# ----------------------------
# 5. Iteration over dictionaries
# ----------------------------

student = {"name": "John", "age": 25, "grade": "A"}

# Iterate over keys (default iteration)
for key in student:                                 # for: loop over each key in dict
    print(key, student[key])                        # access value via student[key]

# Iterate over key-value pairs using items()
for key, value in student.items():                  # items(): yields (key, value) tuples
    print(key, value)                               # unpack into key and value variables

# Iterate over keys explicitly
for key in student.keys():                          # keys(): explicit key iteration
    print(key)

# Iterate over values only
for value in student.values():                      # values(): yields only values
    print(value)

# Comprehension examples
upper_cased = {k.upper(): v for k, v in student.items()}  # upper(): makes keys uppercase
filtered = {k: v for k, v in student.items()              # filtered dict
            if isinstance(v, int)}                        # isinstance(): type check for int

# ----------------------------
# 6. Dictionary comprehensions and operations
# ----------------------------

keys = ["name", "age", "grade"]
values = ["John", 25, "A"]
student = {k: v for k, v in zip(keys, values)}      # zip(): pairs keys and values; comprehension builds dict

numbers = {x: x**2 for x in range(1, 6)}            # ** : exponent; range(1,6): 1..5
even_squares = {x: x**2 for x in range(1, 11)       # conditional comprehension
                if x % 2 == 0}                      # % : modulus; if filters even numbers

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = dict1 | dict2                              # | : merge dicts (3.9+), right overrides left
merged2 = {**dict1, **dict2}                        # ** unpacking: alternative merge

# Counter example (from collections)
from collections import Counter                     # import: load Counter class
text = "hello world"
char_count = Counter(text)                          # Counter: counts each character

# ----------------------------
# 7. All dict methods demonstrated with conditionals
# ----------------------------

student = {"name": "John", "age": 25, "grade": "A"}

# 1. clear()
student_copy = student.copy()                       # copy(): shallow copy of dict
student_copy.clear()                                # clear(): removes all items

# 2. copy()
original = {"name": "John", "age": 25}
copy_dict = original.copy()                         # copy(): new dict object, same contents

# 3. fromkeys()
keys = ["name", "age", "grade"]
new_dict = dict.fromkeys(keys, "Unknown")           # fromkeys(): keys -> "Unknown"

# 4. get()
value = student.get("name", "Not found")            # get(): safe access with default

# 5. items()
items_view = student.items()                        # items(): dynamic view of (key, value)

# 6. keys()
keys_view = student.keys()                          # keys(): dynamic view of keys

# 7. values()
values_view = student.values()                      # values(): dynamic view of values

# 8. pop()
removed = student.pop("age", None)                  # pop(): remove key, return value or default

# 9. popitem()
if student:                                         # if: truthy check (non-empty dict)
    last_pair = student.popitem()                   # popitem(): remove last inserted pair

# 10. setdefault()
value = student.setdefault("phone", "12345")        # setdefault(): get or set default

# 11. update()
student.update({"city": "NYC", "grade": "B"})       # update(): merge dict into existing

# 12. | operator (3.9+)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = dict1 | dict2                              # | : merge, right overrides left

# 13. |= in-place merge
dict1 |= dict2                                      # |= : in-place merge (dict1 updated)

# ----------------------------
# 8. Nested dictionaries and safe access
# ----------------------------

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

# Direct nested access (can raise KeyError if path invalid)
math_grade = nested_dict["student1"]["grades"]["math"]  # chain of [] indexing

# Safe nested access function using conditionals
def safe_get(d, keys):
    """Safely access nested dictionary keys using a list of keys."""
    for key in keys:                              # for: iterate over each key in path
        if isinstance(d, dict) and key in d:      # isinstance(): type check; in: membership
            d = d[key]                            # descend one level
        else:
            return None                           # return None if path breaks
    return d

math_grade_safe = safe_get(nested_dict, ["student1", "grades", "math"])

# ----------------------------
# 9. Sorting, min/max, and switch-like dict
# ----------------------------

student_ages = {"John": 25, "Alice": 22, "Bob": 23, "Charlie": 24}

# Sort by keys
sorted_by_keys = dict(sorted(student_ages.items()))           # sorted(): returns list of sorted pairs
sorted_by_keys_desc = dict(sorted(student_ages.items(),
                                    reverse=True))            # reverse=True: descending order

# Sort by values using lambda
sorted_by_values = dict(sorted(student_ages.items(),
                               key=lambda x: x[1]))           # lambda: anonymous function; x[1]: value
sorted_by_values_desc = dict(sorted(student_ages.items(),
                                    key=lambda x: x[1],
                                    reverse=True))

# Max/min by value using dict.get as key function
max_age_student = max(student_ages, key=student_ages.get)     # max(): key with highest value
min_age_student = min(student_ages, key=student_ages.get)     # min(): key with lowest value

# Dictionary as switch (operation lookup)
def switch_case(operation):
    """Return a function based on operation name using dict lookup."""
    operations = {
        "add": lambda x, y: x + y,                # lambda: anonymous function for addition
        "subtract": lambda x, y: x - y,           # subtraction
        "multiply": lambda x, y: x * y,           # multiplication
        "divide": lambda x, y: x / y if y != 0 else "Error: Division by zero"  # conditional expr
    }
    return operations.get(operation,              # get(): fetch function or default
                          lambda x, y: "Invalid operation")

# ----------------------------
# 10. Inverting dictionaries (with and without duplicates)
# ----------------------------

original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}  # simple inversion (values must be unique)

# Handling duplicate values during inversion
original_dup = {"a": 1, "b": 2, "c": 1}
inverted_dup = {}
for k, v in original_dup.items():               # for: iterate over (key, value) pairs
    if v not in inverted_dup:                   # if: check if value already a key
        inverted_dup[v] = []                    # create list for this value
    inverted_dup[v].append(k)                   # append original key to list

# ----------------------------
# 11. Error handling with dictionaries
# ----------------------------

student = {"name": "John", "age": 25}

# KeyError handling with try/except
try:
    grade = student["grade"]                    # may raise KeyError
except KeyError:
    grade = "Not available"                     # fallback value

# Using get() to avoid errors
grade = student.get("grade", "Not available")   # safe access, no exception

# Safe nested get with try/except
def safe_nested_get(d, keys, default=None):
    """Safely access nested dict with try/except."""
    try:
        for key in keys:                        # for: walk through key path
            d = d[key]                          # descend
        return d
    except (KeyError, TypeError):               # except: catch missing key or non-dict
        return default

# Existence check using 'in'
if "name" in student:                           # in: membership test for keys
    print(student["name"])

# EAFP pattern (try first, handle later)
try:
    student["grade"] = student["age"] * 2       # may fail if "age" missing
except KeyError:
    pass                                        # pass: do nothing on error

# ----------------------------
# 12. Interview-style patterns with conditionals
# ----------------------------

# 1. Character frequency
def char_frequency(text):
    """Return dict of character frequencies."""
    freq = {}
    for char in text:                           # for: each character
        freq[char] = freq.get(char, 0) + 1      # get(): increment count
    return freq

# 2. First non-repeating character
def first_non_repeating(s):
    """Return first char that appears exactly once."""
    freq = {}
    for char in s:                              # build frequency map
        freq[char] = freq.get(char, 0) + 1
    for char in s:                              # scan in order
        if freq[char] == 1:                     # if: exactly one occurrence
            return char
    return None

# 3. Group anagrams
def group_anagrams(words):
    """Group words that are anagrams of each other."""
    from collections import defaultdict         # import inside function (allowed)
    anagrams = defaultdict(list)                # defaultdict(list): default is empty list
    for word in words:                          # for: each word
        sorted_word = ''.join(sorted(word))     # sorted(): letters sorted; join(): back to string
        anagrams[sorted_word].append(word)      # group by sorted form
    return list(anagrams.values())              # values(): list of grouped lists

# 4. Two sum using dict
def two_sum(nums, target):
    """Return indices of two numbers that add to target."""
    seen = {}
    for i, num in enumerate(nums):              # enumerate(): index, value pairs
        complement = target - num               # needed partner value
        if complement in seen:                  # if: complement already seen
            return [seen[complement], i]        # return indices
        seen[num] = i                           # store index for this number
    return []

# 5. Simple LRU cache using OrderedDict
from collections import OrderedDict

class LRUCache:
    """Least Recently Used cache with fixed capacity."""
    def __init__(self, capacity):
        self.cache = OrderedDict()              # OrderedDict: preserves insertion order
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:               # if: key missing
            return -1
        self.cache.move_to_end(key)             # move_to_end(): mark as recently used
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:                   # if: update existing
            self.cache.move_to_end(key)
        self.cache[key] = value                 # insert/update
        if len(self.cache) > self.capacity:     # if: over capacity
            self.cache.popitem(last=False)      # popitem(last=False): remove oldest

# ----------------------------
# 13. Common utility patterns
# ----------------------------

# Merge with conflict resolution (dict2 overrides dict1)
def merge_dicts(dict1, dict2):
    """Merge two dicts; dict2 values override dict1."""
    return {**dict1, **dict2}                   # ** unpacking merge

# Dict to list conversions
def dict_to_list(d):
    """Return keys, values, items as lists."""
    keys = list(d.keys())                       # list of keys
    values = list(d.values())                   # list of values
    items = list(d.items())                     # list of (key, value)
    return keys, values, items

# List to dict conversion
def list_to_dict(list1, list2=None):
    """Convert one or two lists to dict."""
    if list2:                                   # if: second list provided
        return dict(zip(list1, list2))          # zip(): pair lists
    return {i: val for i, val in enumerate(list1)}  # index -> value mapping

# Flatten nested dict
def flatten_dict(nested, parent_key='', sep='_'):
    """Flatten nested dict into single-level dict with composite keys."""
    items = {}
    for k, v in nested.items():                 # for: each key, value
        new_key = f"{parent_key}{sep}{k}" if parent_key else k  # f-string + conditional expr
        if isinstance(v, dict):                 # if: value is dict -> recurse
            items.update(flatten_dict(v, new_key, sep=sep))
        else:
            items[new_key] = v                  # base case: store value
    return items

# Deep merge of dicts
def deep_merge(dict1, dict2):
    """Recursively merge dicts; dict2 overrides dict1."""
    result = dict1.copy()                       # copy(): shallow copy
    for key, value in dict2.items():            # for: each pair in dict2
        if (key in result and
            isinstance(result[key], dict) and
            isinstance(value, dict)):           # if: both are dicts -> recurse
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value                 # else: override or add
    return result

# ----------------------------
# 14. Performance tips (with conditionals where relevant)
# ----------------------------

# Prefer comprehension over manual loop
result = {i: i**2 for i in range(1000)}         # fast dict creation

# Use get() instead of try/except for optional keys
d = {"a": 1}
value = d.get("b")                              # returns None instead of raising

# Use dict.fromkeys for initialization
keys = ["x", "y", "z"]
d_zero = dict.fromkeys(keys, 0)                 # all keys -> 0

# Use defaultdict for counting
from collections import defaultdict
items = ["a", "b", "a", "c", "b", "a"]
counts = defaultdict(int)                       # int(): default 0
for item in items:                              # for: each item
    counts[item] += 1                           # auto-created if missing

# Use Counter for fastest counting
counts_fast = Counter(items)                    # Counter: optimized counting

# ----------------------------
# 15. Interview-prep class with conditionals
# ----------------------------

class DictionaryInterviewPrep:
    """Collection of dictionary-based interview utilities."""

    @staticmethod
    def word_frequency(text):
        """Count frequency of each word in text."""
        word_count = {}
        for word in text.lower().split():       # lower(): normalize; split(): words
            word_count[word] = word_count.get(word, 0) + 1
        return word_count

    @staticmethod
    def merge_dicts_with_priority(dict1, dict2, priority='second'):
        """Merge dicts with priority ('first' or 'second')."""
        if priority == 'first':                 # if: first dict should win
            return {**dict2, **dict1}           # dict1 overrides dict2
        return {**dict1, **dict2}               # else: dict2 overrides

    @staticmethod
    def find_common_keys(*dicts):
        """Find keys present in all given dicts."""
        if not dicts:                           # if: no dicts provided
            return set()
        common = set(dicts[0].keys())           # set(): unique keys from first dict
        for d in dicts[1:]:                     # for: remaining dicts
            common &= set(d.keys())             # &= : set intersection
        return common

    @staticmethod
    def group_by_key(items, key_func):
        """Group items by a key function (e.g., len)."""
        grouped = defaultdict(list)
        for item in items:                      # for: each item
            key = key_func(item)                # call function to get key
            grouped[key].append(item)           # append to list for that key
        return dict(grouped)

    @staticmethod
    def invert_dictionary_safe(d):
        """Invert dict, grouping original keys by value."""
        inverted = defaultdict(list)
        for k, v in d.items():                  # for: each pair
            inverted[v].append(k)               # group keys by value
        return dict(inverted)

    @staticmethod
    def filter_dictionary(d, condition):
        """Filter dict by a condition function (k, v) -> bool."""
        return {k: v for k, v in d.items()      # comprehension
                if condition(k, v)}             # if: keep only if True

    @staticmethod
    def max_value_keys(d):
        """Return all keys that have the maximum value."""
        if not d:                               # if: empty dict
            return []
        max_val = max(d.values())               # max(): highest value
        return [k for k, v in d.items()         # list comprehension
                if v == max_val]                # if: keep keys with max value

    @staticmethod
    def sort_dict_by_key(d, reverse=False):
        """Sort dict by keys."""
        return dict(sorted(d.items(), reverse=reverse))

    @staticmethod
    def sort_dict_by_value(d, reverse=False):
        """Sort dict by values."""
        return dict(sorted(d.items(),
                           key=lambda x: x[1],
                           reverse=reverse))

    @staticmethod
    def get_nested_value(d, keys, default=None):
        """Safely get nested value using a list of keys."""
        current = d
        for key in keys:                        # for: walk path
            if isinstance(current, dict) and key in current:  # type + membership check
                current = current[key]
            else:
                return default                  # return default if path invalid
        return current

# Example usage when run as script
if __name__ == "__main__":
    prep = DictionaryInterviewPrep()

    # Word frequency
    text = "hello world hello python world"
    print(prep.word_frequency(text))

    # Group by length
    words = ["apple", "banana", "cat", "dog", "elephant"]
    grouped = prep.group_by_key(words, len)     # len: built-in function as key_func
    print(grouped)

    # Nested access
    data = {"user": {"profile": {"name": "John", "age": 25}}}
    print(prep.get_nested_value(data, ["user", "profile", "name"]))