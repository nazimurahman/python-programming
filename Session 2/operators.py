# Arithmetic Operators used for mathematical calculations

# Arithmetic Operators in Python
a = 10
b = 3

# Addition (+)
sum_result = a + b  # Adds two numbers: 10 + 3 = 13
print(f"Addition: {sum_result}")

# Subtraction (-)
diff_result = a - b  # Subtracts second from first: 10 - 3 = 7
print(f"Subtraction: {diff_result}")

# Multiplication (*)
mul_result = a * b  # Multiplies two numbers: 10 * 3 = 30
print(f"Multiplication: {mul_result}")

# Division (/)
div_result = a / b  # Returns float result: 10 / 3 = 3.333...
print(f"Division: {div_result}")

# Floor Division (//)
floor_result = a // b  # Returns integer division: 10 // 3 = 3
print(f"Floor Division: {floor_result}")

# Modulus (%)
mod_result = a % b  # Returns remainder: 10 % 3 = 1
print(f"Modulus: {mod_result}")

# Exponentiation (**)
exp_result = a ** b  # Raises to power: 10^3 = 1000
print(f"Exponentiation: {exp_result}")

# Comparison (Relational) Operators used to compare values and return boolean results.

# Comparison Operators
x = 5
y = 10

# Equal to (==)
is_equal = x == y  # Checks if values are equal: False
print(f"Equal: {is_equal}")

# Not equal to (!=)
is_not_equal = x != y  # Checks if values are not equal: True
print(f"Not equal: {is_not_equal}")

# Greater than (>)
is_greater = x > y  # Checks if left is greater than right: False
print(f"Greater than: {is_greater}")

# Less than (<)
is_less = x < y  # Checks if left is less than right: True
print(f"Less than: {is_less}")

# Greater than or equal to (>=)
is_greater_equal = x >= y  # Checks if left >= right: False
print(f"Greater or equal: {is_greater_equal}")

# Less than or equal to (<=)
is_less_equal = x <= y  # Checks if left <= right: True
print(f"Less or equal: {is_less_equal}")


# Logical Operators used to combine conditional statements.

# Logical Operators
is_raining = True
has_umbrella = False

# AND (and) - Both conditions must be True
go_outside = not is_raining and has_umbrella  # False AND False = False
print(f"AND operator: {go_outside}")

# OR (or) - At least one condition must be True
stay_dry = is_raining or has_umbrella  # True OR False = True
print(f"OR operator: {stay_dry}")

# NOT (not) - Reverses the boolean value
should_stay_home = not is_raining  # NOT True = False
print(f"NOT operator: {should_stay_home}")

# Complex example
age = 25
has_license = True
can_drive = age >= 18 and has_license  # True AND True = True
print(f"Can drive: {can_drive}")


# Assignment Operators used to assign values to variables.

# Assignment Operators
num = 10  # Simple assignment
print(f"Initial: {num}")

# Addition assignment (+=)
num += 5  # Equivalent to: num = num + 5
print(f"After +=: {num}")  # Output: 15

# Subtraction assignment (-=)
num -= 3  # Equivalent to: num = num - 3
print(f"After -=: {num}")  # Output: 12

# Multiplication assignment (*=)
num *= 2  # Equivalent to: num = num * 2
print(f"After *=: {num}")  # Output: 24

# Division assignment (/=)
num /= 4  # Equivalent to: num = num / 4
print(f"After /=: {num}")  # Output: 6.0

# Floor division assignment (//=)
num //= 2  # Equivalent to: num = num // 2
print(f"After //=: {num}")  # Output: 3.0

# Modulus assignment (%=)
num %= 3  # Equivalent to: num = num % 3
print(f"After %=: {num}")  # Output: 0.0

# Bitwise Operators work on bits and perform bit-level operations.

# Bitwise Operators
a = 5  # Binary: 0101
b = 3  # Binary: 0011

# AND (&) - Sets each bit to 1 if both bits are 1
bitwise_and = a & b  # 0101 & 0011 = 0001 (1)
print(f"Bitwise AND: {bitwise_and}")

# OR (|) - Sets each bit to 1 if at least one bit is 1
bitwise_or = a | b  # 0101 | 0011 = 0111 (7)
print(f"Bitwise OR: {bitwise_or}")

# XOR (^) - Sets each bit to 1 if only one bit is 1
bitwise_xor = a ^ b  # 0101 ^ 0011 = 0110 (6)
print(f"Bitwise XOR: {bitwise_xor}")

# NOT (~) - Inverts all bits
bitwise_not = ~a  # ~0101 = 1010 (-6 in 2's complement)
print(f"Bitwise NOT: {bitwise_not}")

# Left Shift (<<) - Shifts bits left, fills with 0
left_shift = a << 1  # 0101 << 1 = 1010 (10)
print(f"Left Shift: {left_shift}")

