class LoginPage:

    def __init__(self, email_arg,password_arg):
        self.email_arg = email_arg
        self.password_arg = password_arg

    def login_confirm(self):
        if self.email_arg =="karan@gmail.com" and self.password_arg =="123":
            print("Login Confirmed")
        else:
            print("Login Failed")

email = input("Enter Email Address: ")
password = input("Enter Password: ")
login = LoginPage(email,password)
login.login_confirm()