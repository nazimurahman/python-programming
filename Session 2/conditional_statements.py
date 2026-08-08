# Basic if Statement -> executes code block only when condition is True.

# Basic if statement
temperature = 25

# Simple if - checks if temperature is above comfort level
if temperature > 20:
    print("It's warm outside!")  # This will execute because 25 > 20
    print("You can wear light clothes.")  # Multiple statements can be in if block

# if with comparison
score = 85
if score >= 60:
    print(f"Score {score} is passing!")  # Will execute

# if with variable
is_weekend = True
if is_weekend:
    print("Time to relax!")  # Executes when True




# if-else Statement -> executes one block when condition is True, another when False.

# Basic if-else
age = 17

if age >= 18:
    print("You are eligible to vote.")  # This block executes if True
else:
    print("You are too young to vote.")  # This executes if False
    print(f"Wait {18 - age} more years.")  # Can have multiple statements

# Practical example with user input
user_balance = 100
purchase_amount = 150

if purchase_amount <= user_balance:
    print("Purchase approved!")
    user_balance -= purchase_amount
    print(f"Remaining balance: ${user_balance}")
else:
    print("Insufficient funds!")
    print(f"Need ${purchase_amount - user_balance} more.")



# if-elif-else Statement: -> Handles multiple conditions in sequence.

# if-elif-else structure
grade = 85

# Check multiple grade ranges
if grade >= 90:
    letter_grade = "A"
    message = "Excellent performance!"
elif grade >= 80:
    letter_grade = "B"
    message = "Good job!"
elif grade >= 70:
    letter_grade = "C"
    message = "Satisfactory"
elif grade >= 60:
    letter_grade = "D"
    message = "Need improvement"
else:
    letter_grade = "F"
    message = "Failing"

print(f"Grade: {letter_grade} - {message}")

# Another example - ticket pricing
age = 25

if age < 5:
    ticket_price = 0  # Free for toddlers
elif age < 12:
    ticket_price = 8  # Child price
elif age < 18:
    ticket_price = 12  # Student price
elif age < 60:
    ticket_price = 15  # Adult price
else:
    ticket_price = 10  # Senior discount

print(f"Ticket price: ${ticket_price}")



# Nested if-else Statements: -> if statements inside other if statements.

# Nested if-else example
is_logged_in = True
user_role = "admin"
has_permission = True

# Outer if checks login status
if is_logged_in:
    print("User is logged in")
    
    # Inner if checks role
    if user_role == "admin":
        print("Admin access granted")
        
        # Even deeper nesting for permissions
        if has_permission:
            print("Full system access available")
            print("Can modify all settings")
        else:
            print("Admin but limited permissions")
    elif user_role == "manager":
        print("Manager access granted")
    else:
        print("User access granted")
else:
    print("Please log in first")

# Nested if in practical scenario
def process_order(order_total, is_member, shipping_method):
    """Process order with multiple conditions"""
    
    # Check for minimum order
    if order_total > 0:
        print(f"Processing ${order_total} order")
        
        # Check membership status
        if is_member:
            print("Member discount applied")
            discount = order_total * 0.1
            print(f"Discount: ${discount:.2f}")
            order_total -= discount
        
        # Check shipping method
        if shipping_method == "express":
            print("Express shipping selected")
            shipping_cost = 15
            if order_total > 100:
                shipping_cost = 0  # Free express for orders over $100
                print("Free express shipping applied")
        else:
            print("Standard shipping")
            shipping_cost = 5
            if is_member:
                shipping_cost = 0  # Free shipping for members
                print("Free shipping for members")
        
        final_total = order_total + shipping_cost
        print(f"Final total: ${final_total:.2f}")
    else:
        print("Invalid order amount")

# Test the nested if function
process_order(150, True, "express")



# Special Case: elif vs Nested if -> Understanding when to use each.
# Using elif (mutually exclusive conditions)

score = 75

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Grade: {grade}")  # Only C executes

# Using separate if statements (multiple blocks can execute)

grade = "B"
bonus = 0

