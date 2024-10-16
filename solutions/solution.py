def calculate(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operation"

# Example usage
if __name__ == "__main__":
    print(calculate(10, 5, "add"))       # Output: 15
    print(calculate(10, 5, "subtract"))  # Output: 5
    print(calculate(10, 5, "multiply"))  # Output: 50
    print(calculate(10, 5, "divide"))    # Output: 2.0
    print(calculate(10, 5, "modulus"))    # Output: "Invalid operation"
