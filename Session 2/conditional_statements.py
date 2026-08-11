# CONDITIONAL STATEMENTS AND TYPE VALIDATION IN PYTHON

# ----------Basic if statement------------------

temperature = 25  # Store the temperature as an integer.

# The condition is checked.
# The block executes only when temperature is greater than 20.
if temperature > 20:
    print("It's warm outside!")  # Runs because 25 > 20.
    print("You can wear light clothes.")  # Another statement in the if block.


# ---------if with comparison---------------

score = 85  # Store a student's score.

# >= means "greater than or equal to".
if score >= 60:
    print(f"Score {score} is passing!")  # f-string inserts the score value.


# ---------if with Boolean variable--------------------

is_weekend = True  # Boolean value: True or False.

# This condition runs because is_weekend is True.
if is_weekend:
    print("Time to relax!")


# --------if-else statement------------------

age = 17  # Store the user's age.

if age >= 18:  # Check whether the user is at least 18.
    print("You are eligible to vote.")
else:  # Runs when the if condition is False.
    print("You are too young to vote.")
    print(f"Wait {18 - age} more years.")  # Calculate remaining years.


# ---------Practical balance example------------------

user_balance = 100  # Available money.
purchase_amount = 150  # Required money.

if purchase_amount <= user_balance:
    print("Purchase approved!")

    user_balance -= purchase_amount
    # The statement above is equivalent to:
    # user_balance = user_balance - purchase_amount

    print(f"Remaining balance: ${user_balance:.2f}")
else:
    print("Insufficient funds!")

    required_amount = purchase_amount - user_balance
    print(f"Need ${required_amount:.2f} more.")


# ------------if-elif-else statement-----------------

def get_grade(score):
    """Return a letter grade and message after validating the score."""

    # Reject Boolean values because bool is technically a subclass of int.
    if isinstance(score, bool) or not isinstance(score, (int, float)):
        raise TypeError("Score must be an integer or float.")

    # Scores must be within the valid range.
    if not 0 <= score <= 100:
        raise ValueError("Score must be between 0 and 100.")

    # Only one branch executes because these conditions are mutually exclusive.
    if score >= 90:
        return "A", "Excellent performance!"
    elif score >= 80:
        return "B", "Good job!"
    elif score >= 70:
        return "C", "Satisfactory"
    elif score >= 60:
        return "D", "Needs improvement"
    else:
        return "F", "Failing"


letter_grade, message = get_grade(85)
print(f"Grade: {letter_grade} - {message}")


# ------------Ticket pricing------------------

def calculate_ticket_price(age):
    """Calculate a ticket price according to age."""

    if isinstance(age, bool) or not isinstance(age, int):
        raise TypeError("Age must be an integer.")

    if age < 0:
        raise ValueError("Age cannot be negative.")

    if age < 5:
        return 0
    elif age < 12:
        return 8
    elif age < 18:
        return 12
    elif age < 60:
        return 15
    else:
        return 10


ticket_price = calculate_ticket_price(25)
print(f"Ticket price: ${ticket_price}")


# ------------Nested if statements-----------------

def check_access(is_logged_in, user_role, has_permission):
    """Check access using nested conditional statements."""

    # The outer condition checks whether the user is logged in.
    if is_logged_in:
        print("User is logged in.")

        # The inner condition checks the user's role.
        if user_role == "admin":
            print("Admin access granted.")

            # A deeper condition checks permission.
            if has_permission:
                print("Full system access available.")
                print("Can modify all settings.")
            else:
                print("Admin but limited permissions.")

        elif user_role == "manager":
            print("Manager access granted.")
        else:
            print("Basic user access granted.")
    else:
        print("Please log in first.")


check_access(True, "admin", True)


# -----------Nested practical order example------------------

