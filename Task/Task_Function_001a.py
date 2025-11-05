attempt = 1
max_attempt = 3
response = None

while attempt <= max_attempt:
    try:
        response = int(input(f"Attempt {attempt}/{max_attempt} - Enter Response: "))
    except ValueError:
        print("❌ Invalid input! Please enter a number.")
        attempt += 1
        continue

    if response == 200:
        print("✅ Test Passed")
        break
    attempt += 1

if response != 200:
    print("❌ Test Failed after 3 attempts.")