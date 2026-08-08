"""
In Python, data types defines what kind of value a variable hold, As we know python is
dynamically types programming language it means 'Python' can automatically interprete 
assign a data type based on vlaue (data) given to the variable.
Data types:
  -> Integer Data Type
  -> Float Data Type
  -> String Data Type
  -> Boolean Data Type
  -> None Type Data Type
  -> Complex Data Type
  -> Lists
  -> Touple
  -> Dictionary
  -> Set (frozenset)
"""
# Integer Data Type (int)
# It can reqresent whole numbers ('+ve' & '-ve' values -> data)
age = 24
temp = -10
# print(f'He is {age} year old and he can bear colest temp {temp} Data types{type(age,temp)}')

# Float Data Type (float)
# It can represent the numbers but with decimal point ( '+ve' & '-ve' values -> data )
cgpa = 3.99
per = 99.9
# print(f'Ali scored {cgpa} CGPA with {per} %.Data types{type(cgpa)}')

# String Data Type (str)
# It represent 'Text Data' in Single, Double & Multi strings
first_name = 'nazim'
last_name = "urahman"
info = """ My name is Nazim Urahman and i am a python developer with some sort of
experience with Machine learning, deep learning, natural language processing, 
computer vision, data science, generative ai, agentic ai and LLMs. """
# print(info, type(info))

# Complex Data Type (complex)
# It can be used in the advanced mathematics (a + bj -> real_part: a or imaginary_part: b)
complex_data = 9 + 8j
# print(complex_data, type(complex_data))

# Boolean Data Type (True or False)
# It can be used in the conditional statements
is_student = True
employed = False
# print(f'Is Ali Student?: {is_student} and Is he employed?:{employed} {type(is_student)}')

# None Type (None)
# It can represents empty or absence of any value.
result = None
# print(result, type(result))

# List -> list: ([1,2,3,4])
# Lists are mutable, ordered elements of data
# they are changeable, allows duplicates, & it can modified. 
fruits = (['apple', 'orange','banana'])
# print(type(fruits))
# NOTE: complete working of the list should be discused latter.

# Touple -> touple((12, 21,42,43,53))
# they are immutable, oreder and can't modified
# they don't allow duplicates, and faster then lists
cord = ((12,14,15,11, 12))
# print(cord, type(cord))
# NOTE: complete working of the Touple should be discused latter.

# Dictionary -> {'key': 'value'}
# they are unordered, changeable
dic = {'name': 'Nazim', 'age':25}
# print(dic, type(dic))
# NOTE: complete working of the Dictionary should be discused latter.

# Set -> {1,2,3,4,5}
# Set is an unordered unique elements
# they are mutable or modified
unique_elements = {1,2,3,4,5,}
# print(f'{type(unique_elements)} Elements are: {unique_elements}')

# Frozenset -> ({1,2,3,4,5,})
# Immutable version of the set
frz_set = ({1,2,3,4,5})
# print(f'{type(frz_set)} Elements are: {frz_set}')