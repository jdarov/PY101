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

def print_result(the_result):
    """
    print_result(result) prints the result of the operation
    rounds a float to 2 decimal places for cleaner looking result
    """
    if isinstance(the_result, (int, float)):
        return f'The result is {round(the_result, 2)}'
    return the_result

def return_answer(this_operation, num1, num2):
    """
    Take the user input and return the answer of the input
    Returns error message if attempt divide by 0
    """
    match this_operation:
        case '1':
            return num1 + num2
        case '2':
            return num1 - num2
        case '3':
            return num1 * num2
        case '4':
            try:
                return num1 / num2
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
        this_operation = input(prompt)
        if this_operation in valid_operations:
            return this_operation
        print("Invalid operation: Please select 1, 2, 3, or 4")

def point_to_prompt(prompt):
    return f'==> {prompt}'

#main program body

print(point_to_prompt('Welcome to the Calculator!'))

PROMPT_1 = "What's the first number?\n"
PROMPT_2 = "What's the second number?\n"

number1 = check_for_number(point_to_prompt(PROMPT_1))
number2 = check_for_number(point_to_prompt(PROMPT_2))

print(f'{number1}, {number2}')

OPERATION_PROMPT_1 = "What operation would you like to perform?\n"
OPERATION_PROMPT_2 = "1) Add 2) Subtract 3) Multiply 4) Divide\n"

operation = ask_for_operation(OPERATION_PROMPT_1 + OPERATION_PROMPT_2)
result = return_answer(operation, number1, number2)

print(print_result(result))