if grade == "A":
    bonus += 100
if grade == "B":
    bonus += 50
if grade == "C":
    bonus += 25
if grade == "D":
    bonus += 0

print(f"Bonus: {bonus}")  # Both B and C conditions checked, only B applies

# When to use each:
# Use elif when:
#  ->  Conditions are mutually exclusive
#  ->  Only one condition should execute
#  ->  You want to stop checking after a match

# Use nested if when:
#  ->  Conditions are dependent on each other
#  ->  Need to check multiple layers of conditions
#  ->  Have complex business logic


# Conditional Expressions (Ternary Operator) -> Single-line if-else statements.

# Basic ternary operator
age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Status: {status}")

# Nested ternary (use sparingly)
temperature = 25
weather = "Hot" if temperature > 30 else "Warm" if temperature > 20 else "Cool"
print(f"Weather: {weather}")

# Ternary with multiple conditions
is_member = True
is_weekend = False
discount = 0.2 if is_member and not is_weekend else 0.1 if is_member else 0
print(f"Discount: {discount * 100}%")

# Practical ternary example
def get_user_status(age, is_active):
    return "Active Adult" if age >= 18 and is_active else "Inactive or Minor"

print(get_user_status(25, True))  # Output: Active Adult


#  Chained Comparisons: -> Multiple comparisons in a single statement.

# Chained comparisons - more Pythonic
value = 50

# Traditional approach
if value >= 0 and value <= 100:
    print("Value is between 0 and 100 (traditional)")

# Chained comparison (cleaner)
if 0 <= value <= 100:
    print("Value is between 0 and 100 (chained)")

# More examples
age = 25
if 18 <= age < 65:
    print("Working age adult")

score = 85
if 70 <= score < 90:
    print("B grade")

# With strings
letter = 'm'
if 'a' <= letter <= 'z':
    print(f"{letter} is a lowercase letter")



# Practical Real-World Examples: -> User Authentication System
def authenticate_user(username, password, user_database):
    """
    Complete authentication system with multiple conditions
    """
    # Check if username exists
    if username not in user_database:
        print("❌ Username not found!")
        return False
    
    user_data = user_database[username]
    
    # Check password
    if user_data["password"] != password:
        print("❌ Incorrect password!")
        return False
    
    # Check account status
    if user_data["status"] == "banned":
        print("❌ Account is banned!")
        return False
    elif user_data["status"] == "suspended":
        print("⚠️ Account is suspended. Contact support.")
        return False
    
    # Check if email is verified
    if not user_data.get("verified", False):
        print("⚠️ Email not verified. Check your inbox.")
        return False
    
    # If all checks pass
    print(f"✅ Welcome back, {username}!")
    return True

# User database
users = {
    "alice": {
        "password": "secret123",
        "status": "active",
        "verified": True
    },
    "bob": {
        "password": "password456",
        "status": "suspended",
        "verified": True
    },
    "charlie": {
        "password": "pass789",
        "status": "active",
        "verified": False
    }
}

# Test authentication
authenticate_user("alice", "secret123", users)  # Success
authenticate_user("bob", "password456", users)  # Suspended
authenticate_user("charlie", "pass789", users)  # Not verified


# E-commerce Discount Calculator

