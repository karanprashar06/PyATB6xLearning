from unittest import case

print("Enter which test You want to run")
test_type  = input("Enter the Test Type : API, UI, Performance, Security ")

match test_type:
    case "API":
        print("API")
    case "UI":
        print("UI")
    case "Performance":
        print("Performance")
    case "Security":
        print("Security")
    case _:
        print("Invalid input")