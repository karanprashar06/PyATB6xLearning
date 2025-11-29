class Bank:
    def __init__(self, account_number,balance):
        self.__account = account_number
        self.balance = balance

    def check_balance(self):
        print(self.balance)

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def show_me_account_number(self,is_auth):
        if is_auth == True:
            print(self.__account)
        else:
            print("Not allowed")

icici = Bank("984809872070",100)
icici.check_balance()
ok= icici.deposit(100)
print(ok)
okk = icici.withdraw(20)
print(okk)

icici.show_me_account_number(False)
icici.show_me_account_number(True)