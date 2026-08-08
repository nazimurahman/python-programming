"""
Key concepts:
  -> The process of converting data_type of one variabel to another data_type
  -> Type conversion (type casting) = changing a value from one data type to another.
  -> Implicit conversion = Python converts automatically (safe, no data loss).
     Example: mixing int and float in arithmetic.
  -> Explicit conversion = you call a conversion function yourself (int(), float(), str(), list(), tuple(), set(), bool(), etc.).
     This can lose information (e.g., converting float to int truncates the decimal part).

NOTE:
int(x):
  -> Converts x to integer. If x is a float, int(x) truncates toward zero (does not round): int(3.99) -> 3, int(-3.99) -> -3.
  -> If x is a numeric string (possibly with + or -), it converts: int("123") -> 123.
  -> int(" 12 ") also works (leading/trailing whitespace allowed).
  -> int("3.14") raises ValueError (string must be integer-like).
  -> You can specify a base for string-to-int: int("11", 2) -> 3 (binary).

float(x):
  -> converts to floating-point. float(3) -> 3.0, float("3.14") -> 3.14, float(" -2.5 ") -> -2.5.
  -> float("1e2") -> 100.0.

str(x):
  -> Converts any object to its string representation: str(12) -> "12", str(True) -> "True", str() -> "".

bool(x):
  -> Converts to boolean. In Python, the following are False when converted to bool: False, None, 0 (any numeric zero),
     empty sequences/collections ("" , [], (), {} , set()), and custom objects defining _bool_ or _len_ returning False/0.
     Everything else is True.
     Examples: bool(0) -> False, bool(1) -> True, bool("") -> False, bool("0") -> True (non-empty string).

list(x):
  -> Creates a list from an iterable. Strings are iterables of characters: list("nazim") -> ['n','a','z','i','m'].
  -> range(n) is iterable: list(range(6)) -> .
  -> list(123) raises TypeError because int is not iterable.

tuple(x): 
  -> Similar to list(): tuple("nazim") -> ('n','a','z','i','m'); tuple() -> (1,2,3).

set(x):

  -> Creates a set from an iterable; this removes duplicates and loses ordering (sets are unordered):
     set() -> {1,2,3}, set("anna") -> {'a','n'}.
  -> Converting range or list to set works; converting non-iterables fails.

range(n):
  -> Not a converter, but used in examples to produce sequences of integers 0..n-1.

Converting between sequences and strings:
  -> ''.join(list_of_strings) converts list of strings to single string; join needs string elements: ''.join(['n','a']) -> "na".
  -> To convert list of numbers to string, map or comprehension: ''.join(str(x) for x in ) -> "12".

Converting numeric strings with decimals:
  -> To convert "3.14" -> float("3.14") works; to get int you must convert float first then int: int(float("3.14")) -> 3.

Using exception handling:
  -> Conversions can raise ValueError or TypeError. Use try/except for user input.
"""

# Implicit conversion examples
# Ex- <i>
a = 10        # int
b = 3.5       # float
result = a + b  # int + float = float (automatically converted)
# print(result, type(result))  # Output: 13.5 <class 'float'>

# Ex- <ii>
c = True      # bool
d = 5         # int
# print(c + d)  # Output: 6 (True is treated as 1)

# Ex- <iii>
e = False     # bool
f = 10        # int
# print(e + f)  # Output: 10 (False is treated as 0)



# Explicit Type Conversion (Manual)

# int() - Convert to Integer
# String to Integer
str_num = "123"
int_num = int(str_num)
# print(int_num, type(int_num))  # Output: 123 <class 'int'>

# Float to Integer (truncates decimal part)
float_num = 3.99
int_num = int(float_num)
# print(int_num)  # Output: 3 (not rounded, it truncates)

# Boolean to Integer
# print(int(True))   # Output: 1
# print(int(False))  # Output: 0

# String with decimal to Integer (will raise error)
# print(int("3.14"))  # ValueError: invalid literal for int()

# Binary string to Integer
binary_str = "1010"
# print(int(binary_str, 2))  # Output: 10 (binary to decimal)

# Hexadecimal to Integer
hex_str = "FF"
# print(int(hex_str, 16))  # Output: 255

# float() - Convert to Float

# Integer to Float
int_num = 10
float_num = float(int_num)
# print(float_num, type(float_num))  # Output: 10.0 <class 'float'>

# String to Float
str_num = "3.14"
float_num = float(str_num)
# print(float_num, type(float_num))  # Output: 3.14 <class 'float'>

# Boolean to Float
# print(float(True))   # Output: 1.0
# print(float(False))  # Output: 0.0

# String number to Float
# print(float("123"))   # Output: 123.0
# print(float("3.14"))  # Output: 3.14
# print(float("1e3"))   # Output: 1000.0 (scientific notation)


# str() - Convert to String

# Integer to String
age = 25
age_str = str(age)
# print(age_str, type(age_str))  # Output: 25 <class 'str'>

# Float to String
pi = 3.14159
pi_str = str(pi)
# print(pi_str)  # Output: 3.14159

# Boolean to String
# print(str(True))   # Output: "True"
# print(str(False))  # Output: "False"

# List to String
my_list = [1, 2, 3]
list_str = str(my_list)
# print(list_str)  # Output: "[1, 2, 3]"

# Dictionary to String
my_dict = {"name": "John", "age": 25}
dict_str = str(my_dict)
# print(dict_str)  # Output: "{'name': 'John', 'age': 25}"

# bool() - Convert to Boolean

# Integer to Boolean
# print(bool(0))      # Output: False (zero is False)
# print(bool(1))      # Output: True (non-zero is True)
# print(bool(-5))     # Output: True
# print(bool(3.14))   # Output: True

