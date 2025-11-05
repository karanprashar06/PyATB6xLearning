import time
import random

# Customizable max wait time (edge case: test various values)
MAX_WAIT = 5
wait_time = 0
page_loaded = False

def api_response():
    # Edge case: Might return unexpected values
    result = random.choice([False, True, None, "loaded"])
    return result

while wait_time < MAX_WAIT:
    response = api_response()

    # Validate response is a boolean
    if response is True:
        page_loaded = True
        print(f"✅ Page loaded successfully in {wait_time + 1} second(s).")
        break
    else:
        print(f"⏳ Checking... (second {wait_time + 1}) - Response: {response}")
        time.sleep(random.uniform(0.5, 1.5))  # random realistic delay
        wait_time += 1

if not page_loaded:
    print(f"❌ Timeout! Page failed to load within {MAX_WAIT} seconds.")
