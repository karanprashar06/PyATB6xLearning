try:
    x = int(input("Enter number: "))
    result = 10 / x
except ValueError:
    print("❌ Not a valid number.")
except ZeroDivisionError:
    print("⚠️ Division by zero not allowed.")
else:
    print(f"✅ Result: {result}")
finally:
    print("🔚 Done executing.")