def process_order(order_total, is_member, shipping_method):
    """Process an order using validation and nested conditions."""

    # Validate the order amount.
    if isinstance(order_total, bool) or not isinstance(
        order_total, (int, float)
    ):
        raise TypeError("Order total must be an integer or float.")

    if order_total <= 0:
        print("Invalid order amount.")
        return None

    # Validate the membership value.
    if not isinstance(is_member, bool):
        raise TypeError("is_member must be True or False.")

    # Validate the shipping method.
    valid_shipping_methods = {"standard", "express"}

    if shipping_method not in valid_shipping_methods:
        raise ValueError("Shipping method must be 'standard' or 'express'.")

    print(f"Processing ${order_total:.2f} order.")

    # Apply membership discount.
    if is_member:
        print("Member discount applied.")

        discount = order_total * 0.10
        print(f"Discount: ${discount:.2f}")

        order_total -= discount

    # Select shipping cost.
    if shipping_method == "express":
        print("Express shipping selected.")

        shipping_cost = 15

        # Nested condition for free express shipping.
        if order_total > 100:
            shipping_cost = 0
            print("Free express shipping applied.")

    else:
        print("Standard shipping.")

        shipping_cost = 5

        # Members get free standard shipping.
        if is_member:
            shipping_cost = 0
            print("Free shipping for members.")

    final_total = order_total + shipping_cost
    print(f"Final total: ${final_total:.2f}")

    return final_total


process_order(150, True, "express")


# ------------elif versus separate if---------------

score = 75

# elif is appropriate because only one grade should be selected.
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

print(f"Grade: {grade}")


grade = "B"
bonus = 0

# Separate if statements are useful when conditions are independent.
if grade == "A":
    bonus += 100

if grade == "B":
    bonus += 50

if grade == "C":
    bonus += 25

if grade == "D":
    bonus += 0

print(f"Bonus: {bonus}")


# ------------Conditional expression-----------------

age = 20

# Syntax:
# value_if_true if condition else value_if_false
status = "Adult" if age >= 18 else "Minor"

print(f"Status: {status}")


temperature = 25

# Nested conditional expressions should be used sparingly.
if temperature > 30:
    weather = "Hot"
elif temperature > 20:
    weather = "Warm"
else:
    weather = "Cool"

print(f"Weather: {weather}")


is_member = True
is_weekend = False

if is_member and not is_weekend:
    discount = 0.20
elif is_member:
    discount = 0.10
else:
    discount = 0

print(f"Discount: {discount * 100:.0f}%")


def get_user_status(age, is_active):
    """Return a status based on age and account activity."""

    if isinstance(age, bool) or not isinstance(age, int):
        raise TypeError("Age must be an integer.")

    if age < 0:
        raise ValueError("Age cannot be negative.")

    if not isinstance(is_active, bool):
        raise TypeError("is_active must be Boolean.")

    if age >= 18 and is_active:
        return "Active Adult"

    return "Inactive or Minor"


print(get_user_status(25, True))


# ------------Chained comparisons------------------

value = 50

# Traditional comparison.
if value >= 0 and value <= 100:
    print("Value is between 0 and 100.")

# Python's chained comparison.
if 0 <= value <= 100:
    print("Value is between 0 and 100.")


age = 25

if 18 <= age < 65:
    print("Working-age adult.")


score = 85

if 70 <= score < 90:
    print("B-grade range.")


letter = "m"

if "a" <= letter <= "z":
    print(f"{letter} is a lowercase letter.")


# ------------Authentication system------------------

def authenticate_user(username, password, user_database):
    """Authenticate a user using multiple independent checks."""

    if not isinstance(username, str):
        raise TypeError("Username must be a string.")

    if not isinstance(password, str):
        raise TypeError("Password must be a string.")

    if not isinstance(user_database, dict):
        raise TypeError("User database must be a dictionary.")

    # Check whether the username exists.
    if username not in user_database:
        print("Username not found.")
        return False

    user_data = user_database[username]

    # Check that the stored record is a dictionary.
    if not isinstance(user_data, dict):
        print("Invalid user record.")
        return False

    # Check the password.
    if user_data.get("password") != password:
        print("Incorrect password.")
        return False

    status = user_data.get("status")

    # Account status conditions are mutually exclusive.
    if status == "banned":
        print("Account is banned.")
        return False
    elif status == "suspended":
        print("Account is suspended. Contact support.")
        return False
    elif status != "active":
        print("Unknown account status.")
        return False

    # The default value is False if verified is missing.
    if not user_data.get("verified", False):
        print("Email not verified.")
        return False

    print(f"Welcome back, {username}!")
    return True


