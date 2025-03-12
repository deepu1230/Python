def arithmetic_operations(num1, num2, operator):  
    """  
    Performs arithmetic operations based on the given operator.  

    Args:  
        num1 (float): The first number.  
        num2 (float): The second number.  
        operator (str): The operator to perform (+, -, *, /).  

    Returns:  
        float: The result of the arithmetic operation.  
               Returns None if the operator is invalid or if division by zero occurs.  
    """  
    if operator == '+':  
        return num1 + num2  
    elif operator == '-':  
        return num1 - num2  
    elif operator == '*':  
        return num1 * num2  
    elif operator == '/':  
        if num2 == 0:  
            print("Error: Division by zero is not allowed.")  
            return None  
        return num1 / num2  
    else:  
        print("Error: Invalid operator. Please use +, -, *, or /.")  
        return None  

# Example usage:  
result = arithmetic_operations(10, 5, '+')  
print("Result of addition:", result)  

result = arithmetic_operations(10, 5, '-')  
print("Result of subtraction:", result)  

result = arithmetic_operations(10, 5, '*')  
print("Result of multiplication:", result)  

result = arithmetic_operations(10, 5, '/')  
print("Result of division:", result)  

result = arithmetic_operations(10, 0, '/')  
print("Result of division by zero:", result)  

result = arithmetic_operations(10, 5, '%')  
print("Result of invalid operator:", result)