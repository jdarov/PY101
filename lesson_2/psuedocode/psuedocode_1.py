def find_greatest(numbers):

    iterator = 0
    saved_number = numbers[0]

    while iterator < len(numbers):
        currentNumber = numbers[iterator]
        if currentNumber > saved_number:
            saved_number = currentNumber
        iterator += 1

    return saved_number

def ask_for_list(prompt):
    while True:
        user_input = input(prompt)
        if user_input.lower() == 'n':
            return 'n'
        try:
            items = [float(num) for num in user_input.replace(',', ' ').split()]
            if not items:
                print('You need to enter at least one number.')
                continue
            return items
        except ValueError:
            print('Please enter only valid numbers.')

greatest_list = []
while True:
    user_numbers = ask_for_list("Please enter a list of numbers (to stop enter 'n'): ")
    if user_numbers == 'n':
        if not greatest_list:
            print("Nice try, but you didn't enter any numbers!")
            continue
        print(f'The list of greatest numbers from those lists is: {[round(num,2) for num in greatest_list]}')
        break
    greatest = find_greatest(user_numbers)
    greatest_list.append(greatest)