from dotenv import load_dotenv
import os

class loginPage:
    def __init__(self,email_arg,password_arg):
        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        load_dotenv()
        if self.email ==os.getenv("USERNAME") and self.password ==os.getenv("PASSWORD"):
            print("Login Successfull")
        else:
            print("Login Failed")

email = input("Enter Email Address: ")
password = input("Enter Password: ")

login = loginPage(email,password)
login.login_confirm()

#print(os.name)