def calculate_discount(order_amount, customer_tier, coupon_code, holiday_season):
    """
    Complex discount calculation with multiple conditions
    """
    base_discount = 0
    
    # Tier-based discount
    if customer_tier == "premium":
        base_discount = 0.20  # 20% off
    elif customer_tier == "gold":
        base_discount = 0.15  # 15% off
    elif customer_tier == "silver":
        base_discount = 0.10  # 10% off
    else:  # standard
        base_discount = 0.05  # 5% off
    
    # Additional discounts for large orders
    if order_amount > 1000:
        base_discount += 0.05  # Extra 5% for large orders
    elif order_amount > 500:
        base_discount += 0.03  # Extra 3% for medium orders
    
    # Coupon codes
    if coupon_code == "SAVE20":
        base_discount += 0.20
    elif coupon_code == "SAVE10":
        base_discount += 0.10
    elif coupon_code == "FLASH15":
        base_discount += 0.15
    
    # Holiday season bonus
    if holiday_season:
        base_discount += 0.05  # Extra 5% during holidays
    
    # Cap maximum discount at 50%
    if base_discount > 0.50:
        base_discount = 0.50
        print("⚠️ Maximum 50% discount applied")
    
    # Calculate final price
    discount_amount = order_amount * base_discount
    final_price = order_amount - discount_amount
    
    # Print summary
    print(f"Order Amount: ${order_amount:.2f}")
    print(f"Discount Rate: {base_discount * 100:.1f}%")
    print(f"Discount Amount: ${discount_amount:.2f}")
    print(f"Final Price: ${final_price:.2f}")
    
    return final_price

# Test the function
calculate_discount(750, "gold", "SAVE20", True)

# Grade Management System

def calculate_grade(assignments, midterm, final, participation):
    """
    Calculate final grade with multiple conditionals
    """
    # Calculate weighted average
    assignment_avg = sum(assignments) / len(assignments) if assignments else 0
    weighted_score = (
        assignment_avg * 0.3 +  # 30% assignments
        midterm * 0.3 +         # 30% midterm
        final * 0.3 +           # 30% final
        participation * 0.1     # 10% participation
    )
    
    print(f"Final Score: {weighted_score:.1f}%")
    
    # Determine letter grade with nested conditions
    if weighted_score >= 90:
        letter_grade = "A"
        if weighted_score >= 97:
            remark = "Excellent! Outstanding performance!"
        elif weighted_score >= 93:
            remark = "Very good! Keep it up!"
        else:
            remark = "Good work!"
            
    elif weighted_score >= 80:
        letter_grade = "B"
        if weighted_score >= 87:
            remark = "Above average performance"
        else:
            remark = "Good but can improve"
            
    elif weighted_score >= 70:
        letter_grade = "C"
        if weighted_score >= 77:
            remark = "Satisfactory performance"
        else:
            remark = "Needs improvement in some areas"
            
    elif weighted_score >= 60:
        letter_grade = "D"
        remark = "Below average. Need significant improvement"
        
    else:
        letter_grade = "F"
        remark = "Failing. Must retake the course"
        
        # Special check for failing students
        if midterm < 50 or final < 50:
            remark += " (Poor exam performance)"
        elif assignment_avg < 50:
            remark += " (Poor assignment performance)"
    
    print(f"Letter Grade: {letter_grade}")
    print(f"Remark: {remark}")
    
    return letter_grade

# Test with different scenarios
calculate_grade([85, 90, 88], 82, 91, 80)


# Basic isinstance() Usage

# Basic isinstance() - checks if object is instance of a class
number = 10
text = "Hello"
boolean = True
decimal = 3.14

# Check type of variables
print(f"Is 10 an int? {isinstance(number, int)}")        # True
print(f"Is 'Hello' a str? {isinstance(text, str)}")      # True
print(f"Is True a bool? {isinstance(boolean, bool)}")    # True
print(f"Is 3.14 a float? {isinstance(decimal, float)}")  # True

# Check against multiple types
print(f"Is 10 int or float? {isinstance(number, (int, float))}")  # True
print(f"Is True int or bool? {isinstance(boolean, (int, bool))}") # True
print(f"Is 'Hello' int or str? {isinstance(text, (int, str))}")   # True



# isinstance() with Custom Classes

# Define custom classes
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Car:
    def __init__(self, brand):
        self.brand = brand

# Create instances
dog = Dog("Buddy")
cat = Cat("Whiskers")
car = Car("Toyota")
animal = Animal("Generic")

# isinstance with inheritance
print(f"Is dog a Dog? {isinstance(dog, Dog)}")          # True
print(f"Is dog an Animal? {isinstance(dog, Animal)}")   # True (inheritance)
print(f"Is dog a Car? {isinstance(dog, Car)}")          # False
print(f"Is animal an Animal? {isinstance(animal, Animal)}")  # True
print(f"Is animal a Dog? {isinstance(animal, Dog)}")    # False

