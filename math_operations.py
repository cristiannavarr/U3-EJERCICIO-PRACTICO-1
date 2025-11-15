import math

def add_numbers(a, b):
    # Suma
    result = a + b
    return round(result, 2) 

def subtract_numbers(a, b):
    # Resta
    result = a - b
    return round(result, 2) 

def multiply_numbers(a, b):
    # Multiplicación
    result = a * b
    return round(result, 2)

def divide_numbers(a, b):
    # División
    if b == 0:
        return None
    result = a / b
    return round(result, 2)  

MAX_FLOAT = 1.797e308
LOG_MAX = math.log(MAX_FLOAT)

def power_numbers(a, b):
    # Se revisa si puede existir overflow debido al tamaño de los números
    if a > 0 and b * math.log(a) > LOG_MAX:
        return "Resultado demasiado grande"
    
    result = a ** b
    return round(result, 2)


def calculate(operation, num1, num2):
    # Se determina que operación realizar
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