users = {
    "alice": {
        "password": "secret123",
        "status": "active",
        "verified": True,
    },
    "bob": {
        "password": "password456",
        "status": "suspended",
        "verified": True,
    },
    "charlie": {
        "password": "pass789",
        "status": "active",
        "verified": False,
    },
}

authenticate_user("alice", "secret123", users)
authenticate_user("bob", "password456", users)
authenticate_user("charlie", "pass789", users)
authenticate_user("unknown", "test", users)


# ------------Discount calculator-----------------

def calculate_discount(
    order_amount,
    customer_tier,
    coupon_code=None,
    holiday_season=False,
):
    """Calculate a discount with validation and conditional rules."""

    if isinstance(order_amount, bool) or not isinstance(
        order_amount, (int, float)
    ):
        raise TypeError("Order amount must be numeric.")

    if order_amount < 0:
        raise ValueError("Order amount cannot be negative.")

    valid_tiers = {"standard", "silver", "gold", "premium"}

    if customer_tier not in valid_tiers:
        raise ValueError("Invalid customer tier.")

    if coupon_code is not None and not isinstance(coupon_code, str):
        raise TypeError("Coupon code must be a string or None.")

    if not isinstance(holiday_season, bool):
        raise TypeError("holiday_season must be Boolean.")

    # Tier-based discount.
    if customer_tier == "premium":
        base_discount = 0.20
    elif customer_tier == "gold":
        base_discount = 0.15
    elif customer_tier == "silver":
        base_discount = 0.10
    else:
        base_discount = 0.05

    # Order-size discount.
    if order_amount > 1000:
        base_discount += 0.05
    elif order_amount > 500:
        base_discount += 0.03

    # Coupon discount.
    if coupon_code == "SAVE20":
        base_discount += 0.20
    elif coupon_code == "SAVE10":
        base_discount += 0.10
    elif coupon_code == "FLASH15":
        base_discount += 0.15
    elif coupon_code is not None:
        print("Coupon code is not recognized.")

    # Holiday discount.
    if holiday_season:
        base_discount += 0.05

    # Limit the discount to 50 percent.
    if base_discount > 0.50:
        base_discount = 0.50
        print("Maximum 50% discount applied.")

    discount_amount = order_amount * base_discount
    final_price = order_amount - discount_amount

    print(f"Order amount: ${order_amount:.2f}")
    print(f"Discount rate: {base_discount * 100:.1f}%")
    print(f"Discount amount: ${discount_amount:.2f}")
    print(f"Final price: ${final_price:.2f}")

    return final_price


calculate_discount(750, "gold", "SAVE20", True)


# ---------Grade management system------------------

