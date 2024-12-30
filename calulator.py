import math
class ScientificCalculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    def power(self, a, b):
        return a ** b
    def square_root(self, a):
        if a < 0:
            raise ValueError("Cannot take the square root of a negative number")
        return math.sqrt(a)
    def sine(self, angle):
        return math.sin(math.radians(angle))
    def cosine(self, angle):
        return math.cos(math.radians(angle))
    def tangent(self, angle):
        return math.tan(math.radians(angle))
# Example usage:
calculator = ScientificCalculator()
# Basic arithmetic operations
print("Addition:", calculator.add(5, 3))
print("Subtraction:", calculator.subtract(5, 3))
print("Multiplication:", calculator.multiply(5, 3))
print("Division:", calculator.divide(5, 3))
# Scientific functions
print("Power:", calculator.power(2, 3))
print("Square Root:", calculator.square_root(16))
print("Sine:", calculator.sine(30))
print("Cosine:", calculator.cosine(60))
print("Tangent:", calculator.tangent(45))