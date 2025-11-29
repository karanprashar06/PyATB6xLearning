class BaseTest:
    def setup(self):
        print("Setup from BaseTest")


class LoginTest(BaseTest):
    def run(self):
        print("Running Login Test")


class SignupTest(BaseTest):
    def run(self):
        print("Running Signup Test")


LoginTest().setup()
LoginTest().run()
SignupTest().setup()
SignupTest().run()

test1 = SignupTest()
test1.setup()
test1.run()
