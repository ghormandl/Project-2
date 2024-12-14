import math

class CalculatorLogic:
    def __init__(self):
        self.current_input = ""

    def update_input(self, input_text):
        """Update the current input with the button pressed."""
        if self.current_input == "0":
            self.current_input = input_text
        else:
            self.current_input += input_text
        return self.current_input

    def clear_input(self):
        """Clear the current input."""
        self.current_input = ""
        return self.current_input

    def evaluate_expression(self):
        """Evaluate the current mathematical expression."""
        try:
            result = eval(self.current_input)
            self.current_input = str(result)
            return self.current_input
        except Exception as e:
            self.current_input = "Error"
            return self.current_input

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Error"

    def square_area(self, side):
        """Calculate the area of a square given the side length."""
        return side ** 2

    def rectangle_area(self, length, width):
        """Calculate the area of a rectangle."""
        return length * width

    def circumference(self, radius):
        """Calculate the circumference of a circle."""
        return 2 * math.pi * radius