def calculate_grade(assignments, midterm, final, participation):
    """Calculate a weighted grade with validation."""

    if not isinstance(assignments, (list, tuple)):
        raise TypeError("Assignments must be a list or tuple.")

    if not assignments:
        raise ValueError("At least one assignment score is required.")

    all_scores = list(assignments) + [midterm, final, participation]

    for current_score in all_scores:
        if isinstance(current_score, bool) or not isinstance(
            current_score, (int, float)
        ):
            raise TypeError("All scores must be numeric.")

        if not 0 <= current_score <= 100:
            raise ValueError("Every score must be between 0 and 100.")

    assignment_avg = sum(assignments) / len(assignments)

    weighted_score = (
        assignment_avg * 0.30
        + midterm * 0.30
        + final * 0.30
        + participation * 0.10
    )

    print(f"Final score: {weighted_score:.1f}%")

    # Outer if selects the letter grade.
    if weighted_score >= 90:
        letter_grade = "A"

        # Nested conditions provide a more detailed remark.
        if weighted_score >= 97:
            remark = "Excellent! Outstanding performance!"
        elif weighted_score >= 93:
            remark = "Very good! Keep it up!"
        else:
            remark = "Good work!"

    elif weighted_score >= 80:
        letter_grade = "B"

        if weighted_score >= 87:
            remark = "Above-average performance."
        else:
            remark = "Good, but there is room for improvement."

    elif weighted_score >= 70:
        letter_grade = "C"

        if weighted_score >= 77:
            remark = "Satisfactory performance."
        else:
            remark = "Needs improvement in some areas."

    elif weighted_score >= 60:
        letter_grade = "D"
        remark = "Below average; significant improvement is needed."

    else:
        letter_grade = "F"
        remark = "Failing; the course must be retaken."

        # Independent checks can add more details.
        if midterm < 50 or final < 50:
            remark += " Poor exam performance."
        elif assignment_avg < 50:
            remark += " Poor assignment performance."

    print(f"Letter grade: {letter_grade}")
    print(f"Remark: {remark}")

    return letter_grade


calculate_grade([85, 90, 88], 82, 91, 80)


# -------------isinstance() examples-----------------

number = 10
text = "Hello"
boolean = True
decimal = 3.14

print(isinstance(number, int))
print(isinstance(text, str))
print(isinstance(boolean, bool))
print(isinstance(decimal, float))

# A tuple allows checking more than one type.
print(isinstance(number, (int, float)))
print(isinstance(text, (int, str)))

# Important: bool is a subclass of int.
print(isinstance(True, int))  # True.
print(isinstance(True, bool))  # True.


# -----------------------------
# 17. isinstance() with classes
# -----------------------------

class Animal:
    """Base class for animals."""

    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"


class Dog(Animal):
    """Dog inherits from Animal."""

    def speak(self):
        return "Woof!"


class Cat(Animal):
    """Cat inherits from Animal."""

    def speak(self):
        return "Meow!"


class Car:
    """A class unrelated to Animal."""

    def __init__(self, brand):
        self.brand = brand


dog = Dog("Buddy")
cat = Cat("Whiskers")
car = Car("Toyota")
animal = Animal("Generic")

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))  # True because Dog inherits Animal.
print(isinstance(dog, Car))
print(isinstance(animal, Animal))
print(isinstance(animal, Dog))
print(isinstance(dog, (Dog, Cat)))
print(isinstance(dog, (Animal, Car)))
print(isinstance(car, (Animal, Car)))


# -----------------------------
# 18. Processing different types
# -----------------------------

def process_data(data, operation):
    """Process lists, tuples, dictionaries, and strings."""

    supported_types = (list, tuple, dict, str)

    if not isinstance(data, supported_types):
        raise TypeError(
            f"Unsupported data type: {type(data).__name__}"
        )

    if not isinstance(operation, str):
        raise TypeError("Operation must be a string.")

    if isinstance(data, (list, tuple)):
        if operation == "sum":
            # all() ensures every item is numeric.
            if all(
                isinstance(item, (int, float))
                and not isinstance(item, bool)
                for item in data
            ):
                return sum(data)

            raise ValueError("All elements must be numbers for sum.")

        elif operation == "length":
            return len(data)

        elif operation == "copy":
            return list(data)

        else:
            raise ValueError("Unknown list or tuple operation.")

    elif isinstance(data, dict):
        if operation == "keys":
            return list(data.keys())
        elif operation == "values":
            return list(data.values())
        elif operation == "items":
            return list(data.items())
        else:
            raise ValueError("Unknown dictionary operation.")

    elif isinstance(data, str):
        if operation == "uppercase":
            return data.upper()
        elif operation == "lowercase":
            return data.lower()
        elif operation == "length":
            return len(data)
        else:
            raise ValueError("Unknown string operation.")


