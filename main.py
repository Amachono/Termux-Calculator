from colorama import Fore, Style, init
import math

init(autoreset=True)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero!"

def parse_value(value):
    if value == 'π':
        return math.pi
    elif value == '∞':
        return float('inf')
    else:
        return float(value)

def calculate_expression(expression):
    tokens = expression.split()
    result = parse_value(tokens[0])
    current_operation = None

    for token in tokens[1:]:
        if token in "+-*/":
            current_operation = token
        else:
            value = parse_value(token)
            if current_operation == '+':
                result = add(result, value)
            elif current_operation == '-':
                result = subtract(result, value)
            elif current_operation == '*':
                result = multiply(result, value)
            elif current_operation == '/':
                result = divide(result, value)
            else:
                result = value

    return result

def main():
    print(Fore.GREEN + "Welcome to the text calculator!")
    print(Fore.YELLOW + "This calculator supports the following operations:")
    print(Fore.CYAN + "+ : Addition")
    print(Fore.CYAN + "- : Subtraction")
    print(Fore.CYAN + "* : Multiplication")
    print(Fore.CYAN + "/ : Division")
    print(Fore.MAGENTA + "π : Constant π (3.14159)")
    print(Fore.MAGENTA + "∞ : Infinity")
    
    print(Fore.YELLOW + "\nInput examples:")
    print(Fore.CYAN + "1. Addition: 5 + 3 (Result: 8.0)")
    print(Fore.CYAN + "2. Addition with π: 7 + π (Result: 10.14159)")
    print(Fore.CYAN + "3. Subtraction: 10 - 4 (Result: 6.0)")
    print(Fore.CYAN + "4. Multiplication: 7 * 6 (Result: 42.0)")
    print(Fore.CYAN + "5. Division: 8 / 2 (Result: 4.0)")
    print(Fore.CYAN + "6. Mixed operations: 89 - 18 + 81 - 19 (Result: 133.0)")
    
    while True:
        command = input(Fore.BLUE + "Enter command (or 'exit' to quit): ")

        if command.lower() == 'exit':
            print(Fore.RED + "Exiting calculator. Goodbye!")
            break

        try:
            result = calculate_expression(command)
            print(Fore.GREEN + f"Result: {result}")
        except ValueError:
            print(Fore.RED + "Error: Please enter valid numbers or symbols!")
        except Exception as e:
            print(Fore.RED + f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()