# Multiple types including parent classes
print(f"Is dog Dog or Cat? {isinstance(dog, (Dog, Cat))}")    # True
print(f"Is dog Animal or Car? {isinstance(dog, (Animal, Car))}")  # True
print(f"Is car Animal or Car? {isinstance(car, (Animal, Car))}")  # True


# isinstance() with Built-in Types

# Comprehensive type checking
data = [1, 2, 3]
numbers = (4, 5, 6)
info = {"name": "John", "age": 30}
unique = {1, 2, 3}
empty = None

print("=== Built-in Type Checking ===")
print(f"Is list a list? {isinstance(data, list)}")          # True
print(f"Is tuple a tuple? {isinstance(numbers, tuple)}")    # True
print(f"Is dict a dict? {isinstance(info, dict)}")          # True
print(f"Is set a set? {isinstance(unique, set)}")           # True
print(f"Is None NoneType? {isinstance(empty, type(None))}") # True

# Checking against base types
print(f"Is list an iterable? {isinstance(data, (list, tuple, set))}")  # True
print(f"Is tuple an iterable? {isinstance(numbers, (list, tuple, set))}")  # True

# Checking numeric types
values = [1, 3.14, 2+3j, True, "not a number"]
for value in values:
    print(f"{value} is number? {isinstance(value, (int, float, complex))}")


#  Practical Examples with isinstance(): -> Function Parameter Validation\
def process_data(data, operation):
    """
    Process different types of data with various operations
    """
    # Validate data type
    if not isinstance(data, (list, tuple, dict, str)):
        raise TypeError(f"Unsupported data type: {type(data)}")
    
    # Process based on type
    if isinstance(data, (list, tuple)):
        if operation == "sum":
            # Only works if all elements are numbers
            if all(isinstance(x, (int, float)) for x in data):
                return sum(data)
            else:
                raise ValueError("All elements must be numbers for sum")
        elif operation == "length":
            return len(data)
        else:
            return list(data) if isinstance(data, tuple) else data
    
    elif isinstance(data, dict):
        if operation == "keys":
            return list(data.keys())
        elif operation == "values":
            return list(data.values())
        elif operation == "items":
            return list(data.items())
        else:
            return data
    
    elif isinstance(data, str):
        if operation == "uppercase":
            return data.upper()
        elif operation == "length":
            return len(data)
        else:
            return data

# Test the function
print("=== Processing Different Data Types ===")
print(process_data([1, 2, 3, 4], "sum"))          # 10
print(process_data((1, 2, 3), "length"))          # 3
print(process_data({"a": 1, "b": 2}, "keys"))     # ['a', 'b']
print(process_data("hello", "uppercase"))         # "HELLO"

# Error cases
try:
    process_data(123, "sum")  # Invalid type
except TypeError as e:
    print(f"Error: {e}")

try:
    process_data([1, "2", 3], "sum")  # Mixed types
except ValueError as e:
    print(f"Error: {e}")



# Data Validation System

class User:
    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age

class Admin(User):
    def __init__(self, username, email, age, permissions):
        super().__init__(username, email, age)
        self.permissions = permissions

class Guest:
    def __init__(self, session_id):
        self.session_id = session_id

def validate_and_process_user(user_data):
    """
    Complex validation using isinstance()
    """
    # Type validation
    if not isinstance(user_data, (User, Admin, Guest)):
        raise TypeError(f"Expected User, Admin, or Guest, got {type(user_data)}")
    
    # Process based on type and conditions
    if isinstance(user_data, Admin):
        print(f"Admin: {user_data.username}")
        print(f"Permissions: {user_data.permissions}")
        
        # Additional validation for admin
        if not isinstance(user_data.permissions, list):
            raise ValueError("Permissions must be a list")
        
        return f"Admin access granted to {user_data.username}"
    
    elif isinstance(user_data, User):
        print(f"Regular User: {user_data.username}")
        
        # Validate user age
        if not isinstance(user_data.age, int):
            raise TypeError("Age must be an integer")
        
        if user_data.age < 18:
            return f"User {user_data.username} is a minor (age {user_data.age})"
        else:
            return f"User {user_data.username} is an adult"
    
    elif isinstance(user_data, Guest):
        print(f"Guest: Session {user_data.session_id}")
        
        # Guest validation
        if not isinstance(user_data.session_id, str):
            raise TypeError("Session ID must be string")
        
        return f"Guest access for session {user_data.session_id}"
    
    return "Unknown user type"