print(process_data([1, 2, 3, 4], "sum"))
print(process_data((1, 2, 3), "length"))
print(process_data({"a": 1, "b": 2}, "keys"))
print(process_data("hello", "uppercase"))


# -----------------------------
# 19. User validation classes
# -----------------------------

class User:
    """Regular user."""

    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age


class Admin(User):
    """Admin is a specialized User."""

    def __init__(self, username, email, age, permissions):
        super().__init__(username, email, age)
        self.permissions = permissions


class Guest:
    """Guest user with a temporary session."""

    def __init__(self, session_id):
        self.session_id = session_id


def validate_and_process_user(user_data):
    """Validate and process User, Admin, or Guest objects."""

    if not isinstance(user_data, (User, Admin, Guest)):
        raise TypeError("Expected User, Admin, or Guest.")

    # Admin must be checked before User.
    # Admin is also an instance of User because it inherits User.
    if isinstance(user_data, Admin):
        if not isinstance(user_data.permissions, list):
            raise ValueError("Permissions must be a list.")

        if not all(
            isinstance(permission, str)
            for permission in user_data.permissions
        ):
            raise ValueError("Every permission must be a string.")

        print(f"Admin: {user_data.username}")
        print(f"Permissions: {user_data.permissions}")

        return f"Admin access granted to {user_data.username}"

    elif isinstance(user_data, User):
        if not isinstance(user_data.username, str):
            raise TypeError("Username must be a string.")

        if not isinstance(user_data.age, int):
            raise TypeError("Age must be an integer.")

        if user_data.age < 0:
            raise ValueError("Age cannot be negative.")

        print(f"Regular user: {user_data.username}")

        if user_data.age < 18:
            return f"User is a minor: {user_data.age}"
        else:
            return f"User is an adult: {user_data.age}"

    elif isinstance(user_data, Guest):
        if not isinstance(user_data.session_id, str):
            raise TypeError("Session ID must be a string.")

        if not user_data.session_id:
            raise ValueError("Session ID cannot be empty.")

        print(f"Guest session: {user_data.session_id}")
        return f"Guest access for {user_data.session_id}"


admin = Admin(
    "alice_admin",
    "alice@company.com",
    35,
    ["read", "write", "delete"],
)

user = User("bob_user", "bob@example.com", 25)
guest = Guest("session_12345")

print(validate_and_process_user(admin))
print(validate_and_process_user(user))
print(validate_and_process_user(guest))


# -----------------------------
# 20. Iterable, sequence, mapping
# -----------------------------

from collections.abc import Iterable, Mapping, Sequence


def process_collection(data):
    """Process common collection types."""

    if isinstance(data, Iterable):
        print(f"{data!r} is iterable.")

        if isinstance(data, Sequence):
            print(f"It is a sequence with length {len(data)}.")

        if isinstance(data, Mapping):
            print(f"It is a mapping with {len(data)} keys.")

    if isinstance(data, list):
        return [str(item) for item in data]

    elif isinstance(data, tuple):
        return tuple(str(item) for item in data)

    elif isinstance(data, dict):
        return {key: str(value) for key, value in data.items()}

    elif isinstance(data, str):
        return data.upper()

    elif isinstance(data, set):
        return {str(item) for item in data}

    else:
        return "Unknown collection type"


collections = [
    [1, 2, 3],
    (4, 5, 6),
    {"a": 1, "b": 2},
    "hello",
    {1, 2, 3},
    123,
]

for item in collections:
    print(f"Testing: {item!r}")
    print(f"Result: {process_collection(item)}")


# -----------------------------
# 21. Safe division
# -----------------------------

def is_real_number(value):
    """Return True only for int or float, excluding bool."""

    return isinstance(value, (int, float)) and not isinstance(
        value, bool
    )


def safe_divide(a, b):
    """Divide two real numbers safely."""

    if not is_real_number(a):
        raise TypeError("First argument must be numeric.")

    if not is_real_number(b):
        raise TypeError("Second argument must be numeric.")

    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")

    return a / b


