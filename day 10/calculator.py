


""" def add(a,b):
    return a + b

def substract(a,b):
    return a - b

def divide(a,b):
    return a / b

def multiply(a,b):
    return a * b

f_number = int(input("What your first number?:"))
continue_calculation = True
while continue_calculation:
    operation = input("enter your operator:")
    n_number = int(input("What your next number?:"))

    if operation == '+':
        result = add(f_number,n_number)
        print(f'{f_number} {operation} {n_number} = {result}')
    elif operation == '-':
        result = substract(f_number,n_number)
        print(f'{f_number} {operation} {n_number} = {result}')
    elif operation == '/':
        result = divide(f_number,n_number)
        print(f'{f_number} {operation} {n_number} = {result}')
    elif operation == '*':
        result = multiply(f_number,n_number)
        print(f'{f_number} {operation} {n_number} = {result}')
    else:
        print("Invalid input")        
    continue_cal = input(f"Type 'y' to continue calculating with {result} or 'n' to start new calculation:").lower()
    if continue_cal == 'y':
        pass
        
    elif continue_cal == 'n':
        continue_calculation = False """
        

def add(a,b):
    return a + b

def substract(a,b):
    return a - b

def divide(a,b):
    return a / b

def multiply(a,b):
    return a * b

operations = {
    '+':add,
    '-':substract,
    '*':multiply,
    '/':divide,
}

def calculator():
    f_number = int(input("What your first number?:"))
    for symbol in operations:
        print(symbol)

    continue_cal = True
    while continue_cal:
        operation_cal = input("enter your operator:")
        n_number = int(input("Enter the next number: "))
        calculation = operations[operation_cal]
        answer = calculation(f_number,n_number)
        print(f'{f_number} {operation_cal} {n_number} = {answer}')
        cal_yes = input(f"Do you want to continue calculations with {answer}? Type 'y' or 'n' to exit:").lower()
        if cal_yes == 'y':
            f_number = answer
        elif cal_yes == 'n':
            continue_cal = False
            calculator()

calculator()