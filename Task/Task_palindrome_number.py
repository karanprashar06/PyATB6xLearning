input_number = int(input("Enter a number: "))

reverse = int(str(input_number)[::-1])

print("palindrome" if input_number == reverse else "not palindrome" )