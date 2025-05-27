from calculator_messages_loader import calc_messages, get_calc_msg

ASK_LANG = "Enter language code (default 'en', 'fr', 'es', 'de', 'it'): "
lang = input(ASK_LANG).strip().lower()
calc_lang = calc_messages(lang)

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
            print(get_calc_msg(calc_lang, 'invalid_number'))

def print_result(the_result):
    """
    print_result(result) prints the result of the operation
    rounds a float to 2 decimal places for cleaner looking result
    """
    if isinstance(the_result, (int, float)):
        return get_calc_msg(calc_lang,'result').format(round(the_result, 2))
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
                return get_calc_msg(calc_lang, 'divide_by_zero')
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
        print(get_calc_msg(calc_lang, 'invalid_operation'))

def point_to_prompt(prompt):
    """
    Simple function to point to selected prompts
    Help to distinguish from user input
    """
    return f'==> {prompt}'

def validate_continue(prompt):
    """
    Asks user if they wish to continue using the calculator
    Returns the valid input 'y' or 'n'
    If input invalid, prints invalid msg and repeat
    """
    print(get_calc_msg(calc_lang, 'continue_question'))
    other_prompt = get_calc_msg(calc_lang, 'continue_invalid')
    user_input = input(prompt)

    while True:
        if user_input.lower() in {'y', 'n'}:
            return user_input.lower()
        user_input = input(other_prompt)

print(point_to_prompt(get_calc_msg(calc_lang, 'welcome')))
PROMPT_1 = point_to_prompt(get_calc_msg(calc_lang, 'first_number'))
PROMPT_2 = point_to_prompt(get_calc_msg(calc_lang, 'second_number'))
PROMPT_3 = point_to_prompt(get_calc_msg(calc_lang, 'continue_prompt'))

OPERATION_PROMPT_1 = get_calc_msg(calc_lang, 'operation_prompt_1')
OPERATION_PROMPT_2 = get_calc_msg(calc_lang, 'operation_prompt_2')


#main program body
def main():
    will_continue = ''
    while will_continue != 'n':

        number1 = check_for_number(PROMPT_1)
        number2 = check_for_number(PROMPT_2)

        print(f'{number1}, {number2}')

        operation = ask_for_operation(OPERATION_PROMPT_1 + OPERATION_PROMPT_2)
        result = return_answer(operation, number1, number2)

        print(print_result(result))
        will_continue = validate_continue(PROMPT_3)

main()