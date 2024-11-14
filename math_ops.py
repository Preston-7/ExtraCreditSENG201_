# math_operations.py

def divide_numbers(a, b):
    """Divides two numbers and returns the result."""
    if b == 0:
        print("Cannot divide by 0.")
    else:
        return a / b  

def multiply_numbers(a, b):
    """Multiplies two numbers and returns the result."""
    return a*b

if __name__ == "__main__":
    x = 10
    y = 0
    result = divide_numbers(x, y)
    print(f"The result of division is: {result}")
    result_multiply = multiply_numbers(x, y)
    print(f"The result of multiplication is: {result_multiply}")
