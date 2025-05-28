def validate_input(prompt):
    """
    Validates that the input is a non-negative integer.
    param prompt: The input prompt to display to the user.
    """
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                raise ValueError("Input must be a non-negative integer.")
            return value
        except ValueError:
            print("Please enter a valid non-negative integer.")

def sum_or_product():
    """
    Calculates the sum or product of all integers from 1 to n based on user choice.
    """
    prompt = "Please enter an integer greater than 0:  "
    choice_prompt = "Enter 's' to cmpute the sum, or 'p' to compute the product: "
    n = validate_input(prompt)
    choice = input(choice_prompt).strip().lower()
    while choice not in {'s', 'p'}:
        choice = input("Invalid choice. Please choose 's' or 'p': ").strip().lower()
    match choice:
        case 's':
            result = sum(range(1, n + 1))
            print(f'The sume of all integer from 1 to {n} is {result:,}')
        case 'p':
            result = 1
            for i in range(1, n + 1):
                result *= i
            print(f'The product of all integers from 1 to {n} is {result:,}')

if __name__ == "__main__":
    sum_or_product()
