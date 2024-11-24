def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


operators_list = ("+","-","*","/")

while True:
    choice = input("Enter math symbol [+,-,*,/]: ")

    if choice in operators_list:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
    
    match choice:
        case "+":
            print(f'Answer: {add(num1, num2)}')
        case "-":
            print(f'Answer: {subtract(num1, num2)}')
        case "*":
            print(f'Answer: {multiply(num1, num2)}')
        case "/":
            try:
                print(f'Answer: {divide(num1, num2)}')
            except ZeroDivisionError:
                print(f'Numbers cannot be divided by zero')


