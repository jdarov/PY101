def check_for_number(prompt):
    """
    def check_for_number(prompt) to check if user input as an actual number
    if not a number then returns an error message and asks again
    """
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print('This is not a valid number. Please enter a number')

def print_result(result):
    """
    print_result(result) prints the result of the numbers after performing operation
    rounds a float to 2 decimal places for cleaner looking result
    """
    return f'The result is {round(result, 2)}' if isinstance(result, (int, float)) else result

def return_answer(operation, number1, number2):
    """
    def return_answer to take the user input and return the answer of the input
    catches an error and prints message if user tries illegal operation divide by 0
    """
    match operation:
        case '1':
            return number1 + number2
        case '2':
            return number1 - number2
        case '3':
            return number1 * number2
        case '4':
            try:
                return number1 / number2
            except ZeroDivisionError:
                return 'Cannot divide by zero!'
        case _:
            return ''

def ask_for_operation(prompt):
    """
    Prompts the user for an operation and checks if input valid
    If invalid input from user, prints Invalid and repeats prompt
    """
    valid_operations = {'1', '2', '3', '4'}
    while True:
        operation = input(prompt)
        if operation in valid_operations:
            return operation
        else:
            print("Invalid operation: Please select 1, 2, 3, or 4")


#main program body

print('Welcome to the Calculator!')

number1 = check_for_number("What's the first number? ")
number2 = check_for_number("What's the second number? ")

print(f'{number1}, {number2}')

operation = ask_for_operation("What operation would you like to perform?\n1) Add 2) Subtract 3) Multiply 4) Divide\n")
result = return_answer(operation, number1, number2)

print(print_result(result))