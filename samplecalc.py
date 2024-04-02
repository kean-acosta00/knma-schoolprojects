print("MDAS CALCULATOR | BY ACOSTA")
print()

# Arithmetic operations
def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Cannot be divided by zero."
    else:
        return a / b

# Calculator definition and list
operations = {
    '1': add,
    '2': subtract,
    '3': multiply,
    '4': divide
}

# Function to display dictionary options
def display_operations():
    print("Select operation:")
    print()
    dOperations = [(1, "Add"), (2, "Subtract"), (3, "Multiply"), (4, "Divide")]
    for d1, d2 in dOperations:
        print(f"{d1} - {d2}")

def calculator():
    display_operations()

    # Choices and results
    choice = input("Enter choice (1 | 2 | 3 | 4): ")

    if choice in operations: 
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = operations[choice](num1, num2)
        print("Result:", result)

        tryAgain = input("Do you want to try again? (yes | no): ")
        if tryAgain.lower() == 'yes':
            calculator()
        else:
            print("Thank you for using this program.")
    else:
        print("Invalid input.")

calculator()