# Test the validation system
admin = Admin("alice_admin", "alice@company.com", 35, ["read", "write", "delete"])
user = User("bob_user", "bob@example.com", 25)
guest = Guest("session_12345")
invalid = "not a user"

print("=== User Processing Results ===")
print(validate_and_process_user(admin))
print("\n" + validate_and_process_user(user))
print("\n" + validate_and_process_user(guest))

try:
    print(validate_and_process_user(invalid))
except TypeError as e:
    print(f"\nError: {e}")



# isinstance() with Generic Types and Type Hints

from typing import List, Dict, Union, Optional, Any
from collections.abc import Iterable, Sequence, Mapping

def process_collection(data: Any):
    """
    Process data with isinstance checking against abstract types
    """
    # Check if iterable
    if isinstance(data, Iterable):
        print(f"{data} is iterable")
        
        # Check if sequence (list, tuple, str, bytes)
        if isinstance(data, Sequence):
            print(f"  It's also a sequence with length {len(data)}")
        
        # Check if mapping (dict)
        if isinstance(data, Mapping):
            print(f"  It's also a mapping with {len(data)} keys")
    
    # Type-specific processing
    if isinstance(data, list):
        print("  Processing as list")
        return [str(x) for x in data]
    
    elif isinstance(data, tuple):
        print("  Processing as tuple")
        return tuple(str(x) for x in data)
    
    elif isinstance(data, dict):
        print("  Processing as dict")
        return {k: str(v) for k, v in data.items()}
    
    elif isinstance(data, str):
        print("  Processing as string")
        return data.upper()
    
    return "Unknown collection type"

# Test with different collections
collections = [
    [1, 2, 3],
    (4, 5, 6),
    {"a": 1, "b": 2},
    "hello",
    {1, 2, 3},  # Set is iterable but not sequence or mapping
    123,         # Not iterable
]

print("=== Generic Type Checking ===")
for item in collections:
    print(f"\nTesting: {item}")
    result = process_collection(item)
    print(f"Result: {result}")



# isinstance() with Exception Handling
def safe_divide(a, b):
    """
    Safe division with comprehensive type checking
    """
    # Check if both are numbers
    if not isinstance(a, (int, float)):
        raise TypeError(f"First argument must be numeric, got {type(a)}")
    
    if not isinstance(b, (int, float)):
        raise TypeError(f"Second argument must be numeric, got {type(b)}")
    
    # Check for division by zero
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    
    return a / b

def process_user_input(user_input):
    """
    Process user input with isinstance validation
    """
    # Handle None
    if user_input is None:
        return "No input provided"
    
    # Handle different types
    if isinstance(user_input, str):
        # Try to convert to number if it looks like one
        if user_input.isdigit():
            return safe_divide(int(user_input), 2)
        else:
            return f"String: {user_input.upper()}"
    
    elif isinstance(user_input, (int, float)):
        return safe_divide(user_input, 2)
    
    elif isinstance(user_input, (list, tuple)):
        # Process each element
        results = []
        for item in user_input:
            try:
                results.append(process_user_input(item))
            except Exception as e:
                results.append(f"Error: {e}")
        return results
    
    elif isinstance(user_input, dict):
        # Process dictionary values
        return {k: process_user_input(v) for k, v in user_input.items()}
    
    else:
        return f"Unsupported type: {type(user_input)}"