def process_user_input(user_input):
    """Process None, strings, numbers, lists, tuples, and dictionaries."""

    if user_input is None:
        return "No input provided."

    if isinstance(user_input, str):
        if user_input.isdigit():
            return safe_divide(int(user_input), 2)

        return f"String: {user_input.upper()}"

    # Check bool before numeric values.
    elif is_real_number(user_input):
        return safe_divide(user_input, 2)

    elif isinstance(user_input, (list, tuple)):
        results = []

        for item in user_input:
            try:
                results.append(process_user_input(item))
            except (TypeError, ValueError, ZeroDivisionError) as error:
                results.append(f"Error: {error}")

        return results

    elif isinstance(user_input, dict):
        return {
            key: process_user_input(value)
            for key, value in user_input.items()
        }

    else:
        return f"Unsupported type: {type(user_input).__name__}"


test_inputs = [
    10,
    3.14,
    "42",
    "hello",
    [1, 2, 3, "4"],
    {"a": 10, "b": "20", "c": [1, 2]},
    None,
    True,
    (5, 6, 7),
]

for test_input in test_inputs:
    print(f"Input: {test_input!r}")
    print(f"Result: {process_user_input(test_input)}")


# -----------------------------
# 22. Dataclasses and Enum
# -----------------------------

from dataclasses import asdict, dataclass
from datetime import date, datetime
from enum import Enum


@dataclass
class Person:
    """Person data with runtime validation."""

    name: str
    age: int
    birth_date: date

    def __post_init__(self):
        if not isinstance(self.name, str):
            raise TypeError("Name must be a string.")

        if isinstance(self.age, bool) or not isinstance(self.age, int):
            raise TypeError("Age must be an integer.")

        if self.age < 0:
            raise ValueError("Age cannot be negative.")

        # datetime is a subclass of date, so reject it explicitly here.
        if not isinstance(self.birth_date, date):
            raise TypeError("Birth date must be a date.")

        if isinstance(self.birth_date, datetime):
            raise TypeError("Birth date must not be a datetime.")


class UserStatus(Enum):
    """Allowed account statuses."""

    ACTIVE = "active"
    INACTIVE = "inactive"
    BANNED = "banned"
    SUSPENDED = "suspended"


@dataclass
class UserAccount:
    """User account with field validation."""

    username: str
    email: str
    status: UserStatus
    person: Person
    created_at: datetime

    def __post_init__(self):
        if not isinstance(self.username, str):
            raise TypeError("Username must be a string.")

        if not self.username.strip():
            raise ValueError("Username cannot be empty.")

        if not isinstance(self.email, str):
            raise TypeError("Email must be a string.")

        if "@" not in self.email:
            raise ValueError("Email must contain '@'.")

        if not isinstance(self.status, UserStatus):
            raise TypeError("Status must be a UserStatus value.")

        if not isinstance(self.person, Person):
            raise TypeError("Person must be a Person object.")

        if not isinstance(self.created_at, datetime):
            raise TypeError("created_at must be a datetime.")


def validate_and_process_account(account):
    """Process an account according to its status."""

    if not isinstance(account, UserAccount):
        raise TypeError("Expected a UserAccount object.")

    if account.status == UserStatus.ACTIVE:
        return f"Active user: {account.username}"

    elif account.status == UserStatus.INACTIVE:
        return f"Inactive user: {account.username}"

    elif account.status == UserStatus.BANNED:
        return f"Banned user: {account.username}"

    elif account.status == UserStatus.SUSPENDED:
        return f"Suspended user: {account.username}"

    else:
        return f"Unknown status: {account.username}"


person = Person(
    name="John Doe",
    age=30,
    birth_date=date(1993, 5, 15),
)

account = UserAccount(
    username="johndoe",
    email="john@example.com",
    status=UserStatus.ACTIVE,
    person=person,
    created_at=datetime.now(),
)

print(validate_and_process_account(account))


