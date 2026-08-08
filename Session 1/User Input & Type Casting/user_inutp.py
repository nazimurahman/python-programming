"""
Use Input:
 -> In python we use input() for getting the input.
 -> User input in Python is always received as a string by default.
 -> NOTE:
    -> Always return string(even for numbers)
    -> can display a prompt message
    -> Execution pauses untill user press the input
    -> To get specific input, you must cast the results 
"""



# Understanding input() Function
# Basic input - always returns a string
user_input = input("Enter something: ")
print(f"You entered: {user_input}")
print(f"Data type: {type(user_input)}")  # Output: <class 'str'>

# Converting String Input to Integer (int())
# Use int() when you need whole numbers for calculations
age_input = input("Enter your age: ")
print(f"Before conversion: {age_input} (type: {type(age_input)})")

# Convert string to integer
age_int = int(age_input)  # Will raise ValueError if input is not a number
print(f"After conversion: {age_int} (type: {type(age_int)})")
print(f"Age + 10 = {age_int + 10}")  # Now we can perform mathematical operations



# Converting String Input to Float (float())
# Use float() when you need decimal numbers
temperature = input("Enter temperature in Celsius: ")
temp_float = float(temperature)  # Convert to float for decimal calculations

# Perform calculation with the converted value
fahrenheit = (temp_float * 9/5) + 32



# Converting String input to Boolean (bool()) -> (strings convert differently)
response = input("Do you agree? (yes/no): ")
is_agreed = bool(response)  # Any non-empty string = True
print(f"Your response as boolean: {is_agreed}")

# Better approach: Custom boolean conversion
def str_to_bool(value):
    """
    Convert string to boolean with specific logic.
    This is more reliable than bool() for user inputs.
    """
    # Convert to lowercase for case-insensitive comparison
    value_lower = value.lower()
    
    # Check for affirmative responses
    if value_lower in ['yes', 'true', 'y', '1', 'ok', 'sure']:
        return True
    # Check for negative responses
    elif value_lower in ['no', 'false', 'n', '0', 'cancel']:
        return False
    else:
        # Fallback: any non-empty string returns True
        return bool(value)

user_response = input("Do you accept terms? (yes/no): ")
result = str_to_bool(user_response)
print(f"Boolean result: {result}")

# Converting String to List (split())
# Use split() to break a string into multiple parts
user_input = input("Enter numbers separated by space (e.g., 10 20 30): ")

# split() creates a list of strings
numbers_list = user_input.split()
print(f"List of strings: {numbers_list}")

# Convert each string to float using map()
# map() applies a function to each element in the list
num1, num2 = map(float, user_input.split())  # Unpack first two values
print(f"First number: {num1}, Second number: {num2}")
print(f"Sum: {num1 + num2}")

# SECURE INPUT WITH GETPASS (Hidden Password Entry)
from getpass import getpass
# getpass() hides the input for security (useful for passwords)
password = getpass("Enter Password: ")  # Characters won't be displayed
print(f"Password entered (length): {len(password)} characters")
# Never print actual passwords in production!



# Getting Valid Integer with Error Handling
def get_valid_integer(prompt):
    """
    Get a valid integer from user with error handling.
    Uses try-except to catch ValueError when conversion fails.
    """
    while True:  # Keep asking until valid input is received
        try:
            # Attempt to convert input to integer
            value = int(input(prompt))
            return value  # Exit function if successful
        except ValueError:
            # This runs if int() conversion fails
            print(" Error: Please enter a valid integer.")

# Usage example
age = get_valid_integer("Enter your age: ")
print(f"Valid age: {age}")

# Getting Integer Within Specific Range
def get_integer_in_range(prompt, min_val, max_val):
    """
    Get integer within specific range.
    Validates both data type AND value range.
    """
    while True:
        try:
            # First, get a valid integer
            value = int(input(prompt))
            
            # Then check if it's within range
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Please enter a number between {min_val} and {max_val}")
                
        except ValueError:
            print("Please enter a valid integer.")

# Usage example
score = get_integer_in_range("Enter score (0-100): ", 0, 100)
print(f"Valid score: {score}")


# Getting Valid Float with Error Handling
def get_valid_float(prompt):
    """
    Get a valid float from user.
    Useful for decimal numbers and measurements.
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Error: Please enter a valid number (e.g., 3.14)")

# Usage example
price = get_valid_float("Enter product price: $")
print(f"Valid price: ${price:.2f}")  # Format to 2 decimal places



# Handling Multiple Inputs with Validation
def get_multiple_numbers(prompt, count):
    """
    Get exactly 'count' numbers from user input.
    Handles cases where user enters too many or too few numbers.
    """
    while True:
        try:
            # Get input and split into list
            user_input = input(prompt)
            numbers = list(map(float, user_input.split()))
            
            # Check if we got exactly the required count
            if len(numbers) != count:
                print(f"Please enter exactly {count} numbers")
                continue
                
            return numbers
            
        except ValueError:
            print("Please enter valid numbers only")

# Usage example
nums = get_multiple_numbers("Enter 3 numbers separated by space: ", 3)
print(f"Numbers entered: {nums}")
print(f"Sum: {sum(nums)}")
print(f"Average: {sum(nums)/len(nums):.2f}")


# Getting Yes/No Confirmation
def get_confirmation(prompt):
    """
    Get a yes/no confirmation from user.
    Returns True for 'yes', False for 'no'.
    """
    while True:
        response = input(prompt + " (yes/no): ").lower()
        if response in ['yes', 'y', 'yeah', 'sure']:
            return True
        elif response in ['no', 'n', 'nope', 'cancel']:
            return False
        else:
            print("Please answer 'yes' or 'no'")

# Usage example
confirmed = get_confirmation("Do you want to continue?")
print(f"User confirmed: {confirmed}")

# COMPLETE USER REGISTRATION

def register_user():
    """
    Complete example combining all input techniques.
    Demonstrates how to handle a complex user input scenario.
    """
    print("\n" + "=" * 50)
    print("USER REGISTRATION FORM")
    print("=" * 50)
    
    # Get name (string)
    name = input("Enter your full name: ").strip()
    while not name:  # Check if name is empty
        print("❌ Name cannot be empty")
        name = input("Enter your full name: ").strip()
    
    # Get age (integer with range validation)
    age = get_integer_in_range("Enter your age (13-120): ", 13, 120)
    
    # Get email (basic string validation)
    email = input("Enter your email: ").strip()
    while '@' not in email or '.' not in email:
        print("❌ Please enter a valid email (must contain @ and .)")
        email = input("Enter your email: ").strip()
    
    # Get password securely
    password = getpass("Enter your password: ")
    while len(password) < 8:
        print("❌ Password must be at least 8 characters")
        password = getpass("Enter your password: ")
    
    # Get confirmation
    agrees = get_confirmation("Do you agree to our terms?")
    
    # Display summary
    print("\n" + "=" * 50)
    print("REGISTRATION COMPLETE!")
    print("=" * 50)
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Email: {email}")
    print(f"Password length: {len(password)} characters")
    print(f"Terms accepted: {agrees}")
    print("=" * 50)
    
    return {
        'name': name,
        'age': age,
        'email': email,
        'terms_accepted': agrees
    }

user_data = register_user()