# Test the robust functions
test_inputs = [
    10,
    3.14,
    "42",
    "hello",
    [1, 2, 3, "4"],
    {"a": 10, "b": "20", "c": [1, 2]},
    None,
    True,
    (5, 6, 7)
]

print("=== Robust Input Processing ===")
for test in test_inputs:
    print(f"\nInput: {test} (type: {type(test)})")
    try:
        result = process_user_input(test)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")


# isinstance() with Dataclasses and Custom Types
from dataclasses import dataclass
from datetime import datetime, date
from enum import Enum

@dataclass
class Person:
    """Person dataclass with type validation"""
    name: str
    age: int
    birth_date: date
    
    def __post_init__(self):
        # Validate types on creation
        if not isinstance(self.name, str):
            raise TypeError(f"Name must be string, got {type(self.name)}")
        
        if not isinstance(self.age, int):
            raise TypeError(f"Age must be integer, got {type(self.age)}")
        
        if not isinstance(self.birth_date, date):
            raise TypeError(f"Birth date must be date, got {type(self.birth_date)}")

class UserStatus(Enum):
    """Enum for user status"""
    ACTIVE = "active"
    INACTIVE = "inactive"
    BANNED = "banned"
    SUSPENDED = "suspended"

@dataclass
class UserAccount:
    """User account with comprehensive type validation"""
    username: str
    email: str
    status: UserStatus
    person: Person
    created_at: datetime
    
    def __post_init__(self):
        # Validate all fields
        self._validate_type(self.username, str, "username")
        self._validate_type(self.email, str, "email")
        self._validate_type(self.status, UserStatus, "status")
        self._validate_type(self.person, Person, "person")
        self._validate_type(self.created_at, datetime, "created_at")
        
        # Additional validation
        if not "@" in self.email:
            raise ValueError("Invalid email format")
    
    def _validate_type(self, value, expected_type, field_name):
        """Helper method for type validation"""
        if not isinstance(value, expected_type):
            raise TypeError(
                f"Field '{field_name}' must be {expected_type.__name__}, "
                f"got {type(value).__name__}"
            )

def validate_and_process_account(account: Any):
    """
    Process account with isinstance validation
    """
    # Check if it's a UserAccount
    if not isinstance(account, UserAccount):
        raise TypeError(f"Expected UserAccount, got {type(account)}")
    
    # Check status with isinstance
    if not isinstance(account.status, UserStatus):
        raise TypeError(f"Invalid status type: {type(account.status)}")
    
    # Process based on status
    if account.status == UserStatus.ACTIVE:
        return f"Active user: {account.username}"
    elif account.status == UserStatus.INACTIVE:
        return f"Inactive user: {account.username} (needs activation)"
    elif account.status == UserStatus.BANNED:
        return f"BANNED user: {account.username} (access revoked)"
    elif account.status == UserStatus.SUSPENDED:
        return f"Suspended user: {account.username} (temporary block)"
    else:
        return f"Unknown status for {account.username}"

# Create and test account
person = Person("John Doe", 30, date(1993, 5, 15))
account = UserAccount(
    username="johndoe",
    email="john@example.com",
    status=UserStatus.ACTIVE,
    person=person,
    created_at=datetime.now()
)

print("=== Dataclass Validation ===")
print(validate_and_process_account(account))

# Test invalid account
try:
    invalid_person = Person("Jane", "25", "1994-06-20")  # Invalid types
except TypeError as e:
    print(f"Validation error: {e}")



# Real-World Production Example
import json
from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass, asdict

@dataclass
class APIResponse:
    """API response with type validation"""
    status: str
    data: Optional[Dict[str, Any]]
    message: str
    code: int
    
    def __post_init__(self):
        """Validate types after initialization"""
        if not isinstance(self.status, str):
            raise TypeError(f"Status must be str, got {type(self.status)}")
        
        if self.data is not None and not isinstance(self.data, dict):
            raise TypeError(f"Data must be dict or None, got {type(self.data)}")
        
        if not isinstance(self.message, str):
            raise TypeError(f"Message must be str, got {type(self.message)}")
        
        if not isinstance(self.code, int):
            raise TypeError(f"Code must be int, got {type(self.code)}")
    
    def to_json(self) -> str:
        """Convert to JSON with type safety"""
        data_dict = asdict(self)
        # Ensure nested types are serializable
        self._ensure_serializable(data_dict)
        return json.dumps(data_dict)
    
    def _ensure_serializable(self, data):
        """Recursively ensure all data is JSON serializable"""
        if isinstance(data, dict):
            return {k: self._ensure_serializable(v) for k, v in data.items()}
        elif isinstance(data, list):
            return [self._ensure_serializable(item) for item in data]
        elif data is None or isinstance(data, (str, int, float, bool)):
            return data
        else:
            return str(data)  # Convert non-serializable to string

class DataParser:
    """Production data parser with isinstance validation"""
    
    @staticmethod
    def parse_input(input_data: Any) -> Dict[str, Any]:
        """
        Parse various input types with comprehensive validation
        """
        # Check for None
        if input_data is None:
            return {"error": "No input provided"}
        
        # Handle JSON string
        if isinstance(input_data, str):
            try:
                parsed = json.loads(input_data)
                return DataParser._process_parsed_data(parsed)
            except json.JSONDecodeError:
                return {"error": "Invalid JSON format", "data": input_data}
        
        # Handle dictionary
        elif isinstance(input_data, dict):
            return DataParser._process_parsed_data(input_data)
        
        # Handle list
        elif isinstance(input_data, list):
            results = []
            for item in input_data:
                result = DataParser.parse_input(item)
                results.append(result)
            return {"results": results}
        
        # Handle other types
        elif isinstance(input_data, (int, float, bool)):
            return {"value": input_data, "type": type(input_data).__name__}
        
        else:
            return {"error": f"Unsupported input type: {type(input_data).__name__}"}
    
    @staticmethod
    def _process_parsed_data(data: Dict[str, Any]) -> Dict[str, Any]:
        """Process parsed JSON data with validation"""
        required_fields = ["id", "name", "value"]
        processed = {"valid": True, "data": {}}
        
        # Validate required fields
        missing_fields = [f for f in required_fields if f not in data]
        if missing_fields:
            processed["valid"] = False
            processed["error"] = f"Missing fields: {missing_fields}"
            return processed
        
        # Validate field types
        id_value = data.get("id")
        name_value = data.get("name")
        value_value = data.get("value")
        
        if not isinstance(id_value, (int, str)):
            processed["valid"] = False
            processed["error"] = f"ID must be int or str, got {type(id_value).__name__}"
            return processed
        
        if not isinstance(name_value, str):
            processed["valid"] = False
            processed["error"] = f"Name must be str, got {type(name_value).__name__}"
            return processed
        
        if not isinstance(value_value, (int, float)):
            processed["valid"] = False
            processed["error"] = f"Value must be number, got {type(value_value).__name__}"
            return processed
        
        # All validations passed
        processed["data"] = {
            "id": id_value,
            "name": name_value,
            "value": value_value,
            "processed_at": datetime.now().isoformat()
        }
        
        return processed

# Production test
test_cases = [
    None,
    '{"id": 1, "name": "Test", "value": 42}',
    '{"id": "abc", "name": "Invalid", "value": "not a number"}',
    {"id": 2, "name": "Dict Test", "value": 99.9},
    [{"id": 3, "name": "Item 1", "value": 10}, {"id": 4, "name": "Item 2", "value": 20}],
    42,
    "plain string"
]

print("=== Production Data Parser ===")
parser = DataParser()
for test in test_cases:
    print(f"\nInput: {test}")
    result = parser.parse_input(test)
    print(f"Result: {json.dumps(result, indent=2)}")

# Create API response
response = APIResponse(
    status="success",
    data={"id": 1, "name": "API Test", "value": 100},
    message="Data processed successfully",
    code=200
)

print(f"\nAPI Response: {response.to_json()}")