# String to Boolean
# print(bool(""))     # Output: False (empty string)
# print(bool("Hello")) # Output: True (non-empty string)
# print(bool("0"))    # Output: True (non-empty string)
# print(bool("False")) # Output: True (non-empty string)

# List to Boolean
# print(bool([]))     # Output: False (empty list)
# print(bool([1, 2])) # Output: True (non-empty list)

# None to Boolean
# print(bool(None))   # Output: False


# list() - Convert to List

# String to List (each character becomes an element)
name = "nazim"
name_list = list(name)
# print(name_list)  # Output: ['n', 'a', 'z', 'i', 'm']

# Tuple to List
my_tuple = (1, 2, 3, 4, 5)
tuple_to_list = list(my_tuple)
# print(tuple_to_list)  # Output: [1, 2, 3, 4, 5]

# Set to List
my_set = {1, 2, 3, 4, 5}
set_to_list = list(my_set)
# print(set_to_list)  # Output: [1, 2, 3, 4, 5]

# Range to List
my_range = range(5)
range_to_list = list(my_range)
# print(range_to_list)  # Output: [0, 1, 2, 3, 4]

# Dictionary to List (only keys)
my_dict = {"a": 1, "b": 2, "c": 3}
dict_to_list = list(my_dict)
# print(dict_to_list)  # Output: ['a', 'b', 'c']

# Integer to List (using range)
score = 6
score_list = list(range(score))
# print(score_list)  # Output: [0, 1, 2, 3, 4, 5]

# Converting list of strings to list of integers
str_list = ["1", "2", "3", "4", "5"]
int_list = [int(x) for x in str_list]
# print(int_list)  # Output: [1, 2, 3, 4, 5]

# Using map for conversion
str_list = ["1", "2", "3", "4", "5"]
int_list = list(map(int, str_list))
# print(int_list)  # Output: [1, 2, 3, 4, 5]  

# tuple() - Convert to Tuple

# String to Tuple
name = "nazim"
name_tuple = tuple(name)
# print(name_tuple)  # Output: ('n', 'a', 'z', 'i', 'm')

# List to Tuple
my_list = [1, 2, 3, 4, 5]
list_to_tuple = tuple(my_list)
# print(list_to_tuple)  # Output: (1, 2, 3, 4, 5)

# Set to Tuple
my_set = {1, 2, 3, 4, 5}
set_to_tuple = tuple(my_set)
# print(set_to_tuple)  # Output: (1, 2, 3, 4, 5)

# Range to Tuple
my_range = range(5)
range_to_tuple = tuple(my_range)
# print(range_to_tuple)  # Output: (0, 1, 2, 3, 4)

# Integer to Tuple
score = 6
score_tuple = tuple(range(score))
# print(score_tuple)  # Output: (0, 1, 2, 3, 4, 5)

# Dictionary to Tuple (only keys)
my_dict = {"a": 1, "b": 2, "c": 3}
dict_to_tuple = tuple(my_dict)
# print(dict_to_tuple)  # Output: ('a', 'b', 'c')


# set() - Convert to Set

# String to Set (duplicates removed, unordered)
name = "nazim"
name_set = set(name)
# print(name_set)  # Output: {'n', 'z', 'm', 'a', 'i'} (order may vary)

# List to Set (duplicates removed automatically)
num_list = [1, 2, 3, 5, 4, 5, 6, 3, 4]
unique_set = set(num_list)
# print(unique_set)  # Output: {1, 2, 3, 4, 5, 6} (order may vary)

# Tuple to Set
my_tuple = (1, 2, 3, 2, 4, 1, 5)
tuple_to_set = set(my_tuple)
# print(tuple_to_set)  # Output: {1, 2, 3, 4, 5}

# Integer to Set
score = 6
score_set = set(range(score))
# print(score_set)  # Output: {0, 1, 2, 3, 4, 5}

# Dictionary to Set (only keys)
my_dict = {"a": 1, "b": 2, "c": 3}
dict_to_set = set(my_dict)
# print(dict_to_set)  # Output: {'a', 'b', 'c'}

# dict() - Convert to Dictionary

# List of tuples to Dictionary
list_of_tuples = [("name", "John"), ("age", 25), ("city", "NYC")]
dict_from_list = dict(list_of_tuples)
# print(dict_from_list)  # Output: {'name': 'John', 'age': 25, 'city': 'NYC'}

# Two lists to Dictionary using zip
keys = ["name", "age", "city"]
values = ["Alice", 30, "London"]
dict_from_lists = dict(zip(keys, values))
# print(dict_from_lists)  # Output: {'name': 'Alice', 'age': 30, 'city': 'London'}


# complex() - Convert to Complex Number

# Integer to Complex
num = 5
complex_num = complex(num)
# print(complex_num)  # Output: (5+0j)

# Float to Complex
num = 3.14
complex_num = complex(num)
# print(complex_num)  # Output: (3.14+0j)

# String to Complex
str_num = "3+4j"
complex_num = complex(str_num)
# print(complex_num)  # Output: (3+4j)

# Complex with real and imaginary parts
complex_num = complex(3, 4)
# print(complex_num)  # Output: (3+4j)


# Ex: Implicit mixed Type Operations

# Different types in arithmetic operations
a = 10          # int
b = 3.5         # float
c = "20"        # str
d = 2           # int

# Combining conversions
result = a + b + int(c) / d
# print(result)   # Output: 23.5
# print(type(result))  # Output: <class 'float'>

# Formatting Numbers

# Formatting after conversion
number = 1234.56789

# Integer conversion with formatting
# print(f"{int(number):,}")  # Output: 1,234

# Float with specific decimal places
# print(f"{float(number):.2f}")  # Output: 1234.57

# Percentage
percentage = 0.75
# print(f"{percentage:.1%}")  # Output: 75.0%