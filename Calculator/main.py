from art import calculator_3d_logo
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
print(calculator_3d_logo)

def calculator():
    num1 = float(input("What's the first number that you want to enter?\n"))
    for key in operations:
        print(key)
    
    continueCalculation = True

    while continueCalculation:
        operator = input("What's the operation that you want to perform?")
        num2 = float(input("What is the next number that you want to enter?\n"))
        calculation_function = operations[operator]
        answer = calculation_function(num1, num2)
        
        print(f"{num1} {operator} {num2} = {answer}")
        
        if input(f"Type 'y' to continue calculating with {answer}: or 'n' to restart the calculator") == 'y':
            num1 = answer
        else:
            print("Invalid operator. Please choose a valid operator from +, -, *, or /")
            continueCalculation = False

    calculator()  # Recursive call moved outside the while loop

calculator()