# Right Shift (>>) - Shifts bits right, drops bits
right_shift = a >> 1  # 0101 >> 1 = 0010 (2)
print(f"Right Shift: {right_shift}")



#  Identity Operators check if two variables point to the same object.

# Identity Operators
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1  # list3 references the same object as list1

# is - True if both variables refer to same object
is_same = list1 is list3  # True - same object
print(f"is operator: {is_same}")

is_different = list1 is list2  # False - different objects with same content
print(f"is operator (different objects): {is_different}")

# is not - True if variables refer to different objects
is_not_same = list1 is not list2  # True - different objects
print(f"is not operator: {is_not_same}")

# Comparing with None
value = None
is_none = value is None  # True - checking for None
print(f"Check None: {is_none}")


#  Membership Operators test if a value is present in a sequence

# Membership Operators
fruits = ['apple', 'banana', 'orange', 'grape']
text = "Hello World"

# in - True if value exists in sequence
has_apple = 'apple' in fruits  # True
print(f"'apple' in fruits: {has_apple}")

has_pear = 'pear' in fruits  # False
print(f"'pear' in fruits: {has_pear}")

# in with strings
has_hello = 'Hello' in text  # True
print(f"'Hello' in text: {has_hello}")

# not in - True if value does NOT exist in sequence
not_in_list = 'mango' not in fruits  # True
print(f"'mango' not in fruits: {not_in_list}")

# With dictionaries (checks keys)
person = {'name': 'John', 'age': 30, 'city': 'NYC'}
has_name_key = 'name' in person  # True - checks keys
print(f"'name' in person: {has_name_key}")

has_john_value = 'John' in person.values()  # True - checks values
print(f"'John' in person.values(): {has_john_value}")


# Ternary/Conditional Operator short-hand for if-else statements.

# Ternary Operator in Python
age = 18

# Syntax: value_if_true if condition else value_if_false
status = "Adult" if age >= 18 else "Minor"
print(f"Status: {status}")  # Output: Adult

# Nested ternary
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D"
print(f"Grade: {grade}")  # Output: B

# Practical example
is_logged_in = True
message = "Welcome back!" if is_logged_in else "Please login"
print(f"Message: {message}")



#Operator Precedence understanding the order in which operators are evaluated.


# Operator Precedence Example
result = 10 + 5 * 2 - 3 ** 2 / 2
# Step by step evaluation:
# 1. 3 ** 2 = 9 (Exponentiation)
# 2. 5 * 2 = 10 (Multiplication)
# 3. 9 / 2 = 4.5 (Division)
# 4. 10 + 10 = 20 (Addition)
# 5. 20 - 4.5 = 15.5 (Subtraction)

print(f"Result with normal precedence: {result}")

# Using parentheses to change precedence
result_with_parentheses = (10 + 5) * 2 - (3 ** 2 / 2)
# Step by step:
# 1. (10 + 5) = 15
# 2. (3 ** 2 / 2) = 4.5
# 3. 15 * 2 = 30
# 4. 30 - 4.5 = 25.5
print(f"Result with parentheses: {result_with_parentheses}")

# Precedence from highest to lowest:
print("\nOperator Precedence (highest to lowest):")
print("1. () - Parentheses")
print("2. ** - Exponentiation")
print("3. *, /, //, % - Multiplication/Division")
print("4. +, - - Addition/Subtraction")
print("5. <<, >> - Bitwise shifts")
print("6. & - Bitwise AND")
print("7. ^ - Bitwise XOR")
print("8. | - Bitwise OR")
print("9. <, <=, >, >=, !=, == - Comparisons")
print("10. not - Logical NOT")
print("11. and - Logical AND")
print("12. or - Logical OR")



# Practical Example - Combining Operators


# Complete practical example
def calculate_bonus(salary, years_experience, performance_rating):
    """
    Calculate employee bonus based on multiple factors
    """
    # Check if employee qualifies for bonus
    qualifies = (years_experience >= 3) and (performance_rating >= 7)
    
    if qualifies:
        # Calculate base bonus
        base_bonus = salary * 0.10  # 10% of salary
        
        # Additional bonus based on performance
        if performance_rating >= 9:
            extra_bonus = base_bonus * 0.50  # 50% extra for excellent
        elif performance_rating >= 8:
            extra_bonus = base_bonus * 0.25  # 25% extra for very good
        else:
            extra_bonus = 0
            
        total_bonus = base_bonus + extra_bonus
    else:
        total_bonus = 0
    
    return total_bonus

# Test the function
employee_salary = 50000
experience = 5
rating = 8

bonus = calculate_bonus(employee_salary, experience, rating)
print(f"Employee Bonus: ${bonus:,.2f}")

# Using multiple operators in one line
age = 25
salary = 60000
employee_status = "Senior" if (age >= 30 and salary > 50000) else "Junior"
print(f"Employee Status: {employee_status}")