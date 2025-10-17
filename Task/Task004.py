response_code = 200

if response_code == 200:
    print("Passed API Request")
else:
    print("Failed API Request")


# Expected and actual values
expected_title = "Dashboard"
actual_title = "Dashboard "

# Normalize both strings by stripping spaces and converting to lowercase
if expected_title.strip().lower() == actual_title.strip().lower():
    print("Test Passed – Title matches")
else:
    print("Test Failed – Title does not match")


# Page load time in seconds
load_time = 4.2

# Check performance condition
if load_time <= 3:
    print(f"Page loaded successfully in {load_time} seconds")
else:
    print(f"Page load too slow: {load_time} seconds")

# Input credentials
username = "admin"
password = "1234"

# Check login validity
if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Credentials")