def add(a, b):
    """Adds two numbers."""
    return a + b

def subtract(a, b):
    """Subtracts two numbers."""
    return a - b

def multiply(a, b):
    """Multiplies two numbers."""
    return a * b

def divide(a, b):
    """Divides two numbers."""
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero"

print("Welcome in our Simple calculator...!! \nLet's Perfom Some Operations..")
while True:
    try:
        num1 = float(input("Enter Your First Number: "))  # Use float for decimal numbers
        num2 = float(input("Enter Your Second number: ")) 
        ope = input("Enter Operator (+, -, *, /): ")  # Use standard operator symbols

        if ope == "+":
            result = add(num1, num2)
        elif ope == "-":
            result = subtract(num1, num2)
        elif ope == "*":
            result = multiply(num1, num2)
        elif ope == "/":
            result = divide(num1, num2)
        else:
            print("Invalid Operator. Please try again.")
            continue

        print(f"Result of {num1} and {num2} is {result} .") 
        

        choice = input("Do you want to perform another calculation? (y/n): ")
        if choice.lower() != 'y':
            print("Thank You..!!")
            break
    except ValueError:
        print("Invalid input. Please enter numbers only.")

    
