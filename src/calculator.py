class Calculator:
    """A simple calculator utility for demonstration and testing purposes."""

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b

    def power(self, base, exp):
        return base ** exp

    def is_even(self, n):
        return n % 2 == 0
