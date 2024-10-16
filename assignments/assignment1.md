# Assignment 1: Basic Calculator

## Objective
Create a basic calculator that can perform the following operations: addition, subtraction, multiplication, and division.

## Requirements
1. Write a function `calculate` that takes three parameters: `a`, `b`, and `operation`.
2. The `operation` parameter can be one of the following strings: `"add"`, `"subtract"`, `"multiply"`, or `"divide"`.
3. The function should return the result of the operation.
4. If the operation is not recognized, return `"Invalid operation"`.

## Example
```python
calculate(10, 5, "add")      # Returns 15
calculate(10, 5, "subtract")  # Returns 5
calculate(10, 5, "multiply")  # Returns 50
calculate(10, 5, "divide")    # Returns 2.0
calculate(10, 5, "modulus")    # Returns "Invalid operation"
