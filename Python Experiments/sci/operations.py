import math


class Operators:
    def __init__(self, num1=0, num2=10.0):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        print(self.num1 + self.num2)

    def add(self, a=0):
        print(self.num1 + self.num2 + a)

    def subtraction(self):
        print(self.num1 - self.num2)

    def multiply(self):
        print(self.num1 * self.num2)

    def divide(self):
        print(self.num1 / self.num2)

    def floordiv(self):
        print(self.num1 // self.num2)

    def mod(self):
        print(self.num1 % self.num2)

    def exponent(self):
        print(self.num1 ** self.num2)

    def root(self):
        print(self.num1 ** (self.num2 ** -1))

    def log(self):
        print(math.log(self.num1, self.num2))
