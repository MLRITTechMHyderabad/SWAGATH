def calculator(a, b, operator):
    
    try:
        
        if type(a) not in [int, float] or type(b) not in [int, float]:
            return "Error: Inputs must be numbers"

       
        if operator == "+":
            return a + b
        elif operator == "-":
            return a - b
        elif operator == "*":
            return a * b
        elif operator == "/":
            if b == 0:
                return "Error: Cannot divide by zero"
            return a / b
        elif operator == "%":
            if b == 0:
                return "Error: Cannot divide by zero"
            return a % b
        elif operator == "**":
            return a ** b
        else:
            return "Error: Unsupported operator"

    except Exception as e:
        return f"Error: {e}"


print(calculator(10, 0, "/"))  
print(calculator(10, "five", "+"))  
print(calculator(10, 5, "$"))  
print(calculator(10, 3, "**"))  
print(calculator(10, 2, "%"))  
