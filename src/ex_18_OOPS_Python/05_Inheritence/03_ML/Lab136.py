#Mutlilevel inheritance
from unittest import TestCase


class TestSuite:
    def info(self):
        print("This is GF- Step1")

class BaseTest(TestSuite):
    def setUp(self):
        print("This is F- Step2")

class MyTestCase(BaseTest):
    def run(self):
        self.info()
        self.setUp()
        print("This is S- Step3")

test = MyTestCase()
test.run()