# -----------------------------
# 23. API response and parser
# -----------------------------

import json
from typing import Any, Optional


@dataclass
class APIResponse:
    """Represent an API response."""

    status: str
    data: Optional[dict[str, Any]]
    message: str
    code: int

    def __post_init__(self):
        if not isinstance(self.status, str):
            raise TypeError("Status must be a string.")

        if self.data is not None and not isinstance(self.data, dict):
            raise TypeError("Data must be a dictionary or None.")

        if not isinstance(self.message, str):
            raise TypeError("Message must be a string.")

        if isinstance(self.code, bool) or not isinstance(self.code, int):
            raise TypeError("Code must be an integer.")

        if not 100 <= self.code <= 599:
            raise ValueError("Code must be an HTTP status code.")

    def to_json(self):
        """Convert the response into JSON text."""

        return json.dumps(asdict(self), default=str)


class DataParser:
    """Parse and validate several types of input."""

    @staticmethod
    def parse_input(input_data: Any) -> dict[str, Any]:
        """Parse input according to its type."""

        if input_data is None:
            return {"error": "No input provided"}

        if isinstance(input_data, str):
            try:
                parsed = json.loads(input_data)
            except json.JSONDecodeError:
                return {
                    "error": "Invalid JSON format",
                    "data": input_data,
                }

            return DataParser._process_parsed_data(parsed)

        elif isinstance(input_data, dict):
            return DataParser._process_parsed_data(input_data)

        elif isinstance(input_data, list):
            results = [
                DataParser.parse_input(item)
                for item in input_data
            ]

            return {"results": results}

        # bool is checked before int because bool inherits from int.
        elif isinstance(input_data, bool):
            return {
                "value": input_data,
                "type": "bool",
            }

        elif isinstance(input_data, (int, float)):
            return {
                "value": input_data,
                "type": type(input_data).__name__,
            }

        else:
            return {
                "error": (
                    "Unsupported input type: "
                    f"{type(input_data).__name__}"
                )
            }

    @staticmethod
    def _process_parsed_data(data: Any) -> dict[str, Any]:
        """Validate a dictionary containing id, name, and value."""

        if not isinstance(data, dict):
            return {
                "valid": False,
                "error": "JSON value must be an object.",
            }

        required_fields = {"id", "name", "value"}
        missing_fields = required_fields - data.keys()

        if missing_fields:
            return {
                "valid": False,
                "error": (
                    "Missing fields: "
                    f"{sorted(missing_fields)}"
                ),
            }

        id_value = data["id"]
        name_value = data["name"]
        value_value = data["value"]

        if isinstance(id_value, bool) or not isinstance(
            id_value, (int, str)
        ):
            return {
                "valid": False,
                "error": "ID must be an integer or string.",
            }

        if not isinstance(name_value, str):
            return {
                "valid": False,
                "error": "Name must be a string.",
            }

        if isinstance(value_value, bool) or not isinstance(
            value_value, (int, float)
        ):
            return {
                "valid": False,
                "error": "Value must be a number.",
            }

        return {
            "valid": True,
            "data": {
                "id": id_value,
                "name": name_value,
                "value": value_value,
                "processed_at": datetime.now().isoformat(),
            },
        }


parser = DataParser()

test_cases = [
    None,
    '{"id": 1, "name": "Test", "value": 42}',
    '{"id": "abc", "name": "Invalid", "value": "wrong"}',
    {"id": 2, "name": "Dict Test", "value": 99.9},
    [
        {"id": 3, "name": "Item 1", "value": 10},
        {"id": 4, "name": "Item 2", "value": 20},
    ],
    42,
    True,
    "plain string",
]

for test_case in test_cases:
    print(f"Input: {test_case!r}")
    print(f"Result: {parser.parse_input(test_case)}")


response = APIResponse(
    status="success",
    data={"id": 1, "name": "API Test", "value": 100},
    message="Data processed successfully",
    code=200,
)

print(response.to_json())