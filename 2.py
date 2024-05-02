# Write a program to create a class to perform calculator functions

class Calculator:

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if(b == 0):
            return "Division by zero not allowed"
        else:
            return a / b


calc = Calculator()
print(calc.add(1, 2))
print(calc.sub(1, 2))
print(calc.mul(2, 3))
print(calc.div(1, 2))
print(calc.div(1, 0))
