
#TASK
status_code = int(input("Please enter a status code: "))
def check_status(status_code):
    match status_code:
        case 200:
            return "PASS"
        case 400:
            return "FAIL"
        case 500:
            return "FAIL"
        case _:
            return "UNKNOWN"



#. Calling a function
result = check_status(status_code)
print(result)