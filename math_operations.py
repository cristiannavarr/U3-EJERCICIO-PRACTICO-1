import math

def add_numbers(a, b):
    # Add two numbers
    result = a + b
    return round(result, 2) 

def subtract_numbers(a, b):
    # Subtract two numbers (a - b)
    result = a - b
    return round(result, 2) 

def multiply_numbers(a, b):
    # Multiply two numbers
    result = a * b
    return round(result, 2)

def divide_numbers(a, b):
    # Divide two numbers (a ÷ b)
    if b == 0:
        return None
    result = a / b
    return round(result, 2)  

MAX_FLOAT = 1.797e308
LOG_MAX = math.log(MAX_FLOAT)

def power_numbers(a, b):
    # Check size without computing a ** b
    if a > 0 and b * math.log(a) > LOG_MAX:
        return "Result too large"
    
    result = a ** b
    return round(result, 2)


def calculate(operation, num1, num2):
    # Choose which math operation to do based on the operation code
    if operation == 'SUM':
        return add_numbers(num1, num2)
    elif operation == 'SUB':
        return subtract_numbers(num1, num2)
    elif operation == 'MUL':
        return multiply_numbers(num1, num2)
    elif operation == 'DIV':
        return divide_numbers(num1, num2)
    elif operation == 'POW':
        return power_numbers(num1, num2)
