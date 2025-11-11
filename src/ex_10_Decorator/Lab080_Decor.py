def before_after_ui_test(func):

    def wrapper():
        print("Before After UI Test")
        func()
        print("After UI Test")
    return wrapper

@before_after_ui_test
def test_ui():
    print("Hi Testing done")